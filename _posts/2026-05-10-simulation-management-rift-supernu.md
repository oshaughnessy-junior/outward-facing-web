---
layout: post
title: "Simulation Management Beyond Run and Hope: Adaptive Placement, Archiving, and SuperNu as a Realization"
date: 2026-05-10 10:53:00 -0400
author: "Richard"
categories: [research]
---

# Simulation Management Beyond "Run and Hope": Adaptive Placement, Archiving, and SuperNu as a Realization

**Status:** Draft v3 — added motivation section per Richard's guidance
**Date:** 2026-05-10
**Authors:** Junior (drafting), based on research by coding-rift and code-op-astro agents

---

## Motivation: Why Simulation Management Is a First-Class Problem

The traditional approach to simulation-driven science treats each simulation as an independent event: write the input, submit the job, wait for the output, move on. This works when simulations are few and the parameter space is small. It breaks down as workflows scale.

**The placement problem.** Gravitational wave parameter estimation involves exploring high-dimensional parameter spaces with expensive simulations. Numerical relativity (NR) waveforms — the gold standard for accuracy — take weeks to generate on hundreds of cores. Simply throwing compute at the problem is not sustainable. The question isn't just "can we run more simulations?" but "which simulations *should* we run, and where?" Adaptive placement answers that by using prior results and workflow structure to guide decisions — routing new simulations to the nodes or backends best suited to the current state of the analysis.

**The archiving problem.** Even when simulations are run well, the outputs are often lost to "ad-hoc directory structures and institutional memory." Six months later, recreating what was done, why, and what the results meant is archaeology, not science. The cost of re-running simulations — in compute, time, and reproducibility — makes proper archiving a prerequisite for long-term scientific productivity, not an afterthought.

**The connection to gravitational wave science.** These problems are amplified in GW parameter estimation, where:

- The parameter space is high-dimensional and structured (masses, spins, eccentricity, sky location, distance).
- Each simulation is expensive (NR waveforms, kilonova light curves, GRMHD merger simulations).
- Results must be reused across analyses (waveform catalogs, surrogate models, population inference).
- New LIGO/Virgo/Kamioka triggers demand rapid response — the system must route work efficiently without manual intervention.

Our group has pioneered adaptive simulation placement across several projects: targeted NR waveform banks for eccentric GW events (GW200208_22, GW200105), NRHybSur3dq8 surrogates for fast LISA/RIFT parameter estimation, and synthetic population validation to expose biases from circular-only PE. The same philosophy — placing simulations deliberately in parameter space to maximize information gain — extends naturally to kilonova radiative transfer (via SuperNu) and, in time, to GRMHD simulations of mergers with matter.

---

## The Problem: Simulations Are Cheap to Start, Hard to Manage

Running a simulation is easy. Running *the right* simulation, in *the right place*, at *the right time*, and then *finding it again six months later* — that's hard. As simulation workflows grow in complexity, the gap between "submitting a job" and "getting useful science out of the output" widens. Two concepts help close that gap: **adaptive simulation placement** and **simulation archiving**. The RIFT Simulation Manager API provides a framework for both; SuperNu provides a concrete implementation.

---

## Adaptive Simulation Placement

**What it means:**
Adaptive placement is about choosing *where* a simulation runs and *how* it's configured based on available resources, prior results, and the structure of the parameter space. Instead of manually matching simulations to machines or tuning parameters by hand, the system reasons about the workflow as a whole.

**Where it lives in RIFT:**
The RIFT Simulation Manager provides a structured backend API (`gw_pe_synthetic`) that decouples simulation logic from execution details. Backends can implement custom placement strategies — deciding which nodes to use, how to partition the workload, and when to adaptively refine parameter estimates.

**Why it matters:**
Parameter estimation for gravitational wave events involves exploring high-dimensional spaces with expensive simulations. Adaptive placement keeps the pipeline responsive: new LIGO/Virgo triggers can be routed efficiently, and intermediate results can guide where to invest the next round of compute.

