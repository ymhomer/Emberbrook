"""Fetch self-hosted subsets from Google Fonts, then record source URLs and hashes."""
from pathlib import Path
import urllib.request,urllib.parse,re,hashlib,json
root=Path(__file__).resolve().parents[1];dest=root/'src/assets/fonts'
ui=(root/'src/ui.js').read_text()+(root/'src/index.html').read_text()
characters=''.join(sorted(set(''.join(c for c in ui if ord(c)>127)+'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;!?/\\-–—+−=()[]{}<>%&’\'“”·…✦↗☀☕⚒◈◇↓✓×⤢')))
assets=[]
for family,name,chars in [('Noto Sans TC:wght@400','ui.ttf',characters),('Cormorant Garamond:wght@500','display.ttf','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;!?/+-’\'')]:
 url='https://fonts.googleapis.com/css2?'+urllib.parse.urlencode({'family':family,'text':chars,'display':'swap'})
 request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 Chrome/120.0.0.0 Safari/537.36'})
 css=urllib.request.urlopen(request,timeout=30).read().decode()
 link=re.search(r'url\((https://[^)]+)\)',css).group(1)
 data=urllib.request.urlopen(link,timeout=30).read();(dest/name).write_bytes(data)
 assets.append({'family':family,'file':name,'source':link,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
 print(name,len(data))
(root/'docs/FONT_SOURCES.json').write_text(json.dumps(assets,indent=2))
for family in ['notosanstc','cormorantgaramond']:
 link='https://raw.githubusercontent.com/google/fonts/main/ofl/'+family+'/OFL.txt'
 data=urllib.request.urlopen(link,timeout=30).read();(dest/(family+'-OFL.txt')).write_bytes(data)
