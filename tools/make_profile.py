from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from matplotlib import get_data_path
R=Path(__file__).resolve().parents[1]
F=Path(get_data_path())/'fonts/ttf'
pdfmetrics.registerFont(TTFont('DianaSans',str(F/'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DianaBold',str(F/'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('DianaSans',normal='DianaSans',bold='DianaBold')
c=canvas.Canvas(str(R/'assets/docs/diana-designer-profile.pdf'),pagesize=(595.28,841.89))
c.setTitle('Диана Тхайцухова — профессиональный профиль')
c.setAuthor('Диана Тхайцухова')
c.setFillColor(HexColor('#101112'));c.rect(0,678,595.28,164,fill=1,stroke=0)
c.setFillColor(HexColor('#e9b97a'));c.setFont('DianaSans',9);c.drawString(44,806,'ПОРТФОЛИО / ПРОФЕССИОНАЛЬНЫЙ ПРОФИЛЬ')
c.setFillColor(HexColor('#f4f1eb'));c.setFont('DianaSans',27);c.drawString(44,765,'Диана Тхайцухова')
c.setFont('DianaSans',12);c.drawString(44,735,'Графический дизайнер')
c.setFont('DianaSans',10);c.drawString(44,709,'Айдентика · упаковка · полиграфия · редакционный дизайн')
style=ParagraphStyle('body',fontName='DianaSans',fontSize=10.2,leading=15,textColor=HexColor('#333638'))
head=ParagraphStyle('head',fontName='DianaBold',fontSize=11,leading=15,textColor=HexColor('#151719'))
y=648

def p(text,st=style,gap=10):
 global y
 para=Paragraph(text,st);_,h=para.wrap(506,800);para.drawOn(c,44,y-h);y-=h+gap

def section(title):
 global y
 y-=8;c.setStrokeColor(HexColor('#d5d4d0'));c.line(44,y,551,y);y-=18;p(title,head,8)

p('Разрабатываю визуальный образ бренда и материалы для печатных и цифровых носителей. Рассматриваю работу в графическом дизайне и UX/UI. Основная специализация портфолио — графический дизайн.')
section('Проекты')
p('<b>Реализованные:</b> GASTRO PORT, «Северная заря».',gap=7)
p('<b>Учебные:</b> «Говори» — айдентика образовательного проекта; «Потерянное бюро» — айдентика и городская среда; «Язык взаимопонимания» — книга и дневник; CALMES — айдентика и упаковка.',gap=7)
p('<b>Авторская практика:</b> творческая мастерская «Хуторок» — работа с материалами, декором и 3D-печатью.')
section('Инструменты и задачи')
p('<b>Illustrator</b> — логотипы, векторная графика и носители.<br/><b>Photoshop</b> — изображения, ретушь и презентационные композиции.<br/><b>InDesign</b> — книги и многостраничная вёрстка.<br/><b>Figma</b> — цифровые макеты, презентации и прототипы.<br/><b>PowerPoint</b> — оформление презентаций.')
section('Образование')
p('<b>КТМУ</b> — дизайн.<br/><b>ВШТЭ</b> — «Искусственный интеллект в информационных системах».')
section('Контакты')
p('<link href="mailto:Soulminori2.0@gmail.com" color="#333638">Soulminori2.0@gmail.com</link><br/><link href="https://t.me/soulminori" color="#333638">Telegram: @soulminori</link><br/><link href="https://soulminori.netlify.app/" color="#333638">Портфолио: soulminori.netlify.app</link>')
assert y>35,y
c.setFont('DianaSans',8);c.setFillColor(HexColor('#6a6d6e'));c.drawString(44,25,'Диана Тхайцухова / Профессиональный профиль');c.drawRightString(551,25,'2026')
c.showPage();c.save();print('Profile created, bottom:',round(y))
