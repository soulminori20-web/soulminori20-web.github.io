"""Build a portable static portfolio from the supplied artwork. No external dependencies at runtime."""
from pathlib import Path
import json, html, re
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
E = html.escape
ORIGINAL = json.loads((ROOT/'tools/original-projects.json').read_text())
DATA = {
 'govori': {
  'title':'ГОВОРИ', 'category':'Айдентика · коммуникационный дизайн',
  'short':'Образ речи в логотипе, иллюстрациях и оформлении образовательного проекта.',
  'lead':'Айдентика образовательного проекта о речи и уверенном общении.',
  'cover':'01-event.webp', 'hero':'02-key-visual.webp', 'accent':'#eea395',
  'task':'Передать энергию живого общения и объединить разные форматы: афиши, печатные материалы, одежду и оформление события.',
  'idea':'Профиль говорящего человека стал основой знака. Речевые облака, красные акценты и рисованная графика продолжают тему диалога на носителях.',
  'scope':'Логотип, фирменная графика, иллюстрации, афиши, полиграфия и мерч.',
  'decisions':[
   ['Образ речи','Профиль встроен в название, а речевое облако используется как самостоятельный элемент. Это связывает логотип с темой проекта.'],
   ['Контраст и интонация','Чёрный и белый образуют основу. Красный выделяет акценты, а рукописные штрихи добавляют графике эмоциональность.'],
   ['Разные форматы','На афишах графика задаёт композицию, в буклетах уступает место тексту, на одежде становится главным изображением.']],
  'outcome':'Собрана учебная айдентика и серия носителей. Визуализации показывают предполагаемое оформление события и применение графики.',
  'omit':[],
  'captions':{
   '02-key-visual.webp':'Профиль, речевое облако и рисованная графика — основные элементы айдентики.',
   '01-event.webp':'Вариант применения айдентики в образовательной среде.',
   '03-logo-system.webp':'Композиция логотипа и набор графических элементов.',
   '04-merch.webp':'Применение фирменной графики на одежде.',
   '05-event-space.webp':'Визуализация плакатов и оформления пространства.',
   '06-system-set.webp':'Общий набор носителей: печатные материалы, одежда и сувенирная продукция.',
   '07-badges.webp':'Варианты бейджей и материалов для участников.',
   '08-print.webp':'Перенос выразительной графики в информационные материалы.'}},
 'buro': {
  'title':'Потерянное бюро', 'category':'Айдентика · навигация · среда',
  'short':'Визуальный язык городского арт-проекта об историях, чувствах и воспоминаниях.',
  'lead':'Концепция городского арт-проекта, который собирает истории о нематериальных потерях.',
  'cover':'01-archive-card.webp', 'hero':'03-system-set.webp', 'accent':'#9ec9c4',
  'task':'Придать осязаемую форму воспоминаниям и чувствам. Связать идею общего архива с карточками, маршрутом и точкой взаимодействия в городе.',
  'idea':'Архивная карточка, номер дела и печать превращают личную историю в экспонат. Линии маршрутов и координаты связывают бумажные носители с городской средой.',
  'scope':'Логотип, печати, карточки, карты, полиграфия, концепция навигации и оформления бюро.',
  'decisions':[
   ['Архив как метафора','Нумерация, карточки и печати задают характер вымышленного бюро. В центре проекта — истории людей, а не поиск физических вещей.'],
   ['Маршрут как действие','Карта и указатели связывают точку бюро с городом. Звезда, ключ и маршрутная линия образуют набор повторяемых символов.'],
   ['Цвет и материал','Бордовый, бирюзовый и светлая бумага сочетают архивную строгость с более личной интонацией.']],
  'outcome':'Разработана учебная концепция айдентики, печатных носителей и городской среды. Изображения бюро показывают проектное предложение.',
  'omit':[],
  'captions':{
   '01-archive-card.webp':'Архивная карточка, конверт и печать задают характер проекта.',
   '02-kiosk-route.webp':'Концепция городской точки бюро и маршрутного указателя.',
   '07-kiosk.webp':'Визуализация взаимодействия посетителя с бюро.',
   '04-logo-system.webp':'Монограмма, дополнительные символы и варианты логотипа.',
   '03-system-set.webp':'Айдентика, полиграфия и среда в одной визуальной концепции.',
   '05-route-desk.webp':'Карта и материалы предполагаемого участника.',
   '06-stationery.webp':'Карточки, папки, конверты и бирки.',
   '08-wayfinding.webp':'Варианты указателей для навигации.',
   '09-wishes.webp':'Концепция объекта для сбора историй.',
   '10-stories.webp':'Оформление истории внутри общего архива.'}},
 'language': {
  'title':'Язык взаимопонимания', 'category':'Редакционный дизайн · иллюстрация',
  'short':'Книга о коммуникации и дневник снов, объединённые графикой и типографикой.',
  'lead':'Учебный редакционный проект: книга об общении и дневник для личных наблюдений.',
  'cover':'01-set.webp', 'hero':'10-complete-set.webp', 'accent':'#c5b9dc',
  'task':'Выстроить иерархию в книге о коммуникации и связать её с более личным форматом дневника. Сохранить узнаваемый характер двух изданий.',
  'idea':'Основная книга посвящена пониманию других людей, дневник — наблюдению за собственным опытом. Чёрно-белая пластичная графика объединяет серию, а цветовые акценты разделяют информационные уровни.',
  'scope':'Концепция серии, обложки, иллюстрации, оформление разворотов и страниц для записей.',
  'decisions':[
   ['Два формата','Книга организует материал о коммуникации. Дневник меняет способ взаимодействия: читатель заполняет страницы сам.'],
   ['Графический ритм','Иллюстрации, светлые и тёмные поля чередуются с текстом. Розовый и голубой используются для отдельных акцентов.'],
   ['Функциональная страница','Разлиновка и поля для записей поддерживают назначение дневника. Графика остаётся частью серии, но занимает меньше места.']],
  'outcome':'Собраны обложки, иллюстративное оформление и примеры внутренних страниц двух изданий. Проект представлен в учебном формате.',
  'omit':['05-interview.webp','06-empathy.webp'],
  'captions':{
   '01-set.webp':'Основная книга и дневник как два формата одной серии.',
   '02-cover.webp':'Обложка основной книги.',
   '03-detail.webp':'Деталь иллюстративного оформления.',
   '04-emotions.webp':'Тёмный разворот как отдельный композиционный акцент.',
   '07-dream-diary.webp':'Обложка дневника снов.',
   '08-binding.webp':'Визуализация переплёта дневника.',
   '09-diary-spread.webp':'Страницы для записей и наблюдений.',
   '10-complete-set.webp':'Книга, дневник и дополнительные материалы серии.'}},
 'calmes': {
  'title':'CALMES', 'category':'Айдентика · упаковка',
  'short':'Растительный знак, цвет и паттерн в оформлении ресторанной упаковки.',
  'lead':'Учебная айдентика ресторана итальянской кухни с акцентом на упаковку.',
  'cover':'03-packaging.webp', 'hero':'03-packaging.webp', 'accent':'#b8cbb7',
  'task':'Объединить оформление пакетов, коробок, винной этикетки и полиграфии. Сохранить узнаваемость на поверхностях разной формы и размера.',
  'idea':'Знак соединяет растительную форму с винным акцентом. Зелёный, винный и молочный цвета поддерживают гастрономическую тему, а паттерн связывает разные носители.',
  'scope':'Логотип, палитра, фирменный паттерн, этикетка, упаковка и полиграфия.',
  'decisions':[
   ['Знак и цвет','Растительная пластика и винный акцент формируют базовый образ. Светлые поля оставляют пространство вокруг знака.'],
   ['Паттерн','Повторяющаяся графика используется на больших поверхностях и внутренних частях упаковки. Масштаб паттерна меняется в зависимости от носителя.'],
   ['Серия носителей','Пакет, коробка и этикетка связаны цветом и графикой. На каждом формате выбирается свой баланс между знаком, паттерном и свободным полем.']],
  'outcome':'Разработана учебная концепция айдентики и оформления упаковки. Показаны варианты применения на разных носителях.',
  'omit':['01-set.webp','02-lifestyle.webp','05-structure.webp','06-logo-system.webp'],
  'captions':{
   '03-packaging.webp':'Варианты оформления пакетов, коробок, этикетки и печатных материалов.',
   '04-detail.webp':'Крупный план знака и паттерна на упаковке.',
   '07-visual-language.webp':'Палитра, типографика и принцип повторения фирменной графики.'}}
}

