"""Render authored navigation for review; outputs stay in ignored artifacts/."""
from pathlib import Path
from PIL import Image,ImageDraw
import subprocess,json
r=Path(__file__).resolve().parents[1]
nav=json.loads(subprocess.check_output(['node','-e',"console.log(JSON.stringify(require('./src/navigation.js')))"] ,cwd=r,text=True))
for name,region in nav['regions'].items():
 im=Image.open(r/'src/assets'/f'{name}.webp').convert('RGBA');layer=Image.new('RGBA',im.size);d=ImageDraw.Draw(layer)
 for polygon in region['ground']:d.polygon([tuple(p) for p in polygon],fill=(80,210,150,60),outline=(185,240,160,190),width=2)
 for rect in region['rectBlocks']:d.rectangle(tuple(rect),fill=(220,80,80,85))
 for polygon in region['polyBlocks']:d.polygon([tuple(p) for p in polygon],fill=(220,80,80,85))
 for portal in nav['portals'][name]:
  x,y,rad=portal['x'],portal['y'],portal['radius'];d.ellipse((x-rad,y-rad,x+rad,y+rad),outline=(240,210,90,255),width=3)
 Image.alpha_composite(im,layer).save(r/'artifacts'/f'{name}-navigation-v04.png')
