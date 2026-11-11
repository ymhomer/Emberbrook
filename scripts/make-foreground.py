"""Extract an original-pixel foreground layer so actors can pass behind roofs."""
from pathlib import Path
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parents[1]
im=Image.open(r/'src/assets/village.webp').convert('RGBA');mask=Image.new('L',im.size);d=ImageDraw.Draw(mask)
# A front-facing village house and forge are composited above actors behind their footprints.
d.polygon([(126,292),(188,219),(241,200),(241,149),(285,149),(285,202),(384,139),(493,157),(554,271),(596,309),(575,449),(139,465),(110,370)],fill=255)
d.polygon([(845,302),(929,177),(1115,184),(1188,237),(1194,270),(1296,322),(1310,356),(1277,491),(1157,499),(1125,454),(896,470)],fill=255)
layer=Image.new('RGBA',im.size);layer.paste(im,(0,0),mask)
assert Image.alpha_composite(im,layer).tobytes()==im.tobytes()
layer.save(r/'src/assets/foreground.png',optimize=True)
