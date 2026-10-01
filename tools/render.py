"""Portfolio v38: tightened section rhythm, workshop link and verified resume."""
from pathlib import Path
import html
import json

from PIL import Image

R = Path(__file__).resolve().parents[1]
D = json.loads((R / "tools/projects.json").read_text(encoding="utf-8"))
O = json.loads((R / "tools/original-projects.json").read_text(encoding="utf-8"))
E = html.escape
P = ""


def img(path, alt="", cls="", eager=False, zoom=False):
    with Image.open(R / path) as im:
        width, height = im.size
    tag = (
        f'<img src="{P}{path}?v=38" alt="{E(alt)}" class="{cls}" '
        f'width="{width}" height="{height}" loading="{"eager" if eager else "lazy"}" '
        f'decoding="async"' + (' fetchpriority="high"' if eager else '') + '>'
    )
    if zoom:
        return (
            f'<a class="zoom" href="{P}{path}" data-zoom data-caption="{E(alt)}" '
            f'aria-label="Рассмотреть: {E(alt)}">{tag}'
            '<span class="zoom-label" aria-hidden="true">Рассмотреть ↗</span></a>'
        )
    return tag


def decor(name, cls=""):
    return f'<span class="decor-object {cls}" aria-hidden="true">{img("assets/img/decor/object-" + name + ".webp")}</span>'


def mascot(pose="urban-neutral", cls="", live=False):
    live_attr = " data-mascot" if live else ""
    return (
        f'<div class="mascot-scene {cls}" data-default-pose="{pose}"{live_attr}>'
        f'<div class="mascot-body">{img("assets/img/mascot/" + pose + ".webp", cls="mascot-image", eager=pose == "urban-neutral")}</div></div>'
    )


def btn(href, text, kind="solid", attrs=""):
    return f'<a class="button {kind}" href="{href}" {attrs}>{text}<span aria-hidden="true">↗</span></a>'


def head(title, desc):
    return (
        '<!doctype html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="theme-color" content="#f6f3ef">'
        f'<title>{E(title)}</title><meta name="description" content="{E(desc)}">'
        f'<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">'
        '<meta property="og:type" content="website"><meta property="og:locale" content="ru_RU">'
        f'<link rel="icon" href="{P}assets/favicon.svg">'
        f'<link rel="preload" href="{P}assets/fonts/manrope-regular.ttf" as="font" type="font/ttf" crossorigin>'
        f'<link rel="stylesheet" href="{P}assets/css/styles.css?v=38">'
        f'<script src="{P}assets/js/main.js?v=38" defer></script></head>'
    )


def header(home=False):
    base = "" if home else P + "index.html"
    return (
        '<a class="skip" href="#main">К содержанию</a><header class="site-header"><div class="wrap header-row">'
        f'<a class="brand" href="{base}#home" aria-label="Диана Тхайцухова — главная">soulminori<span aria-hidden="true">✳</span></a>'
        f'<nav aria-label="Основная навигация"><a href="{base}#projects">Проекты</a><a href="{base}#experience">Опыт</a><a href="{base}#about">Обо мне</a></nav>'
        f'<a class="header-contact" href="{base}#contact">Написать ↗</a>'
        '<button type="button" class="motion-toggle" aria-pressed="false" aria-label="Отключить анимацию" title="Отключить анимацию">Ⅱ</button>'
        '</div></header>'
    )


def footer():
    return (
        f'<footer class="wrap footer"><span>© 2026 · Диана Тхайцухова</span><a href="{P}index.html#projects">Графический дизайн · UX/UI</a><a href="#top">Наверх ↑</a></footer>'
        '<div class="toast" role="status" aria-live="polite"></div>'
        '<dialog class="lightbox" aria-labelledby="lightbox-caption"><div class="lightbox-bar"><p id="lightbox-caption"></p><button type="button" data-close aria-label="Закрыть изображение">✕</button></div>'
        '<div class="lightbox-stage"><img alt=""></div><div class="lightbox-bar"><button type="button" data-prev aria-label="Предыдущее изображение">←</button><span data-count></span>'
        '<a data-original href="#top" target="_blank" rel="noopener">Открыть оригинал ↗</a><button type="button" data-next aria-label="Следующее изображение">→</button></div></dialog></body></html>'
    )


