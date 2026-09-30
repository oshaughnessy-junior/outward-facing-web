---
layout: post
title: "How waveform choices change what we learn from gravitational waves"
date: 2026-09-15T19:24:16+00:00
description: "A 60-event comparison shows why gravitational-wave conclusions should be tested against multiple waveform models."
authors: Junior
tags: [astrophysics, gravitational-waves]
---

Written by Junior at 2026-09-30

## One signal, several possible readings

When researchers detect ripples in spacetime, they use computer models of gravitational-wave signals to infer what produced them: the masses, spins, and other properties of compact objects. That means the model used to interpret a signal can become part of the uncertainty.

In arXiv:2609.15827v1, N. Manning and R. O'Shaughnessy revisit 60 publicly available events from the first three observing runs, covering GWTC-1, GWTC-2, GWTC-2.1, and GWTC-3. They analyze all of them with one consistent framework and compare three quasicircular waveform models. Two are newer time-domain models—SEOBNRv5PHM and IMRPhenomTPHM—that include higher-order modes, extra features of the signal produced by asymmetric or more complicated motions. The third, IMRPhenomPv2, is an older frequency-domain model without those modes.

## What changes when the model changes?

The two newer models agree well overall, but the abstract reports a visible difference in at least one one-dimensional marginal posterior for about 20% of the events. A posterior is a probability distribution for an inferred property; in everyday terms, it records which values remain plausible after the data and model are considered together.

The older model more often gives qualitatively different conclusions for key events across the mass spectrum. The comparison does not mean that every result is unstable. It shows instead that agreement between modern models is useful evidence that an inference is robust, while relying on one model alone can hide model-dependent uncertainty.

## A technical detail with astrophysical consequences

The authors also identify a bug in published LVK GWTC-2.1 SEOBNRv4PHM results and in a later reprocessing of GW200105. At the sampling rates used in those analyses, a restriction tied to the model’s Nyquist frequency excluded part of the allowed parameter space. For seven low-mass events, that artificially cut off the mass-ratio posterior away from equal mass—making equal-mass systems appear less supported by the analysis than they should have been.

## Why this matters

The paper’s lesson is practical: uncertainty in gravitational-wave astronomy includes uncertainty from waveform models and from the settings used to analyze them. Comparing multiple state-of-the-art models, and checking implementation details that define the allowed parameter space, helps separate what the detector data say from what a particular analysis pipeline assumes. As the catalog of gravitational-wave events grows, that discipline will be central to turning faint cosmic signals into reliable knowledge about the universe.

