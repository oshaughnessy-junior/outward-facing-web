import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('refresh', Path(__file__).parents[1] / 'scripts/web_bibliography_refresh.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def rec(aid='2609.09999'):
    return {'arxiv': aid, 'title': 'Test paper', 'authors': ["Richard O'Shaughnessy"], 'published': '2026-09-01', 'primary_class': 'astro-ph.HE'}


class RefreshTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.bib, self.status, self.source = [self.root / x for x in ('papers.bib', 'status.json', 'source.json')]
        self.bib.write_text('original\n')
        self.status.write_text('old\n')
        self.patches = [patch.object(mod, 'BIB', self.bib), patch.object(mod, 'STATUS', self.status)]
        for p in self.patches:
            p.start()
            self.addCleanup(p.stop)

    def apply(self, records):
        self.source.write_text(json.dumps(records))
        return mod.main(['--apply', '--source', str(self.source)])

    def test_invalid_records_leave_both_files_unchanged(self):
        for bad in ({'arxiv': 'bad'}, dict(rec(), published='2026-99-10'), dict(rec(), authors='name'), dict(rec(), authors=['Someone Else']), dict(rec(), primary_class=''), 'wrong type'):
            with self.subTest(record=bad):
                self.assertEqual(self.apply([rec('2609.09998'), bad]), 2)
                self.assertEqual(self.bib.read_text(), 'original\n')
                self.assertEqual(self.status.read_text(), 'old\n')

    def test_repeat_apply_deduplicates(self):
        self.assertEqual(self.apply([rec()]), 0)
        first = self.bib.read_text()
        self.assertEqual(self.apply([rec()]), 0)
        self.assertEqual(self.bib.read_text(), first)
        self.assertNotIn(str(self.root), self.status.read_text())

    def test_supported_existing_identifiers(self):
        for entry in ('eprint = "2609.09999v2"', 'doi={10.48550/arXiv.2609.09999}', 'url={https://arxiv.org/abs/2609.09999v1}', 'eid={arXiv:2609.09999}'):
            self.bib.write_text(entry)
            self.assertEqual(self.apply([rec()]), 0)
            self.assertEqual(self.bib.read_text(), entry)

    def test_feed_namespace_and_truncation(self):
        feed = '''<feed xmlns="http://www.w3.org/2005/Atom" xmlns:o="http://a9.com/-/spec/opensearch/1.1/" xmlns:r="http://arxiv.org/schemas/atom"><o:totalResults>1</o:totalResults><entry><id>http://arxiv.org/abs/2609.09999v1</id><r:primary_category term="gr-qc"/></entry></feed>'''
        self.assertEqual(mod.parse_feed(feed)[0]['primary_class'], 'gr-qc')
        with self.assertRaises(ValueError):
            mod.parse_feed(feed.replace('>1<', '>2<'))

    def test_source_failure_does_not_advance_status(self):
        with patch.object(mod, 'fetch', side_effect=RuntimeError('source offline')):
            self.assertEqual(mod.main(['--apply', '--ids', '2609.09999']), 2)
        self.assertEqual(self.status.read_text(), 'old\n')
        self.assertEqual(self.bib.read_text(), 'original\n')


if __name__ == '__main__':
    unittest.main()