def img(path, alt, cls='', eager=False, zoom=False):
    file = ROOT/path
    with Image.open(file) as im: w,h=im.size
    loading = 'eager' if eager else 'lazy'
    attrs = f'class="{cls}" width="{w}" height="{h}" loading="{loading}" decoding="async"'
    if eager: attrs+=' fetchpriority="high"'
    responsive = ROOT/'assets/img/responsive'/path.removeprefix('assets/img/').replace('/','--')
    if responsive.exists():
        with Image.open(responsive) as thumbnail: responsive_width = thumbnail.width
        attrs += f' srcset="{PREFIX}assets/img/responsive/{responsive.name} {responsive_width}w, {PREFIX}{path} {w}w" sizes="(max-width: 740px) calc(100vw - 40px), (max-width: 1100px) 90vw, 1300px"'
    image=f'<img src="{PREFIX}{path}" alt="{E(alt)}" {attrs}>'
    if zoom:
        return f'<a class="zoom-link" href="{PREFIX}{path}" data-zoom data-caption="{E(alt)}" aria-label="Увеличить: {E(alt)}">{image}<span class="zoom-label" aria-hidden="true">Увеличить <span>↗</span></span></a>'
    return image

def head(title,desc):
 return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#101112">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta property="og:type" content="website"><meta property="og:locale" content="ru_RU"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta name="twitter:card" content="summary">
