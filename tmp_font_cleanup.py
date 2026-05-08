from pathlib import Path
import re
root = Path('resources/views')
for path in root.rglob('*.blade.php'):
    text = path.read_text(encoding='utf-8')
    updated = text
    updated = re.sub('(?m)^\s*{{-- Fonts: Geist & Geist Mono --}}\s*$\n', '', updated)
    updated = re.sub('(?m)^\s*<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?family=.*?"\s*>\s*$\n', '', updated)
    updated = re.sub("font-family:\s*'Geist',[^;]+;", "font-family: 'Harmonia Sans W01', ui-sans-serif, system-ui, sans-serif;", updated)
    updated = re.sub("font-family:\s*'Geist Mono',[^;]+;", '', updated)
    updated = re.sub('\bfont-geist-mono\b', 'font-harmonia', updated)
    updated = re.sub('body class="([^"]*)font-geist([^"]*)"', 'body class="\1font-harmonia\2"', updated)
    if updated != text:
        path.write_text(updated, encoding='utf-8')
        print('Updated', path)