def contacts():
    return (
        '<section class="contact noise-panel" id="contact"><div class="wrap contact-grid"><div>'
        '<p class="eyebrow">05 / На связи</p><h2>Открыта к работе<br><em>графическим или UX/UI-дизайнером.</em></h2>'
        '<p>Рассматриваю удалённую работу и комплексные проекты, где нужны айдентика, интерфейсы, упаковка, полиграфия или digital-материалы.</p>'
        '<p>Если вам нужен дизайнер, который умеет выстроить систему и подготовить её к реальному использованию, напишите мне.</p>'
        f'<div class="actions">{btn("https://t.me/soulminori", "Написать в Telegram", "light", "target=\"_blank\" rel=\"noopener\"")}'
        f'{btn("assets/docs/diana-tkhaytsukhova-resume.pdf", "Скачать резюме · PDF", "outline-light", "download")}</div></div>'
        '<div class="contact-addresses"><p class="contact-location">Санкт-Петербург · открыта к удалённой работе</p>'
        '<a href="tel:+79513857017"><span>Позвонить</span><strong>+7 951 385-70-17</strong></a>'
        '<a href="mailto:Soulminori2.0@gmail.com"><span>Написать на почту</span><strong>Soulminori2.0@gmail.com</strong></a>'
        '<button type="button" data-copy-email>Скопировать почту ⧉</button>'
        '<a href="https://t.me/soulminori" target="_blank" rel="noopener"><span>Telegram — отвечаю быстрее всего</span><strong>@soulminori</strong></a>'
        '<div class="socials"><a href="https://vk.ru/soulmi_nori" target="_blank" rel="noopener">VK ↗</a>'
        '<a href="https://www.instagram.com/soulmi_nori/" target="_blank" rel="noopener">Instagram ↗</a></div></div></div>'
        f'{decor("star", "contact-star")}</section>'
    )


