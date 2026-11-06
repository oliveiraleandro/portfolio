#!/usr/bin/env bash
# Copy the ready-to-serve site; do not regenerate pages or install dependencies.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf dist
mkdir dist
tar --exclude='.DS_Store' --exclude='*.md' --exclude='timeline.json' \
  -cf - index.html .nojekyll css js assets public projects | tar -xf - -C dist

echo "Static publication prepared in dist/"
du -sh dist
