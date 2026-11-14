#!/usr/bin/env bash
# Copy the ready-to-serve site; do not regenerate pages or install dependencies.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/build_themes.py --check
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
