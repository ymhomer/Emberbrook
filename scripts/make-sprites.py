"""Create original transparent pixel-art character frames; no external sprite pack."""
from pathlib import Path
from PIL import Image, ImageDraw
out=Path(__file__).resolve().parents[1]/'src/assets'
def actor(direction,frame,palette='hero'):
 im=Image.new('RGBA',(40,48));d=ImageDraw.Draw(im)
 back=direction==3;side=direction in (1,2);flip=direction==2
 edge='#253030';hair='#a24d29';light='#e5a348';hairHi='#f2bd65';skin='#dfad7a';skinHi='#f2c692';skinShade='#ae7657';coat='#416e68';coatLight='#689284';coatShadow='#294c49';pants='#353c3e';boot='#574538';trim='#c9b374'
 if palette=='smith':hair='#60402e';light='#9d6d48';coat='#785846';coatLight='#aa8254';coatShadow='#493f35'
 if palette=='innkeeper':hair='#49322d';light='#885f43';coat='#8d5e67';coatLight='#b88088';coatShadow='#623f4b'
 if palette=='resident':hair='#5d4b2d';light='#ac995e';coat='#68784d';coatLight='#97a374';coatShadow='#46523b'
 bob=1 if frame in (1,3) else 0;y=bob
 step=[0,2,0,-2][frame]
 def rect(box,c):d.rectangle(tuple(box),fill=c)
 # Legs, shoes and asymmetric stride.
 rect((13,31+y,18,41+y+max(0,step)),edge);rect((21,31+y,26,41+y+max(0,-step)),edge)
 rect((14,32+y,17,40+y+max(0,step)),pants);rect((22,32+y,25,40+y+max(0,-step)),pants)
 rect((12,40+y+max(0,step),18,44+y+max(0,step)),boot);rect((21,40+y+max(0,-step),27,44+y+max(0,-step)),boot)
 rect((13,41+y+max(0,step),17,41+y+max(0,step)),'#8b7455');rect((22,41+y+max(0,-step),26,41+y+max(0,-step)),'#8b7455')
 # Cloak silhouette, tunic, belt, leather satchel.
 d.polygon([(11,20+y),(27,20+y),(30,34+y),(10,34+y)],fill=edge)
 d.polygon([(12,21+y),(26,21+y),(28,33+y),(12,33+y)],fill=coat)
 rect((15,22+y,24,31+y),coatLight);rect((12,27+y,14,33+y),coatShadow)
 rect((13,31+y,26,33+y),'#70513b');rect((19,31+y,21,33+y),trim)
 rect((10,22+y,13,31+y),edge);rect((11,23+y,14,29+y),coatLight);rect((11,30+y,14,33+y),skin)
 rect((26,23+y,29,31+y),edge);rect((26,24+y,28,29+y),coat);rect((26,30+y,29,33+y),skin)
 # scarf and strap.
 rect((17,19+y,23,23+y),'#e3c38d');rect((22,22+y,24,28+y),'#b99b69')
 d.line([(12,23+y),(25,32+y)],fill='#997850',width=2);rect((24,28+y,30,35+y),edge);rect((25,29+y,29,34+y),'#8b6545');rect((26,30+y,29,30+y),'#c39357')
 # Head border and face.
 d.rounded_rectangle((10,5+y,29,22+y),radius=5,fill=edge)
 rect((12,10+y,27,19+y),skin);rect((15,19+y,25,21+y),skin);rect((14,12+y,25,18+y),skinHi);rect((26,12+y,28,17+y),skinShade)
 if not back:
  if side:
   rect((12,13+y,14,15+y),edge);rect((11,16+y,14,17+y),skinHi);rect((15,18+y,18,18+y),skinShade)
  else:
   rect((15,13+y,16,15+y),edge);rect((23,13+y,24,15+y),edge);rect((17,18+y,22,18+y),skinShade);rect((19,15+y,20,16+y),'#ce9564')
 # Layered copper hair.
 d.polygon([(10,12+y),(9,7+y),(13,6+y),(14,3+y),(19,4+y),(23,2+y),(27,6+y),(30,8+y),(28,15+y),(25,12+y),(24,9+y),(20,11+y),(17,8+y),(14,11+y)],fill=hair)
 d.polygon([(11,8+y),(14,7+y),(15,4+y),(20,5+y),(23,4+y),(27,7+y),(25,9+y),(21,8+y),(18,10+y),(16,7+y),(13,10+y)],fill=light)
 d.line([(14,6+y),(18,5+y),(21,7+y)],fill=hairHi,width=1);rect((27,9+y,28,13+y),hair)
 if back:
  d.rounded_rectangle((11,7+y,28,21+y),radius=4,fill=hair);rect((13,8+y,26,15+y),light);d.line([(13,8+y),(22,7+y)],fill=hairHi,width=1)
 if flip:im=im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
 return im
