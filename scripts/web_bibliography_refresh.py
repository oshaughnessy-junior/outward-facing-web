#!/usr/bin/env python3
"""Append verified arXiv metadata; failures never advance the public check record.

Use --check before --apply. This tool does not build, deploy, or authorize blogs.
Author discovery is capped at 1000 records and fails if coverage is truncated.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / '_bibliography/papers.bib'
STATUS = ROOT / '_data/publications_status.json'
ATOM = 'http://www.w3.org/2005/Atom'
ARXIV = 'http://arxiv.org/schemas/atom'
OPEN = 'http://a9.com/-/spec/opensearch/1.1/'


def normalize_id(value):
    if not isinstance(value, str) or not re.fullmatch(r'\d{4}\.\d{4,5}(?:v\d+)?', value):
        raise ValueError('invalid arXiv identifier')
    return value.split('v')[0]


def parse_feed(data):
    root = ET.fromstring(data)
    if root.tag != f'{{{ATOM}}}feed':
        raise ValueError('not an Atom feed')
    records = []
    for entry in root.findall(f'{{{ATOM}}}entry'):
        uri = urllib.parse.urlparse(entry.findtext(f'{{{ATOM}}}id') or '')
        if uri.hostname not in ('arxiv.org', 'export.arxiv.org') or not uri.path.startswith('/abs/'):
            raise ValueError('invalid arXiv entry URL')
        category = entry.find(f'{{{ARXIV}}}primary_category')
        records.append({'arxiv': normalize_id(uri.path.rsplit('/', 1)[-1]),
            'title': ' '.join((entry.findtext(f'{{{ATOM}}}title') or '').split()),
            'authors': [' '.join((a.findtext(f'{{{ATOM}}}name') or '').split()) for a in entry.findall(f'{{{ATOM}}}author')],
            'published': (entry.findtext(f'{{{ATOM}}}published') or '')[:10],
            'primary_class': category.get('term', '') if category is not None else ''})
    total = root.findtext(f'{{{OPEN}}}totalResults')
    if total is None or int(total) != len(records):
        raise ValueError('incomplete/truncated feed; use narrower source coverage')
    return records


def fetch(params):
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'public-bibliography-refresh/1.0'})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
    except Exception:
        data = subprocess.run(['curl', '--fail', '--silent', '--show-error', '--max-time', '45', url], capture_output=True, check=True, timeout=50).stdout
    return parse_feed(data)


def is_pi_record(record):
    authors = record.get('authors', []) if isinstance(record, dict) else []
    if not isinstance(authors, list):
        return False
    names = [re.sub(r'[^a-z]', '', a.lower()) for a in authors if isinstance(a, str)]
    return any(n in ('roshaughnessy', 'richardoshaughnessy', 'oshaughnessyr', 'oshaughnessyrichard') for n in names)


def validate(records):
    if not isinstance(records, list) or not records:
        raise ValueError('metadata source must contain a non-empty list')
    seen = set()
    result = []
    for record in records:
        if not isinstance(record, dict):
            raise ValueError('record must be an object')
        r = dict(record)
        r['arxiv'] = normalize_id(r.get('arxiv'))
        if r['arxiv'] in seen:
            raise ValueError('duplicate source identifier')
        seen.add(r['arxiv'])
        if not isinstance(r.get('title'), str) or not r['title'].strip():
            raise ValueError('missing title')
        if not isinstance(r.get('authors'), list) or not r['authors'] or not all(isinstance(a, str) and a.strip() for a in r['authors']):
            raise ValueError('invalid authors')
        day = date.fromisoformat(r.get('published', ''))
        if day > datetime.now(timezone.utc).date():
            raise ValueError('future publication date')
        if not isinstance(r.get('primary_class'), str) or not re.fullmatch(r'[A-Za-z0-9.-]+', r['primary_class']):
            raise ValueError('missing or invalid primary category')
        # Identity guard: author name must match the PI, not another surname match.
        if not is_pi_record(r):
            raise ValueError('source does not identify Richard O\'Shaughnessy')
        result.append(r)
    return result


def tex(text):
    return ''.join({'\\':r'\textbackslash{}','{':r'\{','}':r'\}','%':r'\%','&':r'\&','#':r'\#','_':r'\_','$':r'\$','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in text)


def render(r):
    aid = r['arxiv']
    day = date.fromisoformat(r['published'])
    authors = ' and '.join(tex(a) for a in r['authors'])
    return f'''@misc{{arxiv-{aid},
  author = {{{authors}}},
  title = {{{{{tex(r['title'])}}}}},
  year = {{{day.year}}},
  month = {{{day.strftime('%b').lower()}}},
  journal = {{arXiv e-prints}},
  archivePrefix = {{arXiv}},
  eprint = {{{aid}}},
  primaryClass = {{{r['primary_class']}}},
  url = {{https://arxiv.org/abs/{aid}}}
}}
'''


def ids_in(text):
    pattern = r'(?:arxiv\s*[:./]|arxiv\.org/(?:abs|pdf)/|eprint\s*=\s*[{"]?)(\d{4}\.\d{4,5})'
    return set(re.findall(pattern, text, re.I))


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as stream:
            name = stream.name
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--apply', action='store_true')
    source = parser.add_mutually_exclusive_group()
    source.add_argument('--source', type=Path, help='reviewed public metadata JSON list')
    source.add_argument('--ids', nargs='+')
    parser.add_argument('--author', default="O'Shaughnessy")
    parser.add_argument('--since', default='2026-01-01')
    args = parser.parse_args(argv)
    try:
        since = date.fromisoformat(args.since)
        if args.source:
            records = json.loads(args.source.read_text())
            query = 'reviewed public metadata; explicit IDs'
        elif args.ids:
            wanted = {normalize_id(x) for x in args.ids}
            records = fetch({'id_list': ','.join(sorted(wanted)), 'max_results': 1000})
            if {r['arxiv'] for r in records} != wanted:
                raise ValueError('requested IDs missing from response')
            query = 'explicit arXiv IDs'
        else:
            records = fetch({'search_query': f'au:"{args.author}" AND submittedDate:[{since.strftime("%Y%m%d")}0000 TO {datetime.now(timezone.utc).strftime("%Y%m%d")}2359]' , 'sortBy': 'submittedDate', 'sortOrder': 'descending', 'max_results': 1000})
            records = [r for r in records if date.fromisoformat(r['published']) >= since]
            query = f'author:{args.author};since:{since}'
        if not args.source and not args.ids:
            excluded = [r['arxiv'] for r in records if not is_pi_record(r)]
            print('excluded other author identities: ' + ','.join(excluded))
            records = [r for r in records if is_pi_record(r)]
        records = validate(records)
        current = BIB.read_text()
        existing = ids_in(current)
        missing = [r for r in records if r['arxiv'] not in existing]
        # Render everything before either file is touched. Bibliography is replaced
        # first; a crash before status leaves a stale check date and retry dedups.
        updated = ''.join(render(r) + '\n' for r in missing) + current
        status = json.dumps({'last_successful_refresh': datetime.now(timezone.utc).isoformat(), 'query': query,
            'records_checked': [r['arxiv'] for r in records], 'records_added': [r['arxiv'] for r in missing]}, indent=2) + '\n'
        print(f'records={len(records)} missing={len(missing)}')
        if args.check:
            return 1 if missing else 0
        if missing:
            atomic_write(BIB, updated)
        atomic_write(STATUS, status)
        return 0
    except Exception as exc:
        print(f'refresh failed: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
