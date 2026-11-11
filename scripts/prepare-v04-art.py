"""Normalize original generated NPCs and extract runtime occlusion/water masks."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib,argparse
r=Path(__file__).resolve().parents[1];out=r/'src/assets'
parser=argparse.ArgumentParser();parser.add_argument('--npc-sheet',type=Path,required=True);src=parser.parse_args().npc_sheet
im=Image.open(src).convert('RGBA');portraits=Image.new('RGBA',(384,152),'#52674c')
for row,role in enumerate(['smith','innkeeper','resident']):
 sheet=Image.new('RGBA',(512,160))
 for col in range(4):
  frame=im.crop((round(col*im.width/4),round(row*im.height/3),round((col+1)*im.width/4),round((row+1)*im.height/3)))
  px=frame.load()
  for y in range(frame.height):
   for x in range(frame.width):
    red,green,blue,alpha=px[x,y]
    if alpha<55 or (red>205 and blue<70 and (green<85 or green>195)):px[x,y]=(0,0,0,0)
  bbox=frame.getchannel('A').point(lambda a:255 if a>90 else 0).getbbox();assert bbox
  frame=frame.crop(bbox);w=round(frame.width*144/frame.height);frame=frame.resize((w,144),Image.Resampling.LANCZOS);sheet.alpha_composite(frame,((128-w)//2+128*col,8))
  if col==0:
   face=frame.crop((0,0,frame.width,80)).resize((128,152),Image.Resampling.LANCZOS);portraits.alpha_composite(face,(row*128,0))
 sheet.save(out/f'npc-{role}-v4.png',optimize=True)
portraits.save(out/'npc-portraits-v4.png',optimize=True)
village=Image.open(out/'village.webp').convert('RGBA');mask=Image.new('L',village.size);d=ImageDraw.Draw(mask);d.polygon([(1208,602),(1255,606),(1402,604),(1444,602),(1448,636),(1400,648),(1245,645),(1200,630)],fill=255);layer=Image.new('RGBA',village.size);layer.paste(village,(0,0),mask);layer.save(out/'bridge-front-v4.png',optimize=True)
for scene in ['village','forest']:
 mask=Image.new('RGBA',(512,1024));d=ImageDraw.Draw(mask)
 if scene=='village':
  polys=[[(1415,0),(1470,0),(1455,70),(1410,130),(1450,205),(1435,285),(1465,355),(1425,440),(1380,510),(1320,550),(1285,545),(1350,485),(1375,395),(1390,325),(1385,250),(1370,180),(1380,90)],[(1285,652),(1395,645),(1410,700),(1415,750),(1390,800),(1455,870),(1470,940),(1536,1000),(1536,1024),(1435,990),(1360,930),(1320,865),(1300,810),(1270,755),(1250,700)]]
  holes=[(1320,690,1355,725),(1370,750,1410,780),(1300,735,1330,765),(1400,910,1445,945)]
 else:
  polys=[[(1280,370),(1420,350),(1536,375),(1536,790),(1450,805),(1380,770),(1270,785),(1150,720),(1115,650),(1125,605),(1300,590),(1310,525),(1220,505),(1200,465)]];holes=[]
 for p in polys:d.polygon([(x-1024,y) for x,y in p],fill=(255,255,255,255))
 for x1,y1,x2,y2 in holes:d.ellipse((x1-1024,y1,x2-1024,y2),fill=(0,0,0,0))
 mask.save(out/f'water-mask-{scene}-v4.png',optimize=True)
files=list(out.glob('*v4.png'));(r/'docs/V04_ART_SOURCES.json').write_text(json.dumps([{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'source':'Original imagegen NPC sheet' if 'npc-' in p.name else 'Derived mask or foreground from original Emberbrook map'} for p in files],indent=2)+'\n');print([(p.name,p.stat().st_size) for p in files])
