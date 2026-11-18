#!/usr/bin/env bash
# Generate and validate editorial content before preparing the static site.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build_site.py
python3 scripts/build_site.py --check
python3 scripts/check_styles.py

rm -rf dist
mkdir dist
tar --exclude='.DS_Store' --exclude='*.md' --exclude='timeline.json' \
  -cf - index.html .nojekyll css js assets public projects | tar -xf - -C dist

# Ship only the CSS, scripts and artwork used by the generated homepage.
for config in themes/*/theme.json; do
  directory=${config%/theme.json}
  mkdir -p "dist/$directory"
  for asset in "$directory"/*; do
    case "$asset" in
      *.html|*.json|*.md) continue ;;
    esac
    cp -R "$asset" "dist/$directory/"
  done
done

echo "Static publication prepared in dist/"
du -sh dist
