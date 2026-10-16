"""Controleer de volledige conceptsites zonder extra dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import sys

root = Path(__file__).resolve().parents[1]
errors = []

class DemoParser(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.hidden = 0
        self.visible = []
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {'script', 'style'}:
            self.hidden += 1
        if tag == 'meta' and attrs.get('name') == 'robots':
            self.noindex = 'noindex' in attrs.get('content', '')
        for key in ('href', 'src'):
            value = attrs.get(key, '')
            if value.startswith('/demos/'):
                target = root / unquote(urlsplit(value).path).lstrip('/')
                if not target.is_file() and not (target / 'index.html').is_file():
                    errors.append(f'{self.page.relative_to(root)}: ontbreekt {value}')

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.visible.append(data)

pages = list((root / 'demos').rglob('*.html'))
for page in pages:
    parser = DemoParser(page)
    parser.feed(page.read_text(encoding='utf-8'))
    if re.search(r'Paul van|van den Heerik|Kooman|Fenno|Hendriksen', ' '.join(parser.visible), re.I):
        errors.append(f'{page.relative_to(root)}: oorspronkelijke klantnaam in zichtbare tekst')
    if not parser.noindex and page.name != '404.html' and page.parent.name != '404':
        errors.append(f'{page.relative_to(root)}: noindex ontbreekt')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'{len(pages)} demopagina’s: lokale links en assets bestaan, geen klantnamen in zichtbare tekst, noindex aanwezig.')