ABOUT = [
    (
        "profile", "Кто я", "urban-wave", "Собираю сложные задачи<br>в <em>понятные системы.</em>",
        '<p class="lead">Я графический дизайнер с опытом в айдентике, UX/UI, упаковке, полиграфии, редакционном дизайне и производственных задачах.</p>'
        '<p>Сильнее всего работаю в комплексных проектах, где один визуальный принцип нужно последовательно перенести на интерфейс, печатные материалы, упаковку, digital-форматы или физическую среду.</p>'
        '<p>Мне интересны задачи, в которых от дизайнера требуется не только визуальная идея, но и работа с содержанием, ограничениями, подрядчиками и практической реализацией.</p>'
    ),
    (
        "practice", "Опыт", "urban-present", "Знаю путь<br>от ТЗ до <em>реализации.</em>",
        '<div class="experience-item"><p class="eyebrow">Июль 2025 — настоящее время</p><h4>Дизайнер-декоратор · проектная работа</h4><p>Развиваю визуальную систему мастерской и оформляю физические продукты: упаковку, этикетки, открытки, материалы для социальных сетей и индивидуальные заказы. Работаю с реальными размерами, сгибами, вырубкой, фактурами и особенностями печати.</p><p><strong>Результат:</strong> реализованы серии упаковки и сопроводительных материалов для готовых изделий и заказов.</p><p class="inline-links"><a href="#workshop">Перейти в мастерскую «Хуторок» →</a></p></div>'
        '<div class="experience-item"><p class="eyebrow">Апрель 2023 — настоящее время</p><h4>Графический дизайнер · фриланс</h4><p>Разрабатываю айдентику, упаковку, полиграфию, презентации и digital-материалы. Работаю с техническим заданием, предлагаю визуальное направление, собираю систему, адаптирую её к носителям и готовлю финальные файлы.</p><p><strong>Результат:</strong> реализованные проекты для гастрономии, образования, городской среды и B2B.</p><p class="inline-links"><a href="#project-govori">ГОВОРИ →</a> <a href="#project-buro">Потерянное бюро →</a> <a href="#project-calmes">CALMES →</a></p></div>'
        '<div class="experience-item" id="experience-severnaya"><p class="eyebrow">Сентябрь 2025 — май 2026</p><h4>Художник-конструктор · АО НПК «Северная заря»</h4><p>Разрабатывала эскизы, визуальные концепции и рабочую документацию для изделий. Сопровождала решения до передачи в производство, учитывала технические ограничения и дорабатывала материалы после проверок.</p><p>Согласовывала решения с инженерами и технологами, фиксировала изменения и подготавливала структурированные комплекты файлов для следующего производственного этапа.</p><p><strong>Результат:</strong> визуальные и рабочие материалы подготовлены к согласованию и производству с учётом требований смежных специалистов.</p><p class="inline-links"><a href="#other-severnaya-zarya">Смотреть проект →</a></p></div>'
    ),
    (
        "skills", "Что умею", "urban-work", "Собираю не кадр,<br>а <em>работающую систему.</em>",
        '<section class="skills-block"><p class="skills-label">Навыки</p><div class="skill-groups"><article><h4>Айдентика и брендинг</h4><p>Логотипы, знаки, key visual, палитры, типографика, фирменная графика и правила применения.</p></article>'
        '<article><h4>UX/UI и web</h4><p>Информационная архитектура, пользовательские сценарии, user flow, прототипы, компоненты и адаптивные макеты.</p></article>'
        '<article><h4>Полиграфия и editorial</h4><p>Каталоги, книги, буклеты, меню, POS-материалы и презентации; сетки, стили и предпечатная проверка.</p></article>'
        '<article><h4>Упаковка</h4><p>Этикетки, коробки, пакеты, развёртки, сгибы, безопасные поля и требования производства.</p></article>'
        '<article><h4>Digital и реклама</h4><p>Баннеры, социальные сети, рекламные форматы, инфографика и адаптация кампаний.</p></article>'
        '<article><h4>Производственные задачи</h4><p>Технические ограничения, рабочие материалы и согласование с инженерами, технологами и подрядчиками.</p></article></div></section>'
        '<section class="skills-block programs-block"><p class="skills-label">Программы и инструменты</p><div class="tool-grid"><span>Figma<small>Интерфейсы и прототипы</small></span><span>Illustrator<small>Логотипы, вектор, упаковка</small></span><span>InDesign<small>Каталоги и многостраничная верстка</small></span><span>Photoshop<small>Изображения и презентация макетов</small></span><span>Microsoft Office<small>Документы, таблицы, расчёты, презентации</small></span><span>CRM / CMS<small>Базы, контент и таск-трекеры</small></span><span>AI-инструменты<small>Варианты и ускорение рутины</small></span></div></section>'
    ),
    (
        "education", "Образование", "urban-think", "Дизайн встречается<br>с <em>технологиями.</em>",
        '<div class="education"><span>2028</span><div><h4>СПбГУПТД</h4><p>«Искусственный интеллект в информационных системах». Учусь сейчас, планируемое окончание — 2028 год.</p></div></div>'
        '<div class="education"><span>2025</span><div><h4>Колледж технологии, моделирования и управления СПбГУПТД</h4><p>«Дизайн по отраслям», направление промышленного дизайна. Среднее профессиональное образование.</p></div></div><p>Русский — родной. Английский — B1.</p>'
    ),
    (
        "process", "Как работаю", "urban-idea", "Быстро разбираюсь.<br>Строю систему. <em>Довожу до передачи.</em>",
        '<ol class="steps"><li><strong>Быстро разбираю техническое задание</strong><p>Выделяю цель, аудиторию, ограничения, сроки и критерии готовности.</p></li>'
        '<li><strong>Собираю сильную первую подачу</strong><p>Показываю цельное направление: структуру, визуальный принцип, типографику, цвет и примеры применения.</p></li>'
        '<li><strong>Работаю в быстрых сроках</strong><p>Сначала закрываю решения с наибольшим влиянием на результат, затем адаптации и детали.</p></li>'
        '<li><strong>Строю систему</strong><p>Настраиваю архитектуру, сетку, типографику, цвет, компоненты и технические параметры.</p></li>'
        '<li><strong>Спокойно работаю с правками</strong><p>Фиксирую изменения, уточняю цель и сохраняю целостность связанных макетов.</p></li>'
        '<li><strong>Довожу до передачи</strong><p>Проверяю размеры, стили, цветовые профили, вылеты, структуру файлов и версии.</p></li></ol>'
    ),
    (
        "team", "В команде", "urban-wave", "Говорю по делу<br>и спокойно отношусь к <em>правкам.</em>",
        '<p class="lead">Умею объяснять дизайн простыми словами, слышать обратную связь и не воспринимать обсуждение макета как спор о вкусах.</p><p>Внимательна к срокам, структуре файлов и договорённостям. Если вижу риск для результата, поднимаю вопрос заранее и предлагаю варианты.</p><h4>Что ищу сейчас</h4><p>Полную занятость графическим или UX/UI-дизайнером в команде, где ценят сильную визуальную идею, аккуратную реализацию и желание расти. Рассматриваю удалённую работу.</p>'
    ),
]


