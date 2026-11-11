"""Package only this project's authored source and web-ready files."""
from pathlib import Path
import zipfile,hashlib,json
r=Path(__file__).resolve().parents[1];out=r/'artifacts/delivery';out.mkdir(parents=True,exist_ok=True)
def make(name,files):
 p=out/name
 with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for disk,archive in sorted(files,key=lambda x:str(x[1])):z.write(disk,str(archive))
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
 return {'file':name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
web=[]
for p in (r/'src').rglob('*'):
 if p.is_file():web.append((r/'dist'/p.relative_to(r/'src'),Path('Emberbrook')/p.relative_to(r/'src')))
for n in ['vendor/phaser.min.js','vendor/PHASER-LICENSE.md','.nojekyll']:web.append((r/'dist'/n,Path('Emberbrook')/n))
web.append((r/'docs/TEST_BUILD_ZH.md',Path('Emberbrook/READ-ME.md')))
source=[]
for folder in ['src','scripts','tests','docs','.github']:
 for p in (r/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:source.append((p,Path('Emberbrook-source')/p.relative_to(r)))
for n in ['README.md','PROJECT.json','CHANGELOG.md','ENVIRONMENT.md','package.json','package-lock.json','.gitignore']:
 source.append((r/n,Path('Emberbrook-source')/n))
report=[make('Emberbrook-playable-v0.3.zip',web),make('Emberbrook-source-v0.3.zip',source)]
(out/'SHA256SUMS.txt').write_text(''.join(x['sha256']+'  '+x['file']+'\n' for x in report))
print(json.dumps(report,indent=2))
