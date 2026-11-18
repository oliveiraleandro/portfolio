"""Regression checks for editorial changes, validation and read-only checking."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import build_site
from site_content import ROOT, blocks, inline, load_cases, load_home, read_case, render_case


class ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = load_cases()

    def test_generated_pages_match_repository(self):
        for path, rendered in build_site.generate_outputs().items():
            self.assertEqual(path.read_text(), rendered, str(path))

    def test_editorial_change_reaches_all_home_themes_and_case(self):
        cases = copy.deepcopy(self.cases)
        case = cases['datacare']
        case['name'] = 'Datacare & pesquisa'
        case['card']['description'] = 'Resumo com <texto> & "aspas".'
        case['title'] = 'Título **revisado**'
        case['body'] = 'Abertura revisada.\n\nNovo parágrafo com **ênfase**.'
        case['captions']['caption_1'] = 'Nova legenda.'
        with patch.object(build_site, 'load_cases', return_value=cases):
            outputs = build_site.generate_outputs()
        page = outputs[ROOT / 'projects/datacare/index.html']
        self.assertIn('<h1>Título <strong>revisado</strong></h1>', page)
        self.assertIn('<p class="case-lead">Abertura revisada.</p>', page)
        self.assertIn('Nova legenda.', page)
        for path, html in outputs.items():
            if path == ROOT / 'index.html' or path.parent.parent == ROOT / 'themes':
                self.assertIn('Datacare &amp; pesquisa', html)
                self.assertIn('Resumo com &lt;texto&gt; &amp; &quot;aspas&quot;.', html)

    def test_missing_image_and_cross_page_anchor_fail(self):
        page = ROOT / 'projects/datacare/index.html'
        for href in ('images/does-not-exist.png', '../sebrae/#does-not-exist'):
            with self.subTest(href=href), self.assertRaises(ValueError):
                build_site.validate_outputs({page: f'<a href="{href}">Link</a>'})

    def test_missing_caption_or_next_case_fail(self):
        for field in ('captions', 'next'):
            cases = copy.deepcopy(self.cases)
            if field == 'captions':
                cases['datacare']['captions'].pop('caption_1')
            else:
                cases['datacare']['next'] = 'inexistente'
            with self.subTest(field=field), self.assertRaises(ValueError):
                render_case(cases['datacare'], cases, load_home(cases))

    def test_invalid_front_matter_and_required_fields(self):
        source = (ROOT / 'projects/datacare/content.md').read_text()
        for raw in ('# Sem campos', source.replace('name = "Datacare"', 'name = ""'),
                    source.replace('tags = [', 'tags = INVALID [')):
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'datacare/content.md'
                path.parent.mkdir()
                path.write_text(raw)
                with patch('site_content.ROOT', Path(directory)), self.assertRaises(ValueError):
                    read_case(path)

    def test_markup_is_escaped_and_unsafe_links_rejected(self):
        self.assertEqual(inline('<script>'), '&lt;script&gt;')
        self.assertIn('<em>texto</em>', inline('_texto_'))
        self.assertIn('<h2>Seção</h2>', blocks('## Seção\n\nTexto.'))
        with self.assertRaises(ValueError):
            inline('[Abrir](javascript:alert)')
        with self.assertRaises(ValueError):
            blocks('- Lista não suportada')

    def test_check_never_writes_stale_output(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'index.html'
            path.write_text('anterior')
            with patch.object(build_site, 'ROOT', Path(directory)), \
                 patch.object(build_site, 'generate_outputs', return_value={path: 'novo'}), \
                 patch.object(sys, 'argv', ['build_site.py', '--check']), \
                 self.assertRaises(SystemExit):
                build_site.main()
            self.assertEqual(path.read_text(), 'anterior')

    def test_invalid_content_does_not_write(self):
        with patch.object(build_site, 'generate_outputs', side_effect=ValueError('inválido')), \
             patch.object(Path, 'write_text') as write, \
             patch.object(sys, 'argv', ['build_site.py']), self.assertRaises(SystemExit):
            build_site.main()
        write.assert_not_called()


if __name__ == '__main__':
    unittest.main()