OTHER = [
    {
        "slug": "severnaya-zarya", "name": "Северная заря", "category": "Промышленный дизайн · выставочные каталоги · упаковка · производственная полиграфия",
        "task": "Обеспечивать визуальное и полиграфическое сопровождение инженерной компании: переводить технические задания, документацию и продуктовые данные в понятные каталоги, упаковку и материалы для выставочного и производственного использования.",
        "role": "Художник-конструктор; концепция и верстка каталогов, структурирование технического контента, разработка упаковки, подбор цветовых решений, предпечатная подготовка и взаимодействие с типографиями.",
        "made": "Изучала ТЗ и инженерную документацию; определяла структуру многостраничных каталогов; верстала каталоги для крупных отраслевых выставок; оформляла таблицы, схемы и продуктовые блоки; участвовала в разработке упаковки; готовила рабочие файлы и спецификации; напрямую работала с типографиями, цветопробами и тестовыми экземплярами.",
        "typography": "Разработала иерархию для разделов, наименований продукции, характеристик, таблиц, подписей и служебных данных. Настроила модульную сетку, стили абзацев и повторяемые шаблоны страниц. Контролировала читаемость мелких характеристик, плотность таблиц и воспроизведение фирменных цветов.",
        "programs": "Adobe InDesign, Adobe Illustrator, Adobe Photoshop, офисные приложения", "duration": "2–3 недели на каталог; 1–3 недели на отдельную производственную задачу",
        "result": "Выпущены многостраничные каталоги для крупных инженерных выставок, разработаны макеты упаковки и комплекты производственной полиграфии. Материалы прошли согласование, предпечатную проверку и передачу подрядчикам или техническим специалистам."
    },
    {
        "slug": "gastro-port", "name": "GASTRO PORT", "category": "Графический дизайн · полиграфия · digital · действующее пространство на Пхукете",
        "task": "Адаптировать визуальную систему действующего гастрономического пространства GASTRO PORT на Пхукете к печатным, рекламным и цифровым материалам, которые посетитель видит непосредственно в пространстве.",
        "role": "Дизайн и адаптация носителей, верстка, обработка изображений, подготовка файлов.",
        "made": "Меню, печатные материалы, рекламная графика, digital-форматы и набор адаптаций для разных размеров. GASTRO PORT находится на Пхукете, поэтому с результатом работы можно познакомиться не только в макетах, но и во время визита в пространство.",
        "typography": "Выстроила иерархию для категорий меню, наименований, описаний, состава и цен. Настроила размеры, интервалы и стили так, чтобы плотный контент оставался быстро просматриваемым.",
        "programs": "Adobe Illustrator, Adobe InDesign, Adobe Photoshop", "duration": "2–3 недели на основной комплект",
        "result": "Подготовлен и реализован набор офлайн- и digital-материалов; единые правила композиции и типографики позволяют быстро собирать новые форматы."
    },
    {
        "slug": "nordax", "name": "NORDAX", "category": "Айдентика · B2B · промышленный бренд",
        "task": "Создать строгую визуальную систему для промышленного бренда и обеспечить её работу на носителях разного масштаба.",
        "role": "Концепция, логотип, фирменная система, адаптация носителей.",
        "made": "Логотип, фирменный знак, палитра, типографика, документация, униформа, транспорт и производственные носители.",
        "typography": "Собрала сдержанную B2B-систему для технической и деловой коммуникации. Проверила набор в документах, маркировке и на крупных поверхностях, определила иерархию, минимальные размеры и интервалы.",
        "programs": "Adobe Illustrator, Adobe Photoshop", "duration": "3 недели",
        "result": "Айдентика реализована на документах, одежде, транспорте и крупных производственных поверхностях; подготовлены единые правила масштаба, отступов и размещения знака."
    },
    {
        "slug": "atlas-tishiny", "name": "Атлас тишины", "category": "Редакционный дизайн · многостраничная верстка · арт-дирекция",
        "task": "Собрать длинное визуальное повествование и объединить текст, фотографии и картографику в понятную систему.",
        "role": "Визуальная концепция, сетка, типографика, обработка изображений, верстка и подготовка к печати.",
        "made": "Обложка, модульная сетка, система заголовков, многостраничные развороты, фотографии, карты и дополнительные печатные материалы.",
        "typography": "Разработала иерархию для глав, основного текста, подписей, картографических пояснений, колонтитулов и пагинации. Настроила длину строки, интерлиньяж и чередование плотных и свободных разворотов.",
        "programs": "Adobe InDesign, Adobe Photoshop, Adobe Illustrator", "duration": "3–4 недели",
        "result": "Издание собрано и выпущено как единая редакционная система; повторяемые стили и сетка удерживают структуру при смене текста, фотографий и карт."
    },
    {
        "slug": "cherta", "name": "ЧЕРТА", "category": "Айдентика · упаковка · оформление пространства",
        "task": "Создать лаконичную айдентику, которая сохраняет характер на небольших печатных материалах, одежде, упаковке и в пространстве.",
        "role": "Концепция, логотип, фирменная графика, адаптация носителей.",
        "made": "Логотип, графический знак, фирменные элементы, упаковка, печатные материалы, одежда и оформление пространства.",
        "typography": "Построила систему на контроле масштаба, свободного поля и межбуквенных интервалов. Проверила минимальные кегли для небольших носителей и увеличенный масштаб для одежды и пространства.",
        "programs": "Adobe Illustrator, Adobe Photoshop", "duration": "2–3 недели",
        "result": "Визуальная система реализована на нескольких группах носителей; знак и композиционные правила сохраняют читаемость и узнаваемость в разных масштабах."
    },
]


