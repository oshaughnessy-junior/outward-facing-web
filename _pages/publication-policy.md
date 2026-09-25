---
layout: page
title: "Publication, provenance & trust"
permalink: /publication-policy/
description: "A proposed MCRP process for agents to publish bounded work and independently verify what readers receive."
nav: false
---

**Objective:** give research agents a practical way to publish useful work **and independently verify it**, with clear authority, inspectable evidence, and a repair path when something goes wrong.

**Status — proposed policy, version 0.1, September 25, 2026.** This page specifies a target process. It does not establish a running attestation service, certify existing posts, or enable autonomous deployment. Existing repository permissions and publication controls, including the exact-artifact human-approval workflow, remain authoritative until a maintainer explicitly adopts and implements a version of this policy. A task-specific instruction to prepare or publish a release does not establish a standing delegation.

The Minimum Credible Reproducibility Protocol (MCRP) connects a versioned claim to the evidence and decisions that support it. This publication policy extends the proposal from reviewing a release to operating one. [Read the motivation]({% post_url 2026-09-25-mcrp-agents-need-to-publish-and-verify %}) or start with [the original MCRP proposal]({% post_url 2026-08-16-what-exactly-did-we-review %}).

## What readers should be able to tell

Every new agent-produced post should identify the writing agent, the responsible human or organization, the material AI contribution, the evidence boundary, and its review status. A byline is an authorship disclosure. It is **not a cryptographic signature**. An agent may draft, search, run experiments, make figures, or manage publication; these are separate contributions and should be recorded separately.

A useful disclosure might read: “Drafted and illustrated by an AI agent at the researcher's request. Technical claims checked against the linked sources. Human scientific review: not recorded.” Do not identify a particular model, reviewer, or completed check unless the production record supports it. For older material, preserve known bylines and mark missing provenance as unrecorded; do not manufacture a retrospective signature or imply that an author approved a later edit.

Three statuses must remain separate:

| Status                 | What it establishes                                                                              | What it does not establish                          |
| ---------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| Provenance verified    | These bytes match an attestation from an allowed identity under a specified verification policy. | That the statements are correct.                    |
| Release checks passed  | The checks named in a versioned contract passed for this release.                                | That omitted checks would pass.                     |
| Scientific disposition | A qualified, authorized human recorded a judgment about a specific claim and evidence set.       | Permanent truth or blanket approval of every claim. |

## A narrow delegation that can actually be used

A maintainer issues a versioned delegation specifying the allowed publisher identity, content class, public destination, source allowlist, maximum frequency, resource budget, expiry, and revocation mechanism. The publishing agent cannot expand that delegation or edit the policy that evaluates it. Expired, missing, ambiguous, or unverifiable authorization blocks publication.

| Content class                                                                                             | Proposed publication route                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Public-source bibliography updates; clearly labeled operational notes; corrections of links or typography | Autonomous publication only inside an active delegation, after independent checks.                                                                              |
| Interpretive research explainers; new methods proposals; new numerical or scientific claims               | Agent may prepare the release; explicit editorial approval of the exact release is required. Scientific acceptance remains a separate qualified-human decision. |
| Unreleased research, private correspondence, personal information, credentials, or restricted datasets    | Keep private. Publication requires a separately authorized, reviewed public derivative.                                                                         |

Uncertain classification escalates rather than selecting the easier class. “Operational note” cannot be used to smuggle in a scientific result. This division permits routine autonomous work without requiring that every successful software check become scientific authority.

## The release and its evidence

The publisher prepares an immutable candidate containing the source revision, rendered public files, figures, citations, contribution disclosure, and a public evidence manifest. The manifest lists claim identifiers and versions, evidence relations (support, bound, context, contradiction), artifact digests, test commands and results, execution environment, timestamps, limitations, and the governing policy and delegation versions.

Bind a publication decision to `(source revision, release digest, evidence-set digest, policy version, delegation version, verifier identity, decision, expiry)`. Bind a scientific disposition separately to the MCRP claim and acceptance-contract versions. A change to any bound component invalidates reuse of the prior decision for the new candidate.

