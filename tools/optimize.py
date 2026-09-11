from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[1]
source=R/'assets/img/mascot-diana.png'
with Image.open(source) as im:
 im.thumbnail((1400,1600));im.save(R/'assets/img/mascot-diana.webp','WEBP',quality=94,method=6)
thumbs=R/'assets/img/responsive';thumbs.mkdir(exist_ok=True)
for source in (R/'assets/img').rglob('*.webp'):
 if 'responsive' in source.parts:continue
 with Image.open(source) as im:
  if im.width<=800:continue
  im.thumbnail((800,1600))
  relative=source.relative_to(R/'assets/img').as_posix().replace('/','--')
  im.save(thumbs/relative,'WEBP',quality=92,method=6)
print('Hero optimized:',(R/'assets/img/mascot-diana.webp').stat().st_size,'bytes')
