---
layout: post
title: "Reconstructing the family histories of black holes"
date: 2026-09-30T14:31:49+00:00
description: "How a physical model of repeated mergers turns patterns in black-hole masses and spins into tests of their origins."
authors: Junior
tags: [astrophysics, gravitational-waves]
---

Written by Junior at 2026-09-30

## Do black holes have a family tree?

A black hole can be born when a massive star collapses. It can also be the survivor of an earlier black-hole collision. If that survivor finds another companion and merges again, the gravitational waves carry clues to a history that began before the collision we observed. Learning how often this happens would tell us how black holes grow and what kinds of crowded cosmic environments bring them together.

Mass and spin provide complementary clues. A merger changes both how heavy a black hole is and how rapidly it rotates. [Earlier research by Davide Gerosa and Emanuele Berti](https://arxiv.org/abs/1703.06223) showed how these patterns could help distinguish black holes formed by stellar collapse from those assembled through previous mergers. A growing catalog lets us move beyond intriguing individual events and test whether a proposed formation history can explain the population as a whole.

## Building a population from the interactions

In [Physics-based phenomenological modeling of binary black hole hierarchical formation 2: Autodifferentiable functional inference of hierarchical compact-binary populations (arXiv:2609.06728v1)](https://arxiv.org/abs/2609.06728v1), we develop a model that connects repeated mergers to the gravitational-wave census. Rather than simply drawing a curve through the observed mass distribution, we begin with a population of newly formed black holes and describe how encounters pair them up. Mergers produce new masses and spins; the recoil from a merger can eject the survivor from its environment, preventing it from participating again. Those ingredients determine how the population changes and which later mergers it can produce.

This approach sits between a purely descriptive fit and a detailed simulation of every interaction in a star cluster. It retains a small, physically interpretable set of rules while remaining practical enough to compare with a catalog. We can vary the initial black-hole population and the preferences for pairing different masses together, then ask which combinations best account for the measurements. The calculation also accounts for which binaries the detectors are more likely to observe.

A key technical advance is making this chain automatically differentiable: the software tracks how changing a formation rule changes the predicted population and its agreement with the data. Embedded in our population-analysis framework, gwkokab, it connects assumptions about birth and subsequent encounters directly to inference from the census. We can test those assumptions together, rather than fitting a distribution first and attaching a formation story afterward.

## When a plausible story meets the census

Applied to GWTC-5.0, the model reveals a difficulty for simple repeated-merger pictures. Heavy black holes growing in a pool of many lighter objects tend to acquire light companions. Yet the observed high-mass population includes binaries whose two members have comparable masses. Producing heavy black holes is therefore not enough: a successful model must also explain which partners they merge with and the associated spin patterns.

We test alternative interaction rules while retaining a separate population that has not been reprocessed through earlier mergers. These comparisons make the formation story more demanding, and more useful. A rule introduced to explain one part of the census must also survive tests elsewhere in the mass-and-spin distribution. The conclusions depend on the environments and interaction rules represented in the model; they are not a unique identification of every binary's birthplace.

That is the payoff of a physical population model: it makes a proposed history answerable to new observations. Some pairing rules predict heavy black holes merging with much lighter companions; continued observations can test whether those systems appear as expected. As the census grows, connected predictions of masses, spins, and pairings can help distinguish how black holes are born from how they grow—turning a collection of cosmic collisions into evidence about the environments that shaped them.
