"""Check page/feed agreement for explicit AI, legacy AI, and astrophysics posts.

Run against the real Jekyll output: python3 tests/check_lane_output.py _site
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(sys.argv[1])
feeds = {}
for lane in ('astrophysics', 'ai-agents'):
    tree = ET.parse(root / lane / 'feed.xml')
    feeds[lane] = {item.findtext('link').rstrip('/').split('/')[-1]
                   for item in tree.findall('./channel/item')}

cases = {
    # This post has explicit AI metadata but is absent from the legacy slug list.
    'llms-and-reproducible-science': 'ai-agents',
    'getting-started-with-openclaw-custom-task-workspaces': 'ai-agents',
    'reconstructing-the-family-histories-of-black-holes': 'astrophysics',
}
for slug, expected in cases.items():
    for lane in feeds:
        should_appear = lane == expected
        assert (slug in feeds[lane]) == should_appear, (slug, lane, 'feed')
        page = (root / lane / 'index.html').read_text()
        assert (f'/{slug}/' in page) == should_appear, (slug, lane, 'page')
assert feeds['astrophysics'].isdisjoint(feeds['ai-agents']), 'Overlapping lanes'
print('Lane regression passed: explicit AI, legacy AI, science, page/feed agreement')
