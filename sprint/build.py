from pathlib import Path
import json
P = Path(__file__).parent
html = (P/'src/shell.html').read_text()
html = html.replace('__CSS__', (P/'src/style.css').read_text())
data = json.loads((P/'src/content.json').read_text())
html = html.replace('__DATA__', json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
html = html.replace('__APP__', (P/'src/app.js').read_text())
out = P.parent/'docs/index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(html)
print('Built', out, len(html.encode()), 'bytes')