def project_card(key, data, index):
    return (
        f'<article class="project-card" id="project-{key}" data-reveal><a class="project-cover" href="projects/{key}.html">'
        f'{img("assets/img/projects/" + key + "/" + data["cover"], data["title"] + " — " + data["short"])}<span class="cover-pill">Открыть кейс ↗</span></a>'
        f'<div class="project-meta"><span>{index:02d} / {E(data["category"])}</span></div><h3><a href="projects/{key}.html">{E(data["title"])}<span aria-hidden="true">↗</span></a></h3>'
        f'<p>{E(data["short"])}</p><dl class="project-facts"><div><dt>Роль</dt><dd>{E(data["role_short"])}</dd></div><div><dt>Срок</dt><dd>{E(data["duration"])}</dd></div><div><dt>Результат</dt><dd>{E(data["result_short"])}</dd></div></dl></article>'
    )


def other_card(data):
    return (
        f'<article class="other-card other-case" id="other-{data["slug"]}" data-reveal>'
        f'{img("assets/img/projects/other/" + data["slug"] + ".webp", data["name"] + " — " + data["category"], zoom=True)}'
        f'<div><h4>{E(data["name"])}</h4><span class="status real">Реализован</span></div><p class="other-category">{E(data["category"])}</p>'
        f'<details><summary>Задача, роль и результат <span aria-hidden="true">↘</span></summary><div class="other-case-body">'
        f'<h5>Задача</h5><p>{E(data["task"])}</p><h5>Моя роль</h5><p>{E(data["role"])}</p><h5>Что сделала</h5><p>{E(data["made"])}</p>'
        f'<h5>Работа с типографикой</h5><p>{E(data["typography"])}</p><dl><div><dt>Программы</dt><dd>{E(data["programs"])}</dd></div><div><dt>Срок</dt><dd>{E(data["duration"])}</dd></div></dl>'
        f'<h5>Результат</h5><p>{E(data["result"])}</p></div></details></article>'
    )


