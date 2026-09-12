"""Create a light two-page recruiter resume with an honest product focus."""
from pathlib import Path
import json
from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from PIL import Image

R = Path(__file__).resolve().parents[1]
OUT = R / 'assets/docs/diana-tkhaytsukhova-resume.pdf'

for name, filename in [
    ('Body', 'manrope-regular.ttf'),
    ('Bold', 'manrope-semibold.ttf'),
    ('Display', 'unbounded-semibold.ttf'),
]:
    pdfmetrics.registerFont(TTFont(name, str(R / 'assets/fonts' / filename)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Bold')

W, H = 595.28, 841.89
PAPER = HexColor('#f6f3ef')
INK = HexColor('#30221f')
MUTED = HexColor('#6a605c')
LINE = HexColor('#d2cbc4')
BLUE = HexColor('#b3cad7')
ORANGE = HexColor('#ce4829')
PINK = HexColor('#eebbbb')
LILAC = HexColor('#c9bdf1')
SKY = HexColor('#91bfe7')

c = canvas.Canvas(str(OUT), pagesize=(W, H))
c.setTitle('Диана Тхайцухова - резюме графического дизайнера, UX/UI')
c.setAuthor('Диана Тхайцухова')
c.setSubject('Резюме графического дизайнера с развитием в UX/UI и продуктовом дизайне')

styles = {
    'body': ParagraphStyle('body', fontName='Body', fontSize=9.3, leading=13.7, textColor=INK),
    'small': ParagraphStyle('small', fontName='Body', fontSize=8.1, leading=11.3, textColor=MUTED),
    'head': ParagraphStyle('head', fontName='Display', fontSize=12.4, leading=16.8, textColor=INK),
    'label': ParagraphStyle('label', fontName='Bold', fontSize=8.3, leading=11.2, textColor=ORANGE),
    'card': ParagraphStyle('card', fontName='Body', fontSize=8.35, leading=11.6, textColor=INK),
}


def compact_image(path, max_px=1000, quality=84):
    """Embed a screen-sized JPEG instead of the multi-megabyte source."""
    image = Image.open(path).convert('RGB')
    image.thumbnail((max_px, max_px), Image.Resampling.LANCZOS)
    buffer = BytesIO()
    image.save(buffer, format='JPEG', quality=quality, optimize=True)
    buffer.seek(0)
    return ImageReader(buffer)


def soft_gradient(width=1200, height=470):
    """Create a subtle pink-lilac-blue wash for the top of each page."""
    stops = [(245, 220, 226), (235, 229, 241), (220, 235, 244)]
    line = Image.new('RGB', (width, 1))
    pixels = []
    for x in range(width):
        t = x / max(1, width - 1)
        if t <= .5:
            a, b, q = stops[0], stops[1], t * 2
        else:
            a, b, q = stops[1], stops[2], (t - .5) * 2
        pixels.append(tuple(round(a[i] + (b[i] - a[i]) * q) for i in range(3)))
    line.putdata(pixels)
    gradient = line.resize((width, height))
    base = Image.new('RGB', (width, height), (246, 243, 239))
    mask = Image.new('L', (1, height))
    mask.putdata([round(205 * (1 - y / max(1, height - 1)) ** 1.5) for y in range(height)])
    gradient = Image.composite(gradient, base, mask.resize((width, height)))
    buffer = BytesIO()
    gradient.save(buffer, format='PNG', optimize=True)
    buffer.seek(0)
    return ImageReader(buffer)


TOP_GRADIENT = soft_gradient()


def gradient_rule(x, y, width):
    colors = [(0.91, 0.62, 0.73), (0.75, 0.68, 0.91), (0.48, 0.68, 0.87)]
    steps = 72
    c.setLineWidth(2.2)
    for i in range(steps):
        t = i / max(1, steps - 1)
        if t <= .5:
            a, b, q = colors[0], colors[1], t * 2
        else:
            a, b, q = colors[1], colors[2], (t - .5) * 2
        rgb = tuple(a[j] + (b[j] - a[j]) * q for j in range(3))
        c.setStrokeColorRGB(*rgb)
        xa = x + width * i / steps
        xb = x + width * (i + 1) / steps + .2
        c.line(xa, y, xb, y)


def p(text, x, y, width=507, style='body'):
    item = Paragraph(text, styles[style])
    _, height = item.wrap(width, H)
    item.drawOn(c, x, y - height)
    return y - height


def page(number):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.drawImage(TOP_GRADIENT, 0, H - 235, W, 235, mask='auto')
    c.setStrokeColor(LINE)
    c.setLineWidth(.7)
    c.line(44, 42, 551, 42)
    c.setFillColor(MUTED)
    c.setFont('Body', 7.5)
    c.drawString(44, 26, 'Диана Тхайцухова / Резюме')
    c.drawRightString(551, 26, f'{number} / 2')


def section(title, y):
    c.setStrokeColor(LINE)
    c.line(44, y + 8, 551, y + 8)
    c.setFillColor(ORANGE)
    c.circle(48, y - 1, 2.6, fill=1, stroke=0)
    return p(title.upper(), 59, y + 4, 492, 'head') - 12


def link(text, url, x, y, width, style='body'):
    return p(f'<link href="{url}" color="#30221f">{text}</link>', x, y, width, style)


page(1)
p('РЕЗЮМЕ / 2026', 44, 801, style='label')
c.setFillColor(INK)
c.setFont('Display', 22.5)
c.drawString(44, 761, 'Диана')
c.drawString(44, 730, 'Тхайцухова.')
gradient_rule(44, 716, 325)
p('Графический дизайнер / Junior UX/UI', 44, 700, 330, 'head')
p('Айдентика  ·  визуальные системы  ·  цифровые макеты', 44, 678, 330, 'small')
p('Превращаю сложную идею в понятную визуальную систему. Сильна в айдентике, типографике, упаковке и подготовке макетов; умею доводить решение от концепции до цифрового или печатного носителя.', 44, 653, 330, 'body')

c.setFillColor(BLUE)
c.roundRect(402, 625, 149, 176, 12, fill=1, stroke=0)
c.saveState()
clip = c.beginPath()
clip.roundRect(409, 632, 135, 162, 9)
c.clipPath(clip, stroke=0, fill=0)
c.drawImage(compact_image(R / 'assets/img/about/diana-resume.jpg', 600, 88), 409, 632, 135, 162, mask='auto')
c.restoreState()
c.setFillColor(PINK)
c.circle(407, 793, 11, fill=1, stroke=0)

c.setFillColor(BLUE)
c.roundRect(44, 493, 507, 108, 10, fill=1, stroke=0)
p('<b>КОНТАКТЫ И ПОРТФОЛИО · САНКТ-ПЕТЕРБУРГ / УДАЛЁННО</b>', 59, 582, 360, 'label')
link('<b>soulminori20-web.github.io</b>', 'https://soulminori20-web.github.io/', 59, 561, 355, 'body')
link('Telegram: @soulminori', 'https://t.me/soulminori', 59, 538, 170, 'small')
link('+7 951 385-70-17', 'tel:+79513857017', 232, 538, 145, 'small')
link('Soulminori2.0@gmail.com', 'mailto:Soulminori2.0@gmail.com', 59, 518, 318, 'small')
c.setFillColor(PAPER)
c.roundRect(439, 504, 91, 87, 7, fill=1, stroke=0)
c.drawImage(ImageReader(str(R / 'assets/img/decor/portfolio-qr.png')), 447, 512, 71, 71, preserveAspectRatio=True, mask='auto')
c.linkURL('https://soulminori20-web.github.io/', (439, 504, 530, 591), relative=0)
c.setFillColor(INK)
c.setFont('Bold', 5.8)
c.drawCentredString(484.5, 507, 'ОТКРЫТЬ ПОРТФОЛИО')

y = section('Опыт работы', 465)
jobs = [
    ('Сентябрь 2025 - май 2026', 'Художник-конструктор / АО НПК «Северная заря»',
     'Разрабатывала эскизы, визуальные концепции и рабочую документацию. Сопровождала решения до производства и согласовывала детали с инженерами и технологами.'),
    ('Июль 2025 - сейчас', 'Дизайнер-декоратор / проектная деятельность',
     'Развиваю визуальный стиль мастерской, проектирую упаковку, этикетки и материалы для соцсетей. Готовлю макеты к печати и продумываю оформление индивидуальных заказов.'),
    ('Апрель 2023 - сейчас', 'Графический дизайнер / фриланс',
     'Создаю айдентику, рекламу, упаковку, презентации и полиграфию. Веду проект от первой концепции до правок, адаптаций и аккуратно собранных файлов для передачи.'),
]
for period, title, body in jobs:
    c.setFillColor(ORANGE)
    c.roundRect(44, y - 12, 118, 16, 8, fill=1, stroke=0)
    c.setFillColor(PAPER)
    c.setFont('Bold', 6.5)
    c.drawCentredString(103, y - 7.2, period)
    y = p(f'<b>{title}</b>', 178, y + 1, 373, 'body') - 5
    y = p(body, 44, y, 507, 'small') - 13

y = section('Образование', y + 2)
y = p('<b>СПбГУПТД</b> - «Искусственный интеллект в информационных системах», учусь сейчас, планируемое окончание - 2028.', 44, y, 507, 'small') - 7
y = p('<b>КТМУ СПбГУПТД</b> - «Дизайн по отраслям / промышленный дизайн», среднее профессиональное образование, 2025.', 44, y, 507, 'small')
assert y > 48, y
c.showPage()

page(2)
p('ПРОФЕССИОНАЛЬНЫЙ ФОКУС / ПРОЕКТЫ', 44, 801, style='label')
c.setFillColor(INK)
c.setFont('Display', 19)
c.drawString(44, 763, 'Дизайн, который помогает')
c.drawString(44, 737, 'понять главное.')
gradient_rule(44, 723, 507)
y = p('Мне интересны продукты, где человеку нужно быстро сориентироваться в сложной информации. Мои сильные стороны - визуальная иерархия, системность, аккуратные адаптации и понятная передача макетов команде. Интерфейсное направление развиваю в Figma и учебных проектах.', 44, 704, 507, 'body') - 18

y = section('Навыки', y)
cards = [
    ('ВИЗУАЛЬНАЯ СИСТЕМА', 'Айдентика, упаковка, типографика, композиция, многостраничная вёрстка, цифровые макеты, прототипы и подготовка к печати.'),
    ('ИНСТРУМЕНТЫ', 'Figma, Illustrator, Photoshop, InDesign, PowerPoint и AI-инструменты для поиска, развития и проверки идей.'),
    ('РАБОТА В КОМАНДЕ', 'Аргументирую решения, спокойно работаю с обратной связью, соблюдаю сроки, поддерживаю порядок в файлах и учитываю производство.'),
]
for i, (title, body) in enumerate(cards):
    x = 44 + i * 171
    c.setFillColor([BLUE, PINK, HexColor('#e7ddd3')][i])
    c.roundRect(x, y - 106, 157, 106, 9, fill=1, stroke=0)
    p(f'<b>{title}</b>', x + 12, y - 14, 133, 'label')
    p(body, x + 12, y - 38, 133, 'card')
y -= 135

y = section('Избранные проекты', y)
data = json.loads((R / 'tools/projects.json').read_text(encoding='utf-8'))
top = y
project_focus = {
    'govori': 'Визуальная система и адаптации',
    'buro': 'Навигация и путь посетителя',
    'language': 'Иерархия сложной информации',
    'calmes': 'Айдентика и упаковочная система',
}
for i, (slug, item) in enumerate(data.items()):
    x = 44 + (i % 2) * 272
    row = top - (i // 2) * 148
    frame_y = row - 78
    c.setFillColor(HexColor(item['accent']))
    c.roundRect(x, frame_y, 235, 78, 7, fill=1, stroke=0)
    c.saveState()
    clip = c.beginPath()
    clip.roundRect(x, frame_y, 235, 78, 7)
    c.clipPath(clip, stroke=0, fill=0)
    c.drawImage(compact_image(R / 'assets/img/projects' / slug / item['cover'], 900), x, frame_y, 235, 78, preserveAspectRatio=True, anchor='c', mask='auto')
    c.restoreState()
    p(f'<link href="https://soulminori20-web.github.io/projects/{slug}.html" color="#30221f"><b>{item["title"]}</b></link>', x, row - 88, 235, 'small')
    p(project_focus[slug], x, row - 106, 235, 'small')

y = top - 297
c.setFillColor(BLUE)
c.roundRect(44, y - 64, 507, 64, 9, fill=1, stroke=0)
p('<b>РЕАЛИЗОВАННЫЕ ПРОЕКТЫ</b>', 58, y - 14, 479, 'label')
p('GASTRO PORT и «Северная заря». Также развиваю авторскую мастерскую «Хуторок»: визуальный стиль, мастер-классы, изделия и 3D-печать.', 58, y - 35, 479, 'card')
y -= 78
p('<b>Языки:</b> русский - родной, английский - B1.', 44, y, 300, 'small')
link('Открыть портфолио', 'https://soulminori20-web.github.io/', 393, y, 158, 'small')
assert y > 48, y
c.showPage()
c.save()
print(f'Two-page resume created: {OUT}')
