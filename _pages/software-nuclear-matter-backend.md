---
layout: research
title: NuclearMatter-Backend
description: Open research software connecting nuclear equations of state, neutron-star structure, tidal observables, and inference.
permalink: /software/nuclear-matter-backend/
---

<div class="research-hero research-hero-compact">
  <p class="research-eyebrow">Software contribution / Nuclear astrophysics</p>
  <h1>From nuclear matter<br>to observable stars.</h1>
  <p class="research-lead">NuclearMatter-Backend connects models of dense matter to neutron-star structure, tidal deformability, and statistical inference.</p>
  <p class="research-intro">The contribution is reusable research infrastructure: interchangeable equations of state, selected differentiable calculations, reference comparisons, and interfaces that connect nuclear physics to gravitational-wave analysis.</p>
  <nav class="research-actions" aria-label="Nuclear backend resources">
    <a class="research-primary-link" href="https://github.com/oshaughnessy-junior/NuclearMatter-Backend">Public source</a>
    <a href="https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/README.md">Documentation &amp; installation</a>
    <a href="{{ '/repositories/' | relative_url }}">Software ecosystem</a>
  </nav>
</div>

## Connecting laboratory and astrophysical questions

Neutron-star observations and laboratory measurements probe complementary aspects of dense matter. [Huth and collaborators (2022)](https://arxiv.org/abs/2107.06229) demonstrate a joint analysis combining heavy-ion collisions, microscopic theory, and astrophysical observations. NuclearMatter-Backend supplies components for investigating connections of this kind; it does not claim to reproduce that analysis merely by providing the tools.

The central path runs from **nuclear parameters or an imported EOS → stellar structure and tides → mass–radius–deformability sequences → inference interfaces**. Researchers can vary the physical model, inspect its numerical representation, and carry selected sensitivities through the calculation.

## Models, solvers, and inference

**Multiple descriptions of dense matter.** The EOS layer includes empirical-parameter metamodels, relativistic mean-field models, Skyrme and density-dependent RMF implementations, hybrid phase-transition models, polytropes, and tabular/CompOSE readers. Crust and composition utilities help assemble stellar inputs. The metamodel follows the scientific framework of [Margueron, Hoffmann Casali & Gulminelli (2018)](https://arxiv.org/abs/1708.06894). Inclusion of a model family does not guarantee physical admissibility for every parameter choice; for example, the Skyrme implementation documents high-density causality and effective-mass limitations. See the [EOS source](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/tree/main/src/nmbackend/eos).

**Stellar structure and tides.** An adaptive enthalpy-domain solver integrates the Tolman–Oppenheimer–Volkoff equations and tidal perturbations, producing mass, radius, and tidal deformability. The tidal calculation builds on [Hinderer (2008)](https://arxiv.org/abs/0711.2420) and [Damour & Nagar (2009)](https://arxiv.org/abs/0906.0096). JAX and diffrax support selected automatic-differentiation paths; an independent radius-domain SciPy solver provides a numerical reference. Forward-mode derivatives are supported along documented paths, while higher derivatives and reverse-mode tidal calculations have restrictions. These distinctions matter when selecting an inference method.

**Priors and sensitivities.** The repository implements a constrained bridge prior between low-density nuclear matter and a high-density endpoint, compressed EOS sequences, and a Gaussian coefficient prior. Its Fisher utilities compute fixed-mass sensitivities and maximum-mass derivatives. These are tools for exploring assumptions and information content, not a claim that a particular prior is observationally established. See the [prior implementations](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/tree/main/src/nmbackend/priors) and [sensitivity calculations](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/src/nmbackend/inference/fisher.py).

**Interfaces to data analysis.** Implemented RIFT support includes an `EOSConcrete`-compatible adapter and tabular sequence generation, reading, and compression. The [RIFT pipeline notes](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/docs/rift-tabular-pipeline.md) explain the integration. The laboratory-likelihood layer includes density-tagged pressure constraints and correlated symmetry-energy parameters, with explicit treatment of a transport-model systematic. Its FRIB scenario ladder represents assumed forecast scenarios. A gwkokab adapter remains planned; it should not be confused with the implemented RIFT interface.

## Cooling and rotation extensions

Separate interfaces connect to external NSCool and a pinned RNS reference implementation; neither upstream code is bundled as an original contribution of this project. The rotating path includes a tabulated EOS adapter and recorded forward comparisons. A JAX thermal-transport implementation explores diffusion on supplied stellar backgrounds. [Beznogov and collaborators (2023)](https://arxiv.org/abs/2206.04539) provide relevant primary work on two-dimensional rotating-star cooling.

These extensions open useful comparisons between EOS, structure, and thermal calculations. Their present scope is narrower than a fully coupled rotating-star evolution model: fixed-background thermal calculations do not include an EOS-to-equilibrium response, and a forward rotating comparison is not a convergence or stability certification. Follow the [cooling notes](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/src/nmbackend/cooling/README.md), [thermal validation record](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/docs/cooling/core_transport_validation.md), and [tabulated rotating-star documentation](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/docs/rotating-tabulated.md) for supported cases and external dependency terms.

## Evidence and current scope

The repository records internal solver checks, gradient comparisons, and external reference comparisons. Its [June interpolation study](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/09ca68034bb51e7e5d5b33e371d8242805bc20a1/docs/devlog/2026-06-02f-consistent-interpolation.md) reports that surface and interpolation corrections reduced an earlier radius discrepancy to approximately 3–10 metres against RePrimAnd 1.7. This is a documented comparison for the studied cases, not a universal accuracy guarantee. The README separately reports agreement with the in-process SciPy reference.

A recorded [RIFT integration smoke test](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/examples/gw170817_tabular/SMOKE_TEST_RESULT.md) exercises the interface but explicitly uses remapped EOS indices; it is not a scientific posterior or evidence result. Disconnected stable branches and some adapter paths also remain limited. This page describes inspected source and project-reported checks; it does not report a freshly executed scientific validation suite.

## Reuse and collaboration

The package is MIT-licensed and credits R. O’Shaughnessy and the RIT CCRG nuclear-matter group. Its [attribution record](https://github.com/oshaughnessy-junior/NuclearMatter-Backend/blob/main/ATTRIBUTION.md) distinguishes original implementation, scientific methods, external reference codes, and reused data. Cite the relevant primary work as well as the software when building on it.

Useful collaborations include independent cross-code benchmarks, laboratory-likelihood development, robust phase-transition inference, and reproducible connections between nuclear theory and gravitational-wave analysis. These offer concrete entry points for academic, national-laboratory, and scientific-computing partners.

[Discuss a research collaboration]({{ '/contact/' | relative_url }}) · [Related astrophysics work]({{ '/astrophysics/' | relative_url }})

<p class="software-caption">Source reviewed 9 November 2026 at <a href="https://github.com/oshaughnessy-junior/NuclearMatter-Backend/tree/09ca68034bb51e7e5d5b33e371d8242805bc20a1">09ca680</a>. Consult current documentation and tests before selecting a model, derivative path, or external interface.</p>
