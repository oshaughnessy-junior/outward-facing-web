---
layout: post
title: "McFACTS IV: Hunting for Light from Black Hole Collisions"
date: 2026-05-07 12:00:00 -0400
author: "you"
parent_issue: 18
categories: [research]
---

**Title:** McFACTS IV: Electromagnetic Counterparts to AGN Disk Embedded Binary Black Hole Mergers

**Bibcode:** 2026arXiv260204135M

**Link:** [Read on arXiv](https://arxiv.org/abs/2602.04135)

---

When black holes collide, they释放 gravitational waves that LIGO, Virgo, and KAGRA can detect. But can we see anything else? Some collisions should produce bursts of light — electromagnetic signals that tell us about the environment where the merger happened.

This new paper, led by a CUNY graduate student (Emily McPike), focuses on one special scenario: black hole pairs embedded in the disks of active galactic nuclei (AGN). Unlike most black hole merger environments, these disks offer a unique possibility: gas around the merger site could produce observable light.

**The problem:** We haven't had good ways to predict what those light signals would look like, or which mergers we'd actually be able to see.

**The solution:** This paper uses [McFACTS](https://www.github.com/mcfacts/mcfacts) — Monte Carlo For AGN Channel Testing and Simulation — to model both the gravitational-wave signals *and* the light we'd expect from these mergers.

Key findings:

1. **Migration traps** in dense AGN disks efficiently grow black holes and produce high-mass, fast-spinning remnants that can power observable light across multiple merger generations.

2. **Mass threshold:** Mergers in dense disks with chirp mass ≳ 40 solar masses are highly likely to produce observable light, provided the disks live long enough and the initial black hole mass distribution is top-heavy.

---

### For those who want more

This work integrates bolometric EM luminosity predictions directly into the McFACTS framework, providing a statistical bridge between gravitational-wave detections and electromagnetic follow-up. Previous McFACTS papers established the core methodology:

- **McFACTS I** ([2025ApJ...990..217M](https://ui.adsabs.harvard.edu/abs/2025ApJ...990..217M)) — Original Monte Carlo framework for testing the AGN channel against LVK data
- **McFACTS II** ([2025ApJ...993..163C](https://ui.adsabs.harvard.edu/abs/2025ApJ...993..163C)) — Mass ratio and effective spin relationships
- **McFACTS III** ([2025ApJ...989...67D](https://ui.adsabs.harvard.edu/abs/2025ApJ...989...67D)) — Statistical baseline for binary mergers

The primary contribution here is the new capability to simultaneously generate GW observables and their corresponding EM luminosities, enabling real-time selection of counterpart candidates for time-domain surveys like ZTF and LSST.