<link rel="icon" href="{PREFIX}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{PREFIX}assets/css/styles.css"><script src="{PREFIX}assets/js/main.js" defer></script></head>'''

def header(home=False):
 base='' if home else PREFIX+'index.html'
 return f'''<a class="skip-link" href="#main">К содержанию</a><header class="site-header"><div class="shell header-inner"><a class="brand" href="{base}#home" aria-label="Диана Тхайцухова — главная"><span class="brand-mark" aria-hidden="true">ДТ<span>✳</span></span><span>Диана<br>Тхайцухова</span></a><nav aria-label="Основная навигация"><a href="{base}#projects">Проекты</a><a href="{base}#workshop">Мастерская</a><a href="{base}#about">Обо мне</a></nav><a class="header-contact" href="{base}#contact">Связаться <span aria-hidden="true">↗</span></a></div></header>'''

def footer():
 return f'''<footer class="shell footer"><p>© 2026 Диана Тхайцухова</p><a href="{PREFIX}index.html#projects">Графический дизайн</a><a href="#top">Наверх ↑</a></footer><div class="toast" role="status" aria-live="polite"></div>
<dialog class="lightbox" aria-labelledby="lightbox-caption"><div class="lightbox-toolbar"><p id="lightbox-caption"></p><div class="lightbox-controls"><button type="button" data-image-prev aria-label="Предыдущее изображение">←</button><button type="button" data-image-next aria-label="Следующее изображение">→</button><button type="button" data-image-close aria-label="Закрыть изображение">✕</button></div></div><div class="lightbox-stage"><img alt=""></div><div class="lightbox-bottom"><span data-image-count></span><button type="button" data-image-size aria-pressed="false">Исходный размер</button><a href="#" data-image-open target="_blank" rel="noopener">Открыть отдельно ↗</a></div></dialog></body></html>'''

def contact():
 return '''<section class="contact section" id="contact" aria-labelledby="contact-title"><div class="shell contact-grid"><div><p class="eyebrow">05 / Контакты</p><h2 id="contact-title">Обсудим работу<br><em>в вашей команде.</em></h2><p class="lead">Рассматриваю предложения о работе в графическом дизайне и UX/UI. Напишите о роли и задачах — обсудим, чем я могу быть полезна.</p></div><div class="contact-links"><a href="https://t.me/soulminori" target="_blank" rel="noopener"><span>Telegram</span><strong>@soulminori</strong><span aria-hidden="true">↗</span></a><a href="mailto:Soulminori2.0@gmail.com"><span>Почта</span><strong>Soulminori2.0@gmail.com</strong><span aria-hidden="true">↗</span></a><button class="copy-email" type="button" data-copy-email>Скопировать почту <span aria-hidden="true">⧉</span></button><a class="profile-download" href="assets/docs/diana-designer-profile.pdf" download><span>Для знакомства</span><strong>Скачать профиль · PDF</strong><span aria-hidden="true">↓</span></a><div class="social-links"><a href="https://vk.ru/soulmi_nori" target="_blank" rel="noopener">VK ↗</a><a href="https://www.instagram.com/soulmi_nori/" target="_blank" rel="noopener">Instagram ↗</a></div></div></div></section>'''

def home():
 global PREFIX
 PREFIX=''
 cards=[]
 for i,(key,d) in enumerate(DATA.items(),1):
  cards.append(f'''<article class="project-card" id="project-{key}"><a class="project-cover" href="projects/{key}.html">{img('assets/img/projects/'+key+'/'+d['cover'],d['title']+' — '+d['short'],eager=False)}<span class="cover-action" aria-hidden="true">Смотреть проект ↗</span></a><div class="project-meta"><span>{i:02d} / {E(d['category'])}</span><span class="status">Учебный проект</span></div><h3><a href="projects/{key}.html">{E(d['title'])}<span aria-hidden="true">↗</span></a></h3><p>{E(d['short'])}</p></article>''')
 others=[('severnaya-zarya','Северная заря','Реализованный проект'),('gastro-port','GASTRO PORT','Реализованный проект'),('nordax','NORDAX','Учебный проект'),('atlas-tishiny','Атлас тишины','Учебный проект'),('cherta','Черта','Учебный проект')]
 otherhtml=''.join(f'''<article class="other-card">{img('assets/img/projects/other/'+key+'.webp',name,zoom=True)}<div><h4>{name}</h4><span class="status {'real' if status.startswith('Реал') else ''}">{status}</span></div></article>''' for key,name,status in others)
 return head('Диана Тхайцухова — графический дизайнер','Айдентика, упаковка, полиграфия и редакционный дизайн. Проекты Дианы Тхайцуховой, навыки и контакты.')+f'''<body id="top">{header(True)}<main id="main">
