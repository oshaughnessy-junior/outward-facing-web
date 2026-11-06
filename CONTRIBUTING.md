# Contributing to the Site

If you notice a typo, outdated information, or want to add a new post/member to the site, please open a GitHub Issue using the following guidelines:

### How to Request a Website Update

1. **Title**: Start your title with `[Feedback]` followed by the section you are referring to.
   - Examples: `[Feedback] People: Update my graduation year`, `[Feedback] Posts: Fix typo in Recent News`.
2. **Details**: In the issue body, please provide:
   - **Location**: The URL of the page or the name of the section.
   - **Current State**: What is currently written (or a screenshot).
   - **Requested Change**: Exactly what the text/link should be changed to.
   - **Reasoning**: A brief note on why this change is needed.

Your request will be processed by the site's autonomous assistant. You will be notified via the issue thread once the change is live.

## Research website release checklist

This is the maintained release checklist for this site. Assistant owns routine maintenance; the release executor records the source commit, CI run, and live verification in the owning issue/activity.

1. Review identity changes against PI-confirmed facts and scientific claims against primary papers. Keep astrophysics primary and published results distinct from experimental agent work. Bibliography maintenance does not grant blog or manuscript approval.
2. Refresh public metadata with `scripts/web_bibliography_refresh.py`, inspect the diff, and repeat the check to confirm deduplication. Preserve failure/cursor evidence; a metadata timestamp is not a deployment receipt.
3. Run the locked formatter and production build. Preview with the configured `/outward-facing-web/` prefix and verify that the preview loads its own CSS. A missing stylesheet invalidates visual/contrast conclusions.
4. Run the existing **Axe accessibility testing** workflow on the exact candidate ref with its URL input empty. It checks seven primary routes, saves `axe-results.json`, and saves desktop/mobile rendering evidence in `layout-evidence`. Inspect screenshots as well as automated findings. A failure must identify its route/rule/selector; retain environment failures separately and do not suppress rules to obtain a pass.
5. After an authorized merge, verify the successful deployment for the exact merged commit, then independently fetch changed public routes and primary links. Check team identity and both lane feeds when relevant. Record any difference between the candidate build and live output.
6. Save the result and one concrete owner/action for unfinished work. Routine site repairs use existing authorization; genuine paper/blog lifecycle holds remain separate. Do not call an audit full accessibility certification or a traffic-capacity test.

The audit workflow builds an isolated root-prefix preview; it does not deploy the site. Run it with:

```sh
gh workflow run axe.yml --ref YOUR_CANDIDATE_BRANCH
```

Keep comprehensive audits at least fourteen elapsed days apart. Candidate release checks and publication-arrival maintenance can run independently.
