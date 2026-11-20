"""Verify primary links in the rendered bibliography, not just identifier text."""
import sys
from html.parser import HTMLParser
from pathlib import Path


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.hrefs.add(dict(attrs).get('href'))


page = Links()
page.feed((Path(sys.argv[1]) / 'publications/index.html').read_text())
# New arrivals and an earlier imported eprint must expose clickable primary sources.
for ident in ('2611.26534', '2609.29969', '2610.40144'):
    assert f'https://arxiv.org/abs/{ident}' in page.hrefs, ident
assert 'https://arxiv.org/abs/' not in page.hrefs, 'Empty arXiv button'
print('Rendered bibliography primary links passed')
