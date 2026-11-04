"""Check locale routing, shared assets, and translation completeness."""

from html.parser import HTMLParser
import unittest
from urllib.parse import unquote, urljoin, urlsplit

from build_locales import EnglishPage, PAGES, ROOT, generate


class Elements(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.tags = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class LocaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = generate()

    def test_all_assets_links_and_fragments_exist(self):
        for prefix in ("/", "/portfolio/"):
            for page, content in self.pages.items():
                for tag, attrs in Elements(content).tags:
                    for attr in ("href", "src"):
                        value = attrs.get(attr)
                        if not value:
                            continue
                        url = urlsplit(urljoin("https://example.test" + prefix + page, value))
                        if url.netloc != "example.test":
                            continue
                        with self.subTest(page=page, prefix=prefix, url=value):
                            self.assertTrue(url.path.startswith(prefix))
                            path = unquote(url.path[len(prefix):])
                            target = ROOT / path
                            if target.is_dir():
                                target /= "index.html"
                            self.assertTrue(target.is_file(), str(target))
                            if url.fragment and target.suffix == ".html":
                                ids = {a.get("id") for _, a in Elements(target.read_text()).tags}
                                self.assertIn(unquote(url.fragment), ids)

    def test_english_navigation_keeps_language(self):
        for source in PAGES:
            pt = Elements(self.pages[source]).tags
            en = Elements(self.pages["en/" + source]).tags
            # Switcher links intentionally cross locales and are checked separately.
            pt_links = [a["href"] for t, a in pt if t == "a" and "lang" not in a]
            en_links = [a["href"] for t, a in en if t == "a" and "lang" not in a]
            self.assertEqual(len(pt_links), len(en_links))
            for before, after in zip(pt_links, en_links):
                original = urlsplit(urljoin("https://example.test/" + source, before))
                translated = urlsplit(urljoin("https://example.test/en/" + source, after))
                path = original.path.lstrip("/")
                candidate = path + "index.html" if path.endswith("/") or not path else path
                expected = "/en" + original.path if candidate in PAGES else original.path
                with self.subTest(source=source, link=before):
                    self.assertEqual(translated.path, expected)
                    self.assertEqual(translated.query, original.query)
                    self.assertEqual(translated.fragment, original.fragment)

    def test_switchers_are_reciprocal_and_language_is_declared(self):
        for page, content in self.pages.items():
            tags = Elements(content).tags
            english = page.startswith("en/")
            source = page.removeprefix("en/")
            self.assertEqual(next(a["lang"] for t, a in tags if t == "html"), "en-US" if english else "pt-BR")
            links = [a for t, a in tags if t == "a" and "language-option" in a.get("class", "")]
            self.assertEqual(len(links), 2)
            self.assertEqual(sum(a.get("aria-current") == "page" for a in links), 1)
            for a in links:
                expected = ("en/" if a["lang"] == "en-US" else "") + source
                resolved = urlsplit(urljoin("https://example.test/" + page, a["href"])).path.lstrip("/")
                self.assertEqual(resolved + "index.html", expected)

    def test_missing_translation_fails_instead_of_falling_back(self):
        parser = EnglishPage("index.html", {})
        with self.assertRaisesRegex(ValueError, "missing translation"):
            parser.feed("<p>Texto novo</p>")

    def test_generated_files_are_current(self):
        for page, content in self.pages.items():
            self.assertEqual((ROOT / page).read_text(), content, page)


if __name__ == "__main__":
    unittest.main()
