---
layout: research
title: Research overview
description: Selected academic contributions in gravitational-wave inference, accelerated scientific computing, multimessenger models, and accountable AI research workflows.
permalink: /research/
---

<div class="research-hero research-hero-compact">
  <p class="research-eyebrow">Richard O’Shaughnessy · Rochester Institute of Technology</p>
  <h1>From physical questions<br>to reusable research.</h1>
  <p class="research-lead">Gravitational-wave astrophysics is our core. Inference, simulation, and scientific software connect the observations to the physics.</p>
  <p class="research-intro">This overview connects selected contributions to their primary papers and public research outputs. Our second lane explores how AI agents can help conduct research with inspectable evidence and accountable review.</p>
  <nav class="research-actions" aria-label="Academic record">
    <a class="research-primary-link" href="{{ '/cv/' | relative_url }}">Richard’s CV</a>
    <a href="{{ '/publications/' | relative_url }}">Full bibliography</a>
    <a href="{{ '/people/' | relative_url }}">Team &amp; alumni</a>
    <a href="{{ '/contact/' | relative_url }}">Research contact</a>
  </nav>
</div>

<section aria-labelledby="contributions-heading">
  <h2 id="contributions-heading">Selected contributions</h2>
  <div class="software-grid">
    <article class="software-card">
      <p class="research-eyebrow">Astrophysics / Inference</p>
      <h3>RIFT: inference with detailed physical models</h3>
      <p>RIFT uses iterative likelihood fitting to infer compact-binary parameters. The foundational study compares its results with LALInference; subsequent work examines algorithm choices, robustness, and performance. These are collaborative methods and software contributions.</p>
      <p><a href="https://arxiv.org/abs/1805.10457">Lange, O’Shaughnessy &amp; Rizzo (2018)</a> · <a href="https://arxiv.org/abs/2210.07912">Wofford et al. (2023)</a></p>
      <p class="software-status">Primary papers + research software</p>
      <p class="software-links"><a href="https://git.ligo.org/rapidpe-rift/rift">Official RIFT source</a><a href="https://github.com/oshaughn/RIFT_pe_public_samples">Public inference products</a></p>
    </article>
    <article class="software-card">
      <p class="research-eyebrow">Scientific computing / GPUs</p>
      <h3>Reducing inference cost and latency</h3>
      <p>Wysocki and collaborators translate parts of the RIFT likelihood calculation to GPUs and evaluate the resulting performance. The paper includes a collaboration with Brookhaven National Laboratory and provides a concrete entry point into our accelerated scientific-computing work.</p>
      <p><a href="https://arxiv.org/abs/1902.04934">Wysocki et al., Physical Review D (2019)</a></p>
      <p class="software-status">Published performance study</p>
      <p class="software-links"><a href="https://github.com/oshaughn/ILE-GPU-Paper">Paper source &amp; examples</a><a href="{{ '/repositories/' | relative_url }}#inference">Inference software</a></p>
    </article>
    <article class="software-card">
      <p class="research-eyebrow">Multimessenger astrophysics / Models</p>
      <h3>Connecting merger ejecta to kilonova light</h3>
      <p>Kedia and collaborators construct surrogate light curves from simulations and apply them to AT2017gfo. The study examines how outflow assumptions and modeling uncertainties affect the inferred ejecta properties.</p>
      <p><a href="https://arxiv.org/abs/2211.04363">Kedia et al., Physical Review Research (2023)</a></p>
      <p class="software-status">Published modeling and inference study</p>
      <p class="software-links"><a href="https://github.com/markoris/surrogate_kne">Surrogate code &amp; notebooks</a><a href="{{ '/repositories/' | relative_url }}#models-data">Models &amp; data</a></p>
    </article>
    <article class="software-card">
      <p class="research-eyebrow">Research practice / AI agents</p>
      <h3>Inspectable experiments in agent coordination</h3>
      <p>Public prototypes explore evaluation records, replayable campaign updates, and evidence-linked review. They expose code, examples, and limitations so collaborators can investigate the mechanisms. MCRP remains a research proposal and prototype; published physics results and validated agent capabilities require their own evidence.</p>
      <p><a href="https://github.com/oshaughnessy-junior/inference-campaign-contracts">Campaign contracts: source and fixtures</a> · <a href="https://github.com/oshaughnessy-junior/trust-and-review-papers">Trust and review: research dossier</a></p>
      <p class="software-status">Experimental research software</p>
      <p class="software-links"><a href="{{ '/ai-agents/' | relative_url }}">AI research lane</a><a href="{{ '/publication-policy/' | relative_url }}">Authorship &amp; verification policy</a></p>
    </article>
  </div>
</section>

<section class="research-disclosure" aria-labelledby="collaboration-heading">
  <h2 id="collaboration-heading">Connect with the work</h2>
  <p>For academic colleagues, the <a href="{{ '/cv/' | relative_url }}">CV</a>, <a href="{{ '/publications/' | relative_url }}">bibliography</a>, and <a href="{{ '/people/' | relative_url }}">team and alumni</a> provide the wider research and mentoring context.</p>
  <p>For AI labs and research partners, the public agent prototypes offer concrete starting points for discussing reproducibility, evaluation, and coordination. For national-laboratory and scientific-computing collaborators, the inference and modeling studies connect accelerator computing, uncertainty, and physical simulation.</p>
  <p><a href="{{ '/contact/' | relative_url }}">Contact Richard about a research collaboration</a>. A useful starting message identifies the scientific question, the relevant paper or repository, and the proposed contribution.</p>
</section>

<p>Selected examples, rather than a complete publication list. Follow the primary papers for author credit, methods, assumptions, and the scope of each result. See the <a href="{{ '/astrophysics/' | relative_url }}">astrophysics lane</a> for research notes and the <a href="{{ '/repositories/' | relative_url }}">software ecosystem</a> for additional projects.</p>