<section class="hero shell" id="home" aria-labelledby="hero-title"><div class="hero-copy"><p class="eyebrow">Портфолио / Графический дизайн</p><h1 id="hero-title">Диана<br>Тхайцухова<span class="gold-dot">.</span></h1><p class="hero-role">Айдентика, упаковка<br>и полиграфия.</p><p class="hero-intro">Разрабатываю визуальный образ бренда и переношу его на печатные и цифровые носители.</p><div class="actions"><a class="button primary" href="#projects">Смотреть проекты <span aria-hidden="true">↗</span></a><a class="text-link" href="assets/docs/diana-designer-profile.pdf" download>Профиль · PDF ↓</a></div><p class="availability"><span aria-hidden="true"></span>Открыта к предложениям о работе</p></div><div class="hero-art"><div class="hero-orbit" aria-hidden="true"></div>{img('assets/img/mascot-diana.webp','Стилизованный портрет Дианы Тхайцуховой','mascot',True)}<span class="art-caption">Форма. Характер. Детали.</span></div><div class="hero-bottom"><span>Айдентика</span><span>Упаковка</span><span>Редакционный дизайн</span><span>Визуальные коммуникации</span></div></section>
<section class="section shell" id="projects" aria-labelledby="projects-title"><div class="section-head"><div><p class="eyebrow">02 / Проекты</p><h2 id="projects-title">Избранные <em>работы.</em></h2></div><p>Четыре учебных проекта:<br>от логотипа до серии носителей.</p></div><div class="project-grid">{''.join(cards)}</div><div class="other-projects"><div class="subsection-head"><h3>Другие проекты</h3><p>Реализованные и учебные работы</p></div><div class="other-grid">{otherhtml}</div></div></section>
<section class="workshop section shell" id="workshop" aria-labelledby="workshop-title"><div class="workshop-panel"><div><p class="eyebrow">03 / Авторская практика</p><h2 id="workshop-title">Хуторок</h2><p class="lead">Моя творческая мастерская: ручная работа, предметный дизайн и 3D-печать.</p><p>Работа с материалами дополняет мою графическую практику. Здесь идеи приобретают форму предметов — от свечей и декора до подарочных наборов.</p><a class="button" href="workshop.html">Открыть мастерскую <span aria-hidden="true">↗</span></a></div><a href="workshop.html" class="workshop-image" aria-label="Открыть мастерскую Хуторок">{img('assets/img/workshop/brand-banner.webp','Фирменное оформление творческой мастерской Хуторок')}</a></div></section>
<section class="about section shell" id="about" aria-labelledby="about-title"><div class="section-head"><div><p class="eyebrow">04 / Обо мне</p><h2 id="about-title">От идеи<br><em>до носителя.</em></h2></div><p>Графический дизайн<br>и внимание к реализации</p></div><div class="about-main"><div class="about-copy"><p class="lead">Я графический дизайнер. Работаю с айдентикой, упаковкой, полиграфией и редакционными проектами.</p><p>Мне интересен весь путь: разобраться в задаче, найти визуальную идею, выстроить композицию и подготовить материалы для использования. В портфолио представлены реализованные и учебные работы.</p><p>Объясняю решения через задачу, аудиторию и ограничения. Обсуждаю обратную связь и дорабатываю результат вместе с командой.</p><div class="role-note"><span class="eyebrow">Что ищу</span><p>Работу графическим дизайнером или UX/UI-дизайнером. Основная специализация представленных здесь проектов — графический дизайн.</p></div></div><figure class="portrait">{img('assets/img/about/diana-portrait.webp','Диана Тхайцухова')}<figcaption>Диана Тхайцухова / дизайнер</figcaption></figure></div>
<div class="profile-grid"><section class="profile-block"><h3>Инструменты</h3><dl class="tools"><div><dt>Illustrator</dt><dd>Логотипы, векторная графика, макеты носителей</dd></div><div><dt>Photoshop</dt><dd>Изображения, ретушь и презентационные композиции</dd></div><div><dt>InDesign</dt><dd>Книги, многостраничная вёрстка и печать</dd></div><div><dt>Figma</dt><dd>Цифровые макеты, презентации и прототипы</dd></div><div><dt>PowerPoint</dt><dd>Оформление презентаций</dd></div></dl><p class="secondary">Также использую AI-инструменты для поиска идей и работы с изображениями. В авторской практике работаю с формой и 3D-печатью.</p></section><section class="profile-block"><h3>Образование</h3><div class="education-item"><h4>Дизайн</h4><p>КТМУ · профильное образование</p></div><div class="education-item"><h4>Искусственный интеллект<br>в информационных системах</h4><p>ВШТЭ · технологическое направление</p></div><div class="production-note"><h4>Подготовка материалов</h4><p>Учитываю формат, цветовую модель, вылеты, безопасные зоны и требования к передаче файлов.</p></div></section></div>
<section class="process" aria-labelledby="process-title"><h3 id="process-title">Как я работаю</h3><ol><li><span>01</span><h4>Разбираюсь в задаче</h4><p>Аудитория, контекст, сроки и ограничения.</p></li><li><span>02</span><h4>Предлагаю направление</h4><p>Идея, референсы и аргументы в пользу решения.</p></li><li><span>03</span><h4>Разрабатываю дизайн</h4><p>Графика, типографика и адаптация к носителям.</p></li><li><span>04</span><h4>Готовлю к передаче</h4><p>Проверка макетов и организация файлов.</p></li></ol></section></section>
{contact()}</main>'''+footer()

def case(key,index):
 global PREFIX
 PREFIX='../'
 d=DATA[key]; old=ORIGINAL[key];path='assets/img/projects/'+key+'/'
 gallery=[];n=0
 for src,label,span,fit,note in old['images']:
  name=Path(src).name
  if name in d['omit'] or name==d['hero']:continue
  n+=1
  caption=d['captions'].get(name,label)
  gallery.append(f'<figure class="case-figure {"wide" if span==12 else ""}">{img(src,caption,zoom=True)}<figcaption><span>{n:02d}</span>{E(caption)}</figcaption></figure>')
 decisions=''.join(f'<article><span class="eyebrow">0{i}</span><h3>{E(t)}</h3><p>{E(p)}</p></article>' for i,(t,p) in enumerate(d['decisions'],1))
 keys=list(DATA);nextkey=keys[(index+1)%len(keys)];nd=DATA[nextkey]
 return head(d['title']+' — Диана Тхайцухова',d['lead'])+f'''<body id="top" class="case-page" style="--case-accent:{d['accent']}">{header()}<main id="main"><div class="shell case-breadcrumb"><a href="../index.html#project-{key}">← Все проекты</a><span>{index+1:02d} / 04</span></div><section class="shell case-intro"><div><p class="eyebrow">{E(d['category'])}</p><h1>{E(d['title'])}</h1></div><div><span class="status">Учебный проект</span><p class="lead">{E(d['lead'])}</p><button type="button" class="text-link copy-case" data-copy-link>Скопировать ссылку ↗</button></div></section><figure class="shell case-hero">{img(path+d['hero'],d['title']+' — визуальная концепция',eager=True,zoom=True)}</figure>
