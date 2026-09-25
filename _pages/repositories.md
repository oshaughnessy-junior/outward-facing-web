---
layout: research
permalink: /repositories/
title: Software ecosystem
nav_title: Software
description: How our contributions to RIFT, kilonova modeling, public inference data, workflow integration, and agent verification connect.
nav: true
nav_order: 5
---

<header class="research-hero research-hero-compact">
  <p class="research-eyebrow">Open research / Code, models &amp; evidence</p>
  <h1>Software that connects<br>questions to evidence.</h1>
  <p class="research-lead">Our contribution is an ecosystem: inference methods, physical models, reusable results, and the infrastructure that makes the work inspectable.</p>
  <p class="research-intro">The group develops and contributes to collaborative scientific software. Some projects are inference engines; others connect tools, release data, teach methods, or test how agents can produce verifiable research. Each has a different role.</p>
</header>

<section class="software-map" aria-labelledby="software-map-title">
  <h2 id="software-map-title">How the pieces fit</h2>
  <ol class="software-flow">
    <li><a href="#models-data">Physical models</a><span>Signals &amp; kilonova surrogates</span></li>
    <li><a href="#inference">Inference</a><span>RIFT &amp; LISA-RIFT</span></li>
    <li><a href="#workflows">Workflow &amp; reporting</a><span>Adapters, tutorials &amp; operating knowledge</span></li>
    <li><a href="#models-data">Reusable evidence</a><span>Samples, likelihoods &amp; paper releases</span></li>
  </ol>
  <p class="software-foundation"><a href="#agents-trust">Experimental foundation: campaign contracts + publication &amp; verification</a><br>Make evaluations traceable, consolidation replayable, and claims independently checkable.</p>
  <p class="software-caption">A map of contribution roles, not a claim that every project is already integrated into one pipeline.</p>
</section>

<nav class="software-start" aria-label="Choose a software starting point">
  <h2>Start with your task</h2>
  <ul>
    <li><a href="#inference">Run or extend gravitational-wave inference</a></li>
    <li><a href="#models-data">Model a counterpart or reuse published samples</a></li>
    <li><a href="#workflows">Learn a workflow or connect analysis to reporting</a></li>
    <li><a href="#agents-trust">Build agent workflows with inspectable evidence</a></li>
  </ul>
</nav>

{% for group in site.data.software %}

<section class="software-category" aria-labelledby="{{ group.id }}">
  <h2 id="{{ group.id }}">{{ group.title }}</h2>
  <p>{{ group.description }}</p>
  <div class="software-grid">
  {% for item in group.entries %}
    <article class="software-card">
      <p class="research-eyebrow">{{ item.role }}</p>
      <h3><a href="{{ item.url }}">{{ item.name }}</a></h3>
      <p>{{ item.purpose }}</p>
      <dl>
        <dt>Contribution</dt><dd>{{ item.contribution }}</dd>
        <dt>Connection</dt><dd>{{ item.connection }}</dd>
      </dl>
      <p class="software-status">{{ item.status }}</p>
      <p class="software-links"><a href="{{ item.url }}">{{ item.link_label }} <span aria-hidden="true">↗</span></a>{% if item.related_url %}<a href="{{ item.related_url }}">{{ item.related_label }} <span aria-hidden="true">↗</span></a>{% endif %}</p>
    </article>
  {% endfor %}
  </div>
</section>
{% endfor %}

<aside class="research-disclosure">
  <h2>Credit, reuse, and contribution</h2>
  <p>Follow each project's source for its license, citation instructions, maintainers, and contribution process. A development fork is not evidence of upstream authorship. A public prototype is not evidence of adoption or validated science. These descriptions distinguish group contributions, collaborative work, and independently maintained upstream tools.</p>
  <p>AI agents help write code, organize evidence, and maintain documentation in parts of this ecosystem. Consult each project's provenance and review records; AI participation and publication do not establish independent validation. <a href="{{ '/publication-policy/' | relative_url }}">Our authorship and verification policy</a> explains the distinction.</p>
  <p>Curated from public project documentation on 25 September 2026. Explore the <a href="{{ '/astrophysics/' | relative_url }}">science questions</a> and the <a href="{{ '/ai-agents/' | relative_url }}">agent and trust objectives</a> behind this work.</p>
</aside>