sheet=Image.new('RGBA',(160,192))
for row in range(4):
 for f in range(4):sheet.paste(actor(row,f),(f*40,row*48))
sheet.save(out/'hero.png')
for palette in ('smith','innkeeper','resident'):
 atlas=Image.new('RGBA',(160,192))
 for row in range(4):
  for f in range(4):atlas.paste(actor(row,f,palette),(f*40,row*48))
 atlas.save(out/('npc-'+palette+'.png'))
# Portrait uses matching original sprite palette in a hand-built vignette.
p=Image.new('RGBA',(96,112),'#374d3c');d=ImageDraw.Draw(p);d.ellipse((-12,-5,110,130),fill='#647954');d.ellipse((3,12,90,122),fill='#74875a')
face=actor(0,0).crop((5,0,35,30)).resize((108,108),Image.Resampling.NEAREST);p.alpha_composite(face,(-6,6));p.convert('RGB').save(out/'portrait.png')
# Small original item graphics sit on the map as additional independent sprites.
for name in ['timber','ore','wisp']:
 im=Image.new('RGBA',(48,48));d=ImageDraw.Draw(im)
 if name=='timber':
  for x,y in [(7,22),(19,17),(26,27)]:
   d.rounded_rectangle((x,y,x+17,y+10),radius=4,fill='#48362c',outline='#cfab62',width=1);d.ellipse((x,y,x+9,y+10),fill='#bb9659',outline='#5b402a');d.ellipse((x+3,y+3,x+6,y+7),outline='#755332')
 elif name=='ore':
  d.polygon([(4,37),(10,22),(22,15),(38,19),(45,34),(32,42),(13,42)],fill='#586a6b',outline='#2e3f42');d.polygon([(10,23),(22,15),(27,26),(16,30)],fill='#94aaa3');d.polygon([(27,26),(38,19),(45,34),(32,38)],fill='#6b8280');d.polygon([(18,28),(23,18),(28,31),(23,35)],fill='#ddc394');d.polygon([(31,33),(35,25),(39,34)],fill='#c6b287')
 else:
  d.ellipse((9,6,39,36),fill='#655b9b',outline='#b9c8ef',width=2);d.polygon([(9,24),(7,42),(17,37),(24,44),(31,37),(40,42),(39,24)],fill='#655b9b');d.ellipse((12,9,35,28),fill='#9b95cf');d.rectangle((16,19,19,23),fill='#19283a');d.rectangle((28,19,31,23),fill='#19283a');d.rectangle((22,28,26,29),fill='#d6d4f6')
 im.save(out/(name+'.png'))
(out/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#253c2c"/><path d="M49 12C19 9 9 29 22 43c17 8 32-10 27-31Z" fill="#b9bb79"/><path d="M16 51 40 24" stroke="#f0d695" stroke-width="4"/></svg>')
print('Created original 16-frame hero, portrait, map items, favicon')