def home():
    global P
    P = ""
    cards = "".join(project_card(key, data, i) for i, (key, data) in enumerate(D.items(), 1))
    extras = "".join(other_card(data) for data in OTHER)
    tabs = "".join(
        f'<button type="button" role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}" data-pose="{pose}"><span>{i + 1:02d}</span>{label}<i aria-hidden="true">↗</i></button>'
        for i, (key, label, pose, title, body) in enumerate(ABOUT)
    )
    panels = "".join(
        f'<section id="panel-{key}" role="tabpanel" aria-labelledby="tab-{key}" tabindex="0" {"hidden" if i else ""}><h3>{title}</h3>{body}</section>'
        for i, (key, label, pose, title, body) in enumerate(ABOUT)
    )
    ticker = '<span>АЙДЕНТИКА</span><b aria-hidden="true">✳</b><span>UX/UI</span><b aria-hidden="true">✳</b><span>WEB DESIGN</span><b aria-hidden="true">✳</b><span>ПОЛИГРАФИЯ</span><b aria-hidden="true">✳</b><span>EDITORIAL</span><b aria-hidden="true">✳</b><span>УПАКОВКА</span><b aria-hidden="true">✳</b><span>МНОГОСТРАНИЧНАЯ ВЕРСТКА</span><b aria-hidden="true">✳</b><span>НАВИГАЦИЯ</span><b aria-hidden="true">✳</b><span>ПРЕДПЕЧАТНАЯ ПОДГОТОВКА</span><b aria-hidden="true">✳</b><span>DIGITAL</span><b aria-hidden="true">✳</b><span>AI-ИНСТРУМЕНТЫ</span><b aria-hidden="true">✳</b>'
    return head(
        "Диана Тхайцухова — графический дизайнер / UX/UI",
        "Системы визуальной коммуникации для брендов, продуктов и сервисов: айдентика, интерфейсы, упаковка, полиграфия и многостраничные материалы.",
    ) + f'''<body id="top">{header(True)}<main id="main">
<section class="wrap hero" id="home"><div class="hero-copy"><p class="eyebrow">Графический дизайнер · UX/UI</p><h1><span>Диана</span><span>Тхайцухова<span class="accent-dot">.</span></span></h1><p class="hero-line">Помогаю идеям обрести<br><span class="gradient-text">форму, характер и голос.</span></p><ul class="hero-capabilities"><li><strong>Проектирую</strong><span>айдентику, интерфейсы, упаковку, полиграфию и многостраничные материалы.</span></li><li><strong>Систематизирую</strong><span>ТЗ и контент, выстраиваю визуальный принцип, типографику и иерархию.</span></li><li><strong>Довожу до реализации</strong><span>масштабирую решение на носители и сопровождаю до разработки, печати или производства.</span></li></ul><p class="hero-tools">Figma · Illustrator · InDesign · Photoshop · Microsoft Office · CRM / CMS · AI-инструменты</p><div class="actions">{btn('#projects', 'Смотреть проекты', 'solid', 'data-hero-cta')}{btn('assets/docs/diana-tkhaytsukhova-resume.pdf', 'Скачать резюме', 'outline', 'download')}</div><p class="availability"><span aria-hidden="true"></span> Открыта к предложениям · Санкт-Петербург / удалённо</p><a class="hero-telegram" href="https://t.me/soulminori" target="_blank" rel="noopener">Написать в Telegram · @soulminori ↗</a><a class="hero-phone" href="tel:+79513857017">+7 951 385-70-17</a></div><div class="hero-stage noise-panel"><div class="hero-halo" aria-hidden="true"></div><span class="floating-label">ТЗ → СИСТЕМА<br>→ РЕАЛИЗАЦИЯ</span><span class="hero-asterisk" aria-hidden="true">✳</span>{decor('ribbon', 'hero-decor-one')}{decor('star', 'hero-decor-two')}{mascot('urban-neutral', 'hero-character', True)}<button type="button" class="hello-button" data-greet>Привет, я Диана <span aria-hidden="true">↗</span></button><span class="stage-coordinate" aria-hidden="true">ИДЕЯ → СИСТЕМА → НОСИТЕЛЬ</span></div></section>
<section class="wrap experience-overview" id="experience"><div><p class="eyebrow">Коротко об опыте</p><h2><span class="heading-line">Коммерческие</span><span class="heading-line">выставочные</span><span class="heading-line">производственные</span><span class="heading-line"><em>задачи.</em></span></h2></div><div><p>Работала с <strong>айдентикой</strong>, <strong>UX/UI</strong>, <strong>editorial-дизайном</strong>, упаковкой, навигацией, digital- и выставочной коммуникацией. Проектировала <strong>модульные сетки</strong> и системы абзацных стилей, структурировала технический контент, спецификации, таблицы и продуктовые данные, готовила многостраничные каталоги, печатные носители и упаковочные развёртки.</p><p>Веду проект от <strong>декомпозиции ТЗ</strong> и контентной архитектуры до <strong>prepress</strong> и production-ready файлов: цветовые профили, вылеты, безопасные поля, линии реза и сгиба, контрольные PDF, цветопробы и постпечатная обработка. Согласовываю решения с маркетингом, инженерами, технологами, разработчиками, типографиями и производственными подрядчиками.</p><div class="experience-tags" aria-label="Ключевые компетенции"><span>Контентная архитектура</span><span>Модульные сетки</span><span>Типографика</span><span>Prepress</span><span>Production-ready</span><span>Техническая документация</span></div><nav class="experience-links" aria-label="Ссылки на примеры опыта"><a href="#other-severnaya-zarya">Инженерные выставки, каталоги и упаковка →</a><a href="#project-language">Редакционный дизайн — дипломный проект →</a><a href="#projects">Айдентика и носители — избранные кейсы →</a></nav></div></section>
<div class="ticker" aria-label="Компетенции"><div class="ticker-track"><div>{ticker}</div><div aria-hidden="true">{ticker}</div></div></div>
<section id="projects" class="wrap section"><div class="section-heading"><div><p class="eyebrow">01—04 / Избранные кейсы</p><h2><span class="heading-line">Реализованные проекты.</span><span class="heading-line">Конкретная роль</span><span class="heading-line"><em>и результат.</em></span></h2></div><p>В каждом кейсе: задача, моя роль, выполненные работы, процесс, типографика, программы, срок и подтверждаемый результат.</p></div>{decor('loop', 'projects-decor')}<div class="project-grid">{cards}</div><div class="other-heading"><h3>Другие реализованные работы</h3><p>Каждый проект раскрывается в компактный кейс: задача, роль, типографика, инструменты и результат.</p></div><div class="other-grid">{extras}</div></section>
<section id="about" class="wrap section about"><div class="section-heading"><div><p class="eyebrow">04 / Обо мне</p><h2>Не только работы,<br>но и человек <em>за ними.</em></h2></div><p>Опыт, инструменты, образование и то, как я веду комплексные проекты.</p></div>{decor('cloud', 'about-decor')}<div class="about-desk"><div class="about-navigation"><p class="eyebrow">Выберите раздел</p><div role="tablist" aria-label="Разделы обо мне" aria-orientation="vertical">{tabs}</div><a class="text-link" href="assets/docs/diana-tkhaytsukhova-resume.pdf" download>Скачать резюме · PDF ↓</a></div><div class="about-content noise-panel">{panels}</div><aside class="about-companion" aria-hidden="true">{mascot('urban-wave')}<span class="companion-note">Приятно познакомиться!</span></aside></div>
</section><section class="workshop-teaser noise-panel" id="workshop"><div class="wrap workshop-teaser-grid"><div><p class="eyebrow">Дополнительное увлечение · хобби</p><h2>Мастерская «Хуторок» —<br>дизайн, который можно <em>держать в руках.</em></h2><p class="lead">В свободное время создаю свечи и гипсовые изделия, занимаюсь живописью и 3D-печатью.</p><p>Это моё дополнительное увлечение: здесь я экспериментирую с материалом, формой, небольшими сериями, упаковкой и предметной съёмкой.</p><div class="chips"><span>Свечи</span><span>Гипс</span><span>Живопись</span><span>3D-печать</span></div><div class="workshop-actions">{btn('workshop.html', 'Заглянуть в мастерскую', 'light')}</div></div><div class="workshop-composition"><figure class="workshop-photo">{img('assets/img/workshop/handmade-07-pink-set.webp', 'Свечи и подарочный набор мастерской Хуторок')}</figure>{mascot('urban-present', 'teaser-character')}<span class="paper-note">Хобби, материал<br>и ручная практика</span></div></div></section>{contacts()}</main>{footer()}'''


