---
layout: post
title: "Fisher Matrix"
date: 2015-06-01
---

What will gravitational waves tell us about merging compact binaries and why? For a theorist, that question can be easily albeit approximately answered by the Fisher matrix. Until recently surpassed by even-more-accurate (but slow) full Bayesian parameter estimation strategies like `lalinference` and `ILE`, the Fisher matrix has been the workhorse of gravitational wave astronomy for decades, allowing theorists to quickly calculate whether compact objects masses and spins; the nuclear equation of state; and even modifications to general relativity itself will be observationally accessible.

For nonprecesing binaries, the Fisher matrix is easily calculated from derivatives of the predicted GW signal. For precessing binaries, the intermediate quantities needed to compute the Fisher matrix were believed to be analytically intractable. (And, in many practical cases, numerically unstable.) In recent work, my collaborators and I showed how to carry out this calculation. Our extremely simple expressions agree well with the measurement accuracies found by detailed Bayesian calculations. Our estimates can be use to quickly and efficiently assess what parameters can be measured and why in astrophysically plausible sources.

For experts By expanding the spin-weighted harmonics using a corotating frame, we could perform the stationary-phase approximation term by term. If sufficiently many precession cycles occur in band, each term has a unique time-frequency trajectory and is effectively orthogonal to all others. Hence, at leading order the Fisher matrix separates into contributions from each harmonic, weighted by the power in each mode. Critically, each mode's contribution is as if from a nonprecessing binary, in a familiar and tractable form. Though our result formally applies to black hole-neutron star binaries, the a priori rarity of comparable spins implies our conclusions will be broadly applicable.

For more information, see

- Paper: [A semianalytic Fisher matrix for precessing binaries with a single significant spin](http://arxiv.org/abs/1509.06581)

- 2015 April APS Meeting: A [Presentation on the method](ccrg.rit.edu/~oshaughn/2015-04-APS-Talk-export.pdf) (April APS 2015)