<nav class="shell case-nav" aria-label="Разделы проекта"><a href="#brief">Задача</a><a href="#decisions">Решения</a><a href="#gallery">Материалы</a><a href="#result">Итог</a></nav>
<section class="shell case-brief" id="brief"><div><p class="eyebrow">Контекст</p><h2>Задача и идея</h2></div><div class="brief-content"><div><h3>Задача</h3><p>{E(d['task'])}</p></div><div><h3>Визуальная идея</h3><p>{E(d['idea'])}</p></div><div><h3>Состав проекта</h3><p>{E(d['scope'])}</p></div></div></section>
<section class="shell case-decisions" id="decisions" aria-labelledby="decisions-title"><h2 id="decisions-title">Ключевые решения</h2><div>{decisions}</div></section>
<section class="shell case-gallery-section" id="gallery" aria-labelledby="gallery-title"><div class="subsection-head"><h2 id="gallery-title">Материалы проекта</h2><p>Макеты и визуализации</p></div><div class="case-gallery">{''.join(gallery)}</div></section>
<section class="shell case-result" id="result"><p class="eyebrow">Итог</p><p class="lead">{E(d['outcome'])}</p><a class="text-link" href="../index.html#contact">Обсудить работу в команде ↗</a></section>
<nav class="shell next-project" aria-label="Следующий проект"><a href="{nextkey}.html"><span class="eyebrow">Следующий проект / {(index+1)%4+1:02d}</span><strong>{E(nd['title'])}</strong><span class="next-arrow" aria-hidden="true">↗</span></a></nav></main>'''+footer()

def workshop():
 global PREFIX
 PREFIX=''
 # Preserve the complete collection and commercial capabilities in a separate, quieter page.
 handmade=[('handmade-07-pink-set.webp','Свечи и подарочные наборы'),('handmade-08-shell-candles.webp','Свечи в форме ракушек'),('handmade-01-leaf-trays.webp','Расписные подносы'),('handmade-10-cat-coasters.webp','Подставки с росписью'),('handmade-05-mountain-painting.webp','Текстурная картина'),('handmade-04-flower-painting.webp','Интерьерная работа'),('handmade-06-marbled-coasters.webp','Мраморные подставки'),('handmade-09-sunflower-set.webp','Набор с подсолнухами'),('handmade-11-sea-heart.webp','Морская композиция'),('handmade-02-blue-set.webp','Голубой набор'),('handmade-03-painted-trays.webp','Декоративные тарелки')]
 gallery=''.join(f'<figure>{img("assets/img/workshop/"+f,label,zoom=True)}<figcaption>{label}</figcaption></figure>' for f,label in handmade)
 carousel=''.join(f'<figure>{img("assets/img/workshop/"+name,label,zoom=True)}</figure>' for name,label in [('carousel-01-cover.webp','Хуторок — обложка'),('carousel-02-about.webp','О мастерской'),('carousel-03-masterclasses.webp','Мастер-классы'),('carousel-04-handmade.webp','Изделия ручной работы'),('carousel-05-values.webp','Ценности мастерской'),('carousel-06-cta.webp','Приглашение в мастерскую')])
 samples=''.join(f'<figure>{img("assets/img/workshop/"+f,label,zoom=True)}<figcaption>{label}</figcaption></figure>' for f,label in [('print-01-lamp.webp','Светильник'),('print-02-organizer.webp','Органайзер'),('print-03-bag.webp','Декоративный объект')])
 return head('Хуторок — творческая мастерская Дианы','Авторская практика Дианы Тхайцуховой: свечи, декор, роспись, предметы и 3D-печать.')+f'''<body id="top" class="workshop-page">{header()}<main id="main"><div class="shell case-breadcrumb"><a href="index.html#workshop">← К портфолио</a><span>Авторская практика</span></div><section class="shell workshop-intro"><div><p class="eyebrow">Творческая мастерская</p><h1>Хуторок<span>.</span></h1><p class="lead">Место, где руки заняты,<br>а голова отдыхает.</p><p>Моя мастерская объединяет графический дизайн, работу с материалами и создание предметов: свечей, декора, картин и подарочных наборов.</p><a class="button primary" href="https://vk.ru/hutorokdesign" target="_blank" rel="noopener">Мастерская в VK ↗</a></div>{img('assets/img/workshop/brand-banner.webp','Хуторок — фирменное оформление',eager=True)}</section>
