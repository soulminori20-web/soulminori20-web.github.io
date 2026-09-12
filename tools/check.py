"""Check publishable HTML: local resources, duplicate IDs and fragment links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.refs=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        for key in ['src','href']:
            if key in attrs:self.refs.append(attrs[key])
R=Path(__file__).resolve().parents[1];errors=[];count=0
for f in [R/'index.html',R/'workshop.html',*R.glob('projects/*.html')]:
    page=Page(f.read_text())
    if len(page.ids)!=len(set(page.ids)):errors.append((str(f),'duplicate IDs'))
    for ref in page.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        target=f.parent/unquote(u.path) if u.path else f
        if not target.exists():errors.append((str(f),ref))
        elif u.fragment and target.suffix=='.html' and u.fragment not in Page(target.read_text()).ids:errors.append((str(f),'anchor '+ref))
        count+=1
print(f'Checked {count} local references across six pages. Errors: {errors}')
raise SystemExit(bool(errors))
