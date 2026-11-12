"""Prepare original generated art into runtime maps, standees and animation atlases."""
from pathlib import Path
from PIL import Image
import argparse,json,hashlib
r=Path(__file__).resolve().parents[1];out=r/'src/assets';parser=argparse.ArgumentParser();parser.add_argument('--masters',type=Path,required=True);g=parser.parse_args().masters
masters={'forest':'exec-98f71bf7-c3ee-46a3-a5b6-23dcdbdecb7f.png','meadow':'exec-1581bc63-bb60-48b7-b9db-f6578e0748ce.png','portraits':'exec-3187aa45-f782-4bba-9aae-08f7de41cea7.png','smith':'exec-c76daa28-a50b-4b40-86d0-20522ba875eb.png','innkeeper':'exec-38177a62-b124-45a2-9db0-7f3a08267ad1.png','resident':'exec-67d9c022-097b-4fc1-bae3-7dec26d65fb4.png'}
def clean(im):
 im=im.convert('RGBA');px=im.load()
 for y in range(im.height):
  for x in range(im.width):
   red,green,blue,a=px[x,y]
   if a<55 or(red>205 and blue<70 and(green<85 or green>195)):px[x,y]=(0,0,0,0)
 return im
for name in ['forest','meadow']:
 Image.open(g/masters[name]).convert('RGB').resize((1536,1024),Image.Resampling.LANCZOS).save(out/f'{name}-v5.webp',quality=91,method=6)
for role in ['smith','innkeeper','resident']:
 im=Image.open(g/masters[role]);sheet=Image.new('RGBA',(512,640))
 for row in range(4):
  for col in range(4):
   frame=clean(im.crop((round(col*im.width/4),round(row*im.height/4),round((col+1)*im.width/4),round((row+1)*im.height/4))))
   bbox=frame.getchannel('A').point(lambda a:255 if a>90 else 0).getbbox();assert bbox;frame=frame.crop(bbox);frame=frame.resize((round(frame.width*144/frame.height),144),Image.Resampling.LANCZOS)
   feet=frame.getchannel('A').crop((0,123,frame.width,144)).getbbox();anchor=(feet[0]+feet[2])/2 if feet else frame.width/2
   sheet.alpha_composite(frame,(round(col*128+64-anchor),row*160+8))
 sheet.save(out/f'npc-{role}-v5.png',optimize=True)
im=Image.open(g/masters['portraits'])
for col,role in enumerate(['bram','mira','elian']):
 frame=clean(im.crop((round(col*im.width/3),0,round((col+1)*im.width/3),im.height)))
 bbox=frame.getchannel('A').point(lambda a:255 if a>90 else 0).getbbox();assert bbox;frame=frame.crop(bbox);frame.thumbnail((500,960),Image.Resampling.LANCZOS)
 # Clear hidden RGB to keep transparent standees compact and correctly composited.
 canvas=Image.new('RGBA',frame.size);canvas.alpha_composite(frame);canvas.save(out/f'dialogue-{role}-v5.webp',quality=93,method=6)
records=[]
for p in sorted(out.glob('*v5.*')):records.append({'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'tool':'built-in imagegen; runtime crop, alpha cleanup and resizing only'})
(r/'docs/V05_ART_SOURCES.json').write_text(json.dumps({'assets':records,'master_sha256':{k:hashlib.sha256((g/v).read_bytes()).hexdigest() for k,v in masters.items()},'prompts':{'forest':'Preserve existing forest layout; add a west-edge sandy entry at y590 and clear its blocking log.','meadow':'Original orthographic autumn meadow, north entry x760; central clearing, orchard, fountain, herbs and picnic area.','portraits':'Three consistent original characters Bram/Mira/Elian as high-resolution transparent dialogue standees; no UI.','npc_animation':'One 4×4 sheet per character: four front idle gestures/blink frames, four left walk frames, four right walk frames, four back walk frames; transparent, fixed scale/baseline.'}},indent=2)+'\n');print(records)
