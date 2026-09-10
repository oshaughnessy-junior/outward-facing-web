# Bibliography maintenance

Run from the site checkout with Python 3 (standard library; curl is a TLS fallback):

```sh
python3 scripts/web_bibliography_refresh.py --check --since 2026-01-01
python3 scripts/web_bibliography_refresh.py --apply --since 2026-01-01
python3 scripts/web_bibliography_refresh.py --check --since 2026-01-01
python3 -m unittest discover -s tests -p 'test_web_bibliography_refresh.py'
```

For newly announced papers, use `--ids ID [ID ...]`. `--source metadata.json`
accepts a reviewed list of public records with arxiv, title, authors, published
(ISO date), and primary_class fields. Author discovery excludes different author
identities; explicit ID/offline inputs reject them. Truncated feeds and malformed
metadata fail without advancing the check record. Existing entries are preserved;
arXiv identifiers in eprint, DOI, URL, or eid fields prevent duplicate additions.
Journal-version/DOI reconciliation still requires editorial review.

Exit 0 means no missing records (check) or successful file update (apply), 1 means
missing entries (check), and 2 means failure. The timestamp on the publications
page is a metadata check, not a deployment receipt or completeness guarantee.

After apply, inspect the diff, build with the project's locked dependencies,
commit the changed bibliography/status files, deploy, and verify the live page.
Only live verification completes a maintenance task. This command does not
schedule itself, publish the site, or create/approve blog posts.