---

## Simulation Archiving

**What it means:**
Archiving isn't just "saving the output" — it's about preserving *provenance*, *provenance chains*, and *searchability*. When a simulation is archived properly, future users (or future versions of yourself) can understand exactly what was run, why, and what the results mean — without hunting through ad-hoc directory structures.

**Where it lives in RIFT:**
The Simulation Manager's documentation system encodes this philosophy. `DESIGN.md` serves as the single source of truth; automated Sphinx tooling converts it to documentation on every build. The `backends/` tree records the full API surface, making it auditable and discoverable.

---

## The Simulation Manager API: A Common Interface

The real power of the RIFT Simulation Manager isn't just the backends themselves — it's the **API contract**. Any code that implements the simulation manager interface can slot into the same workflow: RIFT's parameter estimation, downstream analysis, archiving, and reuse. This means:

- New simulation backends can be dropped in without rewriting the workflow.
- Results from different codes can be compared in a common framework.
- The system can reason about *where* a given simulation fits in the overall pipeline.

---

## SuperNu as a Realization of the API

**What is SuperNu?**
SuperNu is a Monte Carlo radiative transfer code (Fortran, LANL) that simulates time-dependent radiation transport in matter — the physics that determines what a supernova or kilonova *looks like* to an observer.

**How it fits the pattern:**
SuperNu isn't just a physics code someone wrote — it's a concrete realization of the simulation manager concept:

1.  **It implements a simulation interface** — SuperNu can be treated as a backend that takes structured input (density, velocity, composition from a hydro simulation) and produces structured output (light curves, spectra).
2.  **It enables adaptive post-processing** — Different radiation transport strategies can be explored without re-running the underlying hydro.
3.  **It feeds the archival pipeline** — Its output is exactly the kind of thing that needs to be preserved with full provenance: *this* input model produced *this* observable signature.

**Technical details:**
- Implements Implicit Monte Carlo (IMC) and Discrete Diffusion Monte Carlo (DDMC) methods
- Multi-frequency opacities: Thomson scattering, bound-bound, bound-free, free-free
- 1D/2D/3D geometries, static or homologously expanding grids
- Hybrid MPI + OpenMP parallelization
- **Output:** Light curves and spectra — the observables that connect simulation to observation

**Why users care:**
When a gravitational wave event triggers follow-up observations, the chain from "detection" to "physical interpretation" runs through radiative transfer. SuperNu gives that chain a concrete form: take the output of a hydro simulation, feed it through the radiation transport layer, and get predictions for what JWST or other instruments should see. Making that pipeline explicit — via a simulation manager API — is what turns "we ran some code" into reproducible science.

---

## How They Relate

| Aspect | RIFT Simulation Manager API | SuperNu |
|--------|-----------------------------|---------|
| **Role** | Defines the interface + implements adaptive placement & archiving | Realizes the interface for radiative transfer post-processing |
| **Scope** | Framework-level: parameter estimation workflows | Domain-level: supernova/kilonova light curves and spectra |
| **Output** | Parameter estimates, waveform catalogs | Observables: light curves, spectra |
| **Connection** | SuperNu plugs into the RIFT workflow as a backend | Takes hydro output → produces observable signatures |

---

## Files Referenced

### RIFT Simulation Manager
- **Code:** `MonteCarloMarginalizeCode/Code/RIFT/simulation_manager/`
- **Docs:** `~/RIFT/research-projects-RIT/docs/source/api_reference/simulation_manager/`
- **API:** `gw_pe_synthetic` backend implementation
- [arXiv: RIFT paper](https://arxiv.org/pdf/1805.10457.pdf)

### SuperNu
- [GitHub: rjw57/SuperNu](https://github.com/rjw57/SuperNu) — Monte Carlo radiative transfer
- Origin: Los Alamos National Laboratory (LANL)

---

*This is a draft v2 with the adaptive placement / archiving framing. Feedback welcome.*