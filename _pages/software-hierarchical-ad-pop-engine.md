---
layout: research
title: Hierarchical AD population engine
description: Differentiable compact-binary population modeling, from merger environments to a gwkokab-compatible rate distribution.
permalink: /software/hierarchical-ad-pop-engine/
---

<div class="research-hero research-hero-compact">
  <p class="research-eyebrow">Software contribution / Compact-binary populations</p>
  <h1>From merger environments<br>to population inference.</h1>
  <p class="research-lead"><code>hierarchical_AD_pop_engine</code> is a JAX-based research prototype for connecting hierarchical black-hole merger models to gravitational-wave population inference.</p>
  <p class="research-intro">The contribution is a composable model: describe what one environment produces, describe how environments form, and combine them into a rate distribution that an inference framework can evaluate.</p>
  <nav class="research-actions" aria-label="Population engine resources">
    <a class="research-primary-link" href="https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine">Public source</a>
    <a href="https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine/blob/main/README.md">Usage &amp; installation</a>
    <a href="{{ '/repositories/' | relative_url }}">Software ecosystem</a>
  </nav>
</div>

## The scientific connection

A retained black-hole merger remnant can participate in later mergers, changing the population of masses and spins. [Doctor, Wysocki, O’Shaughnessy, Holz & Farr (2020)](https://arxiv.org/abs/1911.04424) developed a modular coagulation framework for modeling these populations. This repository builds on that line of work with differentiable numerical components and an inference interface. The earlier paper establishes the scientific foundation; it does not validate every feature of this implementation.

## What the software contributes

- **Environment response.** Natal mass and spin distributions, pairing kernels, remnant prescriptions, and recoil-based retention feed a compact-binary merger model. The response layer contains a truncated generational solver and an alternative implicit fixed-point solver with a custom reverse-mode derivative.
- **Formation and assembly.** `FormationRate` separates the distribution of environments from their merger response. `SyntheticUniverse` combines them by quadrature. A single-environment construction provides a useful consistency check on the composition.
- **Inference interface.** A NumPyro distribution evaluates the joint mass, spin, and redshift rate density. The `coagulation_model` factory packages it as a gwkokab `ScaledMixture`; source tests exercise construction, JIT evaluation, and selected parameter gradients. See the [architecture](https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine/blob/main/DESIGN.md) and [integration tests](https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine/blob/main/tests/test_gwkokab_integration.py).

The repository also contains per-event normal-approximate-likelihood preparation tools, following [Delfavero and collaborators](https://arxiv.org/abs/2107.13082). Those scripts have environment-specific inputs; publishing the software does not make their external input datasets available.

## Status and useful limits

This is research software, with package version `0.0.1` at the reviewed revision. The supplied tests cover limiting cases, composition, finite-difference comparisons, and integration behavior; this page reports source contents, not a newly executed scientific validation suite.

The default response is the perturbative solver. The implicit solver is a separate response-layer option with different convergence and differentiation considerations. The aligned-spin retention model uses a hard threshold, so gradients with respect to escape velocity vanish almost everywhere. An automatic-differentiation implementation therefore does not make every physical parameter smoothly inferable. Consult the [response implementation](https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine/tree/main/src/hierarchical_ad_pop_engine/response), [retention implementation](https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine/blob/main/src/hierarchical_ad_pop_engine/retention.py), and current tests before choosing a solver or parameterization.

## Reuse and collaboration

Start with the README example and a small-grid calculation. Useful contributions include independently reproduced solver comparisons, convergence checks across physical regimes, and additional environment-response models. Credit the underlying methods, gwkokab, and the repository contributors when using this work.

[Discuss a research collaboration]({{ '/contact/' | relative_url }}) · [Related astrophysics work]({{ '/astrophysics/' | relative_url }})

<p class="software-caption">Source reviewed 9 November 2026 at <a href="https://github.com/oshaughnessy-junior/hierarchical_AD_pop_engine/tree/d789282">d789282</a>. Check the repository for current implementation, licensing metadata, and citation guidance.</p>