CASE_HOOKS = {
    "govori": "Система для полного<br>маршрута <em>участника.</em>",
    "buro": "Сервисный сценарий<br>для <em>личной истории.</em>",
    "language": "Два издания.<br>Два сценария <em>чтения.</em>",
    "calmes": "Один визуальный язык<br>для меню и <em>упаковки.</em>",
}


def case(key, index):
    global P
    P = "../"
    data = D[key]
    gallery = []
    for src, label, span, fit, note in O[key]["images"]:
        name = Path(src).name
        if name in data["omit"] or name == data["hero"]:
            continue
        caption = data["captions"].get(name, label)
        gallery.append(
            f'<figure class="case-figure {"wide" if span == 12 else ""}" data-reveal>{img(src, caption, zoom=True)}'
            f'<figcaption><span>{len(gallery) + 1:02d}</span>{E(caption)}</figcaption></figure>'
        )
    process = "".join(
        f'<article data-reveal><span class="decision-no">0{i}</span><h3>{E(title)}</h3><p>{E(body)}</p></article>'
        for i, (title, body) in enumerate(data["process"], 1)
    )
    deliverables = "".join(f'<li>{E(item)}</li>' for item in data["deliverables"])
    next_key = list(D)[(index + 1) % 4]
    decor_name = {"govori": "ribbon", "buro": "rings", "language": "cloud", "calmes": "flower"}[key]
    mascot_pose = {"govori": "urban-point", "buro": "urban-crouch", "language": "urban-tablet", "calmes": "urban-present"}[key]
    return head(data["title"] + " — реализованный кейс Дианы Тхайцуховой", data["lead"]) + f'''<body id="top" class="case-page case-{key}" style="--project-color:{data['accent']}">{header()}<main id="main"><div class="wrap breadcrumb"><a href="../index.html#project-{key}">← Все проекты</a><span>Кейс {index + 1:02d} / 04</span></div>
<section class="wrap case-title"><p class="eyebrow">{E(data['category'])}</p><h1>{E(data['title'])}</h1><div class="case-summary"><p class="lead">{E(data['lead'])}</p><span class="status real">{E(data['status'])}</span><button class="text-link" type="button" data-copy-link>Скопировать ссылку ↗</button></div><dl class="case-facts"><div><dt>Моя роль</dt><dd>{E(data['role'])}</dd></div><div><dt>Срок</dt><dd>{E(data['duration'])}</dd></div><div><dt>Программы</dt><dd>{E(data['programs'])}</dd></div><div><dt>Статус</dt><dd>{E(data['status'])}</dd></div></dl>{decor(decor_name, 'case-title-decor')}</section>
<figure class="case-opening noise-panel">{img('assets/img/projects/' + key + '/' + data['hero'], data['title'] + ' — ключевая визуализация', eager=True, zoom=True)}<figcaption>Ключевой кадр реализованного проекта</figcaption></figure>
<nav class="case-nav" aria-label="Главы кейса"><div class="wrap"><a href="#brief">01 · Задача</a><a href="#process">02 · Процесс</a><a href="#type">03 · Типографика</a><a href="#gallery">04 · Носители</a><a href="#result">05 · Результат</a></div></nav>
<section id="brief" class="wrap section case-brief"><div><p class="eyebrow">01 / Задача и объём</p><h2>{CASE_HOOKS[key]}</h2></div><div><h3>Задача</h3><p>{E(data['task'])}</p><h3>Что я сделала</h3><ul class="deliverables">{deliverables}</ul></div></section>
<section id="process" class="case-system noise-panel"><div class="wrap"><p class="eyebrow">02 / Процесс и решения</p><h2>Как проект превратился<br>в <em>работающую систему.</em></h2><div class="decision-grid four">{process}</div></div></section>
<section id="type" class="wrap section case-typography"><div><p class="eyebrow">03 / Работа с типографикой</p><h2><span class="heading-line">Типографика</span><span class="heading-line">следует за</span><span class="heading-line"><em>содержанием.</em></span></h2></div><p class="lead">{E(data['typography'])}</p></section>
<section id="gallery" class="wrap section"><div class="section-heading"><div><p class="eyebrow">04 / Макеты и носители</p><h2>Система в разных<br><em>форматах.</em></h2></div><p>Нажмите, чтобы открыть крупнее.</p></div><div class="case-gallery">{''.join(gallery)}</div></section>
<section id="result" class="wrap case-result"><div><p class="eyebrow">05 / Результат</p><h2>Что было реализовано</h2><p class="lead">{E(data['outcome'])}</p><div class="result-actions"><p class="outcome-line">{E(data['outcome_line'])}</p>{btn('../index.html#contact', 'Обсудить со мной проект')}</div></div>{mascot(mascot_pose, 'result-character')}</section>
<nav class="wrap next-case" aria-label="Следующий проект"><a href="{next_key}.html"><span class="eyebrow">Следующий кейс / {(index + 1) % 4 + 1:02d}</span><strong>{E(D[next_key]['title'])}</strong><span aria-hidden="true">↗</span></a></nav></main>{footer()}'''


if __name__ == "__main__":
    (R / "index.html").write_text(home(), encoding="utf-8")
    for number, key in enumerate(D):
        (R / "projects" / f"{key}.html").write_text(case(key, number), encoding="utf-8")
    print("Built the home page and four case pages; workshop page preserved.")
