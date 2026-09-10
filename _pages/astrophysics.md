---
layout: page
title: Astrophysics
permalink: /astrophysics/
nav: true
nav_order: 1
---

Astrophysics is the primary research lane: gravitational-wave astronomy, compact binaries, simulations, and related multi-messenger questions.

<p><a href="{{ '/astrophysics/feed.xml' | relative_url }}">RSS feed</a> · <a href="{{ '/ai-agents/' | relative_url }}">AI, agents & reproducibility lane</a></p>

{% for post in site.posts %}{% unless site.data.lane_posts.ai contains post.slug or post.external_source != nil %}<article><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2><p><small>{{ post.date | date: '%B %-d, %Y' }}</small></p>{% if post.description %}<p>{{ post.description }}</p>{% endif %}</article>{% endunless %}{% endfor %}

<p><small>Explore the group’s research notes and project updates, with links to the AI and reproducibility lane where the topics overlap.</small></p>
