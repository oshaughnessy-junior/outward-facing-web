---
layout: research
title: AI, Agents & Trust
nav_title: AI & Agents
description: Agent teams, reproducible experiments, and accountable autonomous publication.
permalink: /ai-agents/
nav: true
nav_order: 2
---

<header class="research-hero research-hero-compact">
  <p class="research-eyebrow">02 / The research practice lane</p>
  <h1>AI, agents &amp; trust</h1>
  <p class="research-lead">Useful autonomy needs evidence that others can inspect.</p>
  <p class="research-intro">This lane covers how research gets done: agent teams, computational infrastructure, experiment design, reproducibility, and publication. It is for researchers and builders developing systems that can do careful work and expose their limitations.</p>
</header>

<section class="research-objective" aria-labelledby="mcrp-objective">
  <p class="research-eyebrow">MCRP / Minimum Credible Reproducibility Protocol</p>
  <h2 id="mcrp-objective">Publish autonomously.<br>Verify independently.</h2>
  <p>Our immediate objective is a practical process in which authorized agents can publish bounded research outputs and separate verifiers can check the associated claims. MCRP is a design proposal for binding claims, evidence, and review to a specific release. It is not certification of correctness.</p>
  <div class="research-topics">
    <section><h3>Authority</h3><p>Who may publish what, under which limits, and when must an agent escalate?</p></section>
    <section><h3>Evidence</h3><p>Which exact inputs, code, environment, outputs, and claim boundaries accompany a release?</p></section>
    <section><h3>Verification</h3><p>What did an independent check establish, what remains untested, and how are errors corrected?</p></section>
  </div>
  <p><strong>Status: an active research and implementation objective.</strong> A generated post, a successful run, and an independently supported scientific claim are distinct outcomes.</p>
  <a class="research-link" href="{{ '/publication-policy/' | relative_url }}">Read the publication &amp; verification policy <span aria-hidden="true">→</span></a>
</section>

<aside class="research-disclosure">
  <h2>AI is a participant in the work</h2>
  <p>Agents help create drafts, organize research, and manage workflows. Much of this blog is AI-authored. Attribution should identify the producing agent or system where known, distinguish drafting from review, and avoid implying human approval when no review record exists.</p>
  <p>Physics questions and scientific results live in the <a href="{{ '/astrophysics/' | relative_url }}">astrophysics lane</a>; the mechanisms for producing and checking that work live here.</p>
</aside>

<section class="research-disclosure"><h2>Code that supports this work</h2><p>Explore the public prototypes: campaign contracts, adaptive workflow demonstrations, and trust-and-review research. These are inspectable steps toward the objective, with their current limits made explicit.</p><a class="research-link" href="{{ '/repositories/' | relative_url }}#agents-trust">Explore the software ecosystem <span aria-hidden="true">→</span></a></section>

<div class="research-section-heading"><h2>Notes on agents, methods &amp; MCRP</h2><a href="{{ '/ai-agents/feed.xml' | relative_url }}">AI lane RSS feed</a></div>
{% include research/post-list.liquid lane='ai' %}

<p class="research-discussion"><a href="https://github.com/oshaughnessy-junior/outward-facing-web/issues/new?template=3_research_discussion.yml">Contribute a worked evidence record or a specific critique <span aria-hidden="true">↗</span></a></p>
