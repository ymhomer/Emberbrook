"""Prepare generated original artwork as runtime assets without changing originals."""
from pathlib import Path
from PIL import Image, ImageDraw
import json,hashlib
root=Path(__file__).resolve().parents[1]
g=Path('/home/ymhomer/.codex/generated_images/01a197d8-bd4b-75b0-bde2-f7a41d5d56d9')
forest=Image.open(g/'exec-6bcb29c4-273c-4748-bd30-380028b4e910.png').convert('RGB')
forest.resize((1536,1024),Image.Resampling.LANCZOS).save(root/'src/assets/forest.webp',quality=92,method=6)
im=Image.open(g/'exec-562e7c27-8ca5-4814-8175-7e9c73e39281.png').convert('RGBA')
atlas=Image.new('RGBA',(512,640));frames=[]
for row in range(4):
 for col in range(4):
  frame=im.crop((round(col*im.width/4),round(row*im.height/4),round((col+1)*im.width/4),round((row+1)*im.height/4)))
  # Remove isolated red matte fringes from the generated cutout.
  pixels=frame.load()
  for y in range(frame.height):
   for x in range(frame.width):
    r,gc,b,a=pixels[x,y]
    if r>170 and gc<55 and b<65:pixels[x,y]=(0,0,0,0)
  bounds=frame.getchannel('A').point(lambda a:255 if a>30 else 0).getbbox()
  assert bounds
  frame=frame.crop(bounds);h=144;w=round(frame.width*h/frame.height)
  frame=frame.resize((w,h),Image.Resampling.LANCZOS)
  atlas.alpha_composite(frame,(col*128+(128-w)//2,row*160+8));frames.append(frame)
atlas.save(root/'src/assets/hero-v3.png',optimize=True)
portrait=frames[1].crop((0,0,frames[1].width,75)).resize((128,128),Image.Resampling.LANCZOS)
canvas=Image.new('RGBA',(128,128),'#516747');canvas.alpha_composite(portrait);canvas.convert('RGB').save(root/'src/assets/portrait-v3.png')
village=Image.open(root/'src/assets/village.webp').convert('RGBA');mask=Image.new('L',village.size);draw=ImageDraw.Draw(mask);draw.polygon([(627,772),(650,741),(700,732),(752,738),(804,744),(848,777),(840,815),(790,815),(780,836),(655,830),(645,810),(624,810)],fill=255);arch=Image.new('RGBA',village.size);arch.paste(village,(0,0),mask);arch.save(root/'src/assets/arch-v3.png',optimize=True)
records=[]
for name in ['forest.webp','hero-v3.png','portrait-v3.png','arch-v3.png']:
 p=root/'src/assets'/name;records.append({'file':'src/assets/'+name,'source':'Built-in imagegen; original Emberbrook artwork; runtime crop/resize only','sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(root/'docs/V03_ART_SOURCES.json').write_text(json.dumps(records,indent=2)+'\n')
print(records)