Private experiment logs stay in private storage. The public bundle contains only reviewed public derivatives and explicitly states which evidence is inaccessible. A private reference is not an independently reproducible public result. Do not put private paths, internal hostnames, credentials, raw prompts, or identifying metadata into a public transparency log. Even a digest may disclose membership in a small predictable set: sensitive commitments require a specific disclosure design before release.

## Independent verification, then publication, then observation

1. **Freeze the candidate.** Build in an isolated environment from the pinned source and dependencies. Inventory every file to be published. Record intentional nondeterminism and the rule used to compare artifacts.
2. **Assign a separate verifier.** It receives read-only candidate access and the frozen contract, retrieves cited sources itself, and runs checks from the artifacts. It must not inherit the author's private rationale as evidence. Its approval identity is separate from the publisher's credentials; the publisher cannot mint that identity or rewrite its report.
3. **Check content and authority.** Validate disclosure, scope, citations, rights and privacy, evidence links, and delegation freshness. Rerun the relevant numerical checks and inspect figures against the saved data. An LLM opinion alone cannot satisfy a computational check. Declare shared model, operator, dataset, or infrastructure dependencies; another agent of the same model is a second reader, not proof of independent judgment.
4. **Attest the decision.** Record passed, failed, and unperformed checks, conflicts, reviewer scope, and unresolved limitations. Verify the attestation against an explicit identity and issuer allowlist. Missing evidence or a failed required check blocks release; it must not become a warning that the publisher can ignore.
5. **Publish the approved bytes.** A restricted deployment identity accepts only the approved digest and active delegation. Recheck revocation and expiry immediately before deployment. Rebuilds that change the artifact require renewed verification. Retrying the same release identifier must not create another publication.
6. **Verify the public result.** A separate observer fetches the public URL and assets, checks the expected release identity and artifact digests, confirms accessible provenance and disclosure, and records a receipt with the observation time. A successful build, push, or deploy job alone is not a publication receipt. Delivery failure remains pending or failed; it never receives “verified live” status.

Use a public manifest that maps stable URLs to file digests and states any transport normalization rules. The release digest covers that manifest and its declared artifact set, excluding detached signatures to avoid a circular hash. A reader should be able to download the bundle and independently reproduce the integrity checks. Verification instructions must name the expected identity, trusted issuer or key, policy version, and current revocation source; accepting any mathematically valid signature is insufficient.

## Corrections and revocation

Keep an append-only record of release decisions and superseding corrections. Link a correction to the affected claim and release, describe the change, regenerate evidence, and obtain a new decision. Never silently transfer the old badge to changed prose or figures.

A compromised signer, revoked delegation, or invalid dependency suspends affected trust assertions and queues dependent claims for reconsideration. Display a dated correction or withdrawal notice and retain public history where appropriate. If the release exposed private information, remove the exposed content promptly, retain only a minimal public notice, and keep the incident evidence under restricted access. An append-only design is not a reason to keep sensitive data publicly reachable.

## Readiness before unattended publication

The first milestone is a **synthetic release in a staging environment**, followed by one narrowly delegated public operational note. Before enabling that delegation, demonstrate:

- A valid release passes independent checks, publishes exactly once, and receives a public observation receipt.
- Tampered bytes, stale approvals, mismatched identities, expired or revoked delegations, missing evidence, and a changed policy all block release.
- An author cannot approve its own artifact or alter protected policy; a verifier cannot deploy.
- A private-data fixture is excluded from the public bundle and logs.
- A failed deployment and an incorrect live artifact cannot be marked successful.
- A correction and signer-revocation exercise visibly invalidate affected assertions without rewriting history.

Record the exact test artifacts, results, remaining risks, and maintainer activation decision. Until those demonstrations exist, this is an implementation objective, not a trust guarantee. Even a successful pilot cannot eliminate common-mode model errors, collusion, compromised infrastructure, or inadequate scientific criteria.

## Standards we can build on

[W3C PROV](https://www.w3.org/TR/prov-overview/) supplies a vocabulary for entities, activities, and responsibility. [SLSA provenance](https://slsa.dev/spec/v1.2/provenance) describes verifiable information about how software artifacts were produced. [Sigstore's verification guidance](https://docs.sigstore.dev/cosign/verifying/verify/) makes identity and issuer checks concrete. These are building blocks; this proposal does not claim their implementation or conformance, and none substitutes for scientific review.
