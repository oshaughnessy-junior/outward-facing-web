---
layout: page
title: AI, Agents & Reproducibility
nav_title: AI & Agents
permalink: /ai-agents/
nav: true
nav_order: 2
---

This lane covers agent teams, workflow design, infrastructure, and computational reproducibility. It is written for researchers and builders interested in how AI systems can support careful, reviewable work.

<p><a href="{{ '/ai-agents/feed.xml' | relative_url }}">RSS feed</a> · <a href="{{ '/astrophysics/' | relative_url }}">Astrophysics lane</a></p>

{% for post in site.posts %}{% if site.data.lane_posts.ai contains post.slug and post.external_source == nil %}<article><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p><small>{{ post.date | date: '%B %-d, %Y' }}</small></p>{% if post.description %}<p>{{ post.description }}</p>{% endif %}</article>{% endif %}{% endfor %}

<p><small>MCRP is the Minimum Credible Reproducibility Protocol, a design proposal for binding computational claims and their review to a specific release. See the introductory post for its stated scope and limitations, then <a href="https://github.com/oshaughnessy-junior/outward-facing-web/issues">share a worked record or specific critique</a> in the existing issue discussion.</small></p>
