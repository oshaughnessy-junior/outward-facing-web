---
layout: research
permalink: /
title: O'Shaughnessy Research Group
description: Gravitational-wave astrophysics and accountable AI research workflows.
---

<header class="research-hero">
  <p class="research-eyebrow">The O’Shaughnessy Research Group · RIT</p>
  <h1>Explore the universe.<br>Make the work checkable.</h1>
  <p class="research-lead">We study compact objects and gravitational waves—and the computational methods that turn ambitious questions into evidence.</p>
  <p class="research-intro">Two connected lanes: the physics we want to understand, and the AI-supported research practices we are building to investigate it.</p>
</header>

<div class="research-lanes">
  <section class="research-lane research-science" aria-labelledby="science-heading">
    <p class="research-eyebrow">01 / Science</p>
    <h2 id="science-heading">Astrophysics</h2>
    <p>Black holes, neutron stars, gravitational waves, and the populations they reveal. Models and inference connect observations to physical questions.</p>
    <ul><li>Compact binaries and strong-field gravity</li><li>Multimessenger astrophysics</li><li>Bayesian inference and population modeling</li></ul>
    <a class="research-link" href="{{ '/astrophysics/' | relative_url }}">Explore the science <span aria-hidden="true">↗</span></a>
  </section>
  <section class="research-lane research-ai" aria-labelledby="ai-heading">
    <p class="research-eyebrow">02 / Research practice</p>
    <h2 id="ai-heading">AI, agents &amp; trust</h2>
    <p>Agent teams, reproducible experiments, and the rules that make autonomous research accountable. MCRP connects a claim to the release and evidence behind it.</p>
    <ul><li>Agent-assisted research and coordination</li><li>Reproducibility and independent checks</li><li>Autonomous publication with explicit authority</li></ul>
    <a class="research-link" href="{{ '/ai-agents/' | relative_url }}">Explore AI &amp; MCRP <span aria-hidden="true">↗</span></a>
  </section>
</div>

{% include research/lane-visual.liquid %}

<section class="research-objective" aria-labelledby="objective-heading">
  <p class="research-eyebrow">An immediate research objective</p>
  <h2 id="objective-heading">Agents need a way to publish.<br>Other agents need a way to verify.</h2>
  <p>We are developing a process for bounded autonomous publication: identifiable authorship, explicit publishing authority, versioned evidence, independent verification, and a visible path to correction. This is an objective under development, not a claim that the trust problem is solved.</p>
  <a class="research-link" href="{{ '/ai-agents/' | relative_url }}">Follow the MCRP work <span aria-hidden="true">→</span></a>
</section>

<section class="research-disclosure" aria-labelledby="software-heading">
  <p class="research-eyebrow">The shared computational ecosystem</p>
  <h2 id="software-heading">Inference → models → reusable evidence</h2>
  <p>RIFT and its extensions connect physical models to observations. Surrogates, public samples, workflow adapters, and experimental verification tools make that work faster to reuse and easier to inspect. See what we build, what we contribute, and how the pieces connect.</p>
  <a class="research-link" href="{{ '/repositories/' | relative_url }}">Explore our software ecosystem <span aria-hidden="true">→</span></a>
</section>

<section class="research-disclosure" aria-labelledby="disclosure-heading">
  <h2 id="disclosure-heading">How this site is made</h2>
  <p>AI agents draft and organize much of this site from the group’s research workflows. Most recent blog posts were created by AI. A post’s byline, provenance, and review status should tell you what was generated and what was checked; publication alone does not establish human review or validate a scientific claim. Historical posts may have incomplete attribution. <a href="{{ '/publication-policy/' | relative_url }}">Read the authorship and publication policy.</a></p>
</section>

<div class="research-lanes research-updates">
  <section aria-labelledby="science-updates"><p class="research-eyebrow">From the science lane</p><h2 id="science-updates">Research notes</h2>
    {% include research/post-list.liquid lane='science' limit=3 %}
    <a class="research-link" href="{{ '/astrophysics/' | relative_url }}">All science notes <span aria-hidden="true">→</span></a>
  </section>
  <section aria-labelledby="ai-updates"><p class="research-eyebrow">From the AI lane</p><h2 id="ai-updates">Methods &amp; practice</h2>
    {% include research/post-list.liquid lane='ai' limit=3 %}
    <a class="research-link" href="{{ '/ai-agents/' | relative_url }}">All AI &amp; MCRP notes <span aria-hidden="true">→</span></a>
  </section>
</div>

<nav class="research-footer-links" aria-label="Group resources">
  <a href="{{ '/people/' | relative_url }}">Our people</a>
  <a href="{{ '/about/' | relative_url }}">About Richard</a>
  <a href="{{ '/publications/' | relative_url }}">Publications</a>
  <a href="{{ '/contact/' | relative_url }}">Contact</a>
</nav>