<section class="shell section"><div class="subsection-head"><h2>Визуальный образ</h2><div class="carousel-buttons"><button type="button" data-carousel-prev aria-label="Предыдущий слайд">←</button><button type="button" data-carousel-next aria-label="Следующий слайд">→</button></div></div><div class="carousel" tabindex="0" role="region" aria-label="Оформление мастерской; прокрутите для просмотра">{carousel}</div></section>
<section class="shell section"><div class="section-head"><div><p class="eyebrow">Работа с материалами</p><h2>Форма и <em>фактура.</em></h2></div><p>Свечи, декор и роспись</p></div><div class="handmade-grid">{gallery}</div></section>
<section class="shell section workshop-details"><h2>В мастерской</h2><details open><summary>Изделия и индивидуальные заказы</summary><div><p>Свечи, подносы, подставки, интерьерные картины и подарочные наборы. Цвет, оформление и состав набора можно обсудить под конкретный интерьер или повод.</p><p>Доступность готовых изделий, стоимость и сроки — в сообщениях мастерской.</p></div></details><details><summary>Мастер-классы</summary><div><p>Свечи, декоративные предметы и текстурные картины. Можно прийти без опыта: материалы предоставляются, а этапы работы разбираются вместе.</p><a class="text-link" href="https://vk.ru/hutorokdesign" target="_blank" rel="noopener">Узнать о занятиях ↗</a></div></details><details><summary>Подход к работе</summary><div><p>Ручной труд, внимание к материалу и возможность пробовать новое. Небольшие различия в фактуре и росписи сохраняют характер каждой вещи.</p></div></details></section>
<section class="shell section"><div class="section-head"><div><p class="eyebrow">3D-печать</p><h2>От модели<br><em>к предмету.</em></h2></div><p>Декор, прототипы и детали</p></div><p class="lead narrow">Форму, размеры и материал подбираем под задачу. Ниже — примеры предметов; возможность изготовления обсуждается индивидуально.</p><div class="samples-grid">{samples}</div><details><summary>Задачи и материалы</summary><div><p>Органайзеры, подставки, кашпо, сувениры, корпуса, крепления и прототипы. При выборе материала учитываются форма, нагрузка и условия использования предмета.</p><p>В мастерской используются Bambu Lab A1 и QIDI Q2. Технологию и параметры печати выбираем после обсуждения модели.</p></div></details><details><summary>Как проходит заказ</summary><div><ol class="order-steps"><li>Пришлите описание, эскиз, размеры или пример предмета.</li><li>Обсудим форму и условия использования.</li><li>Подберём или подготовим модель и материал.</li><li>Согласуем стоимость и сроки.</li><li>Изготовим и проверим предмет.</li></ol></div></details></section><section class="shell workshop-final"><p class="eyebrow">Хуторок дизайнера</p><h2>Приходите<br>творить вместе.</h2><p>Занятия, готовые изделия и индивидуальные заказы.</p><a class="button primary" href="https://vk.ru/hutorokdesign" target="_blank" rel="noopener">Написать в мастерскую ↗</a><a class="text-link" href="index.html#workshop">Вернуться к портфолио</a></section></main>'''+footer()

if __name__=='__main__':
 (ROOT/'projects').mkdir(exist_ok=True)
 (ROOT/'index.html').write_text(home())
 for i,key in enumerate(DATA): (ROOT/'projects'/f'{key}.html').write_text(case(key,i))
 (ROOT/'workshop.html').write_text(workshop())
 # Store only current editorial content; the old text is an input, never a published page.
 (ROOT/'tools/projects.json').write_text(json.dumps(DATA,ensure_ascii=False,indent=2))
 print('Built 6 static pages.')
