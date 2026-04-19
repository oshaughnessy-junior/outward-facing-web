---
layout: post
title: "Field-ILE_ROM"
date: 2016-12-01
---

The detection of gravitational waves from massive binary black holes poses a theoretical challenge. Numerical relativity, the only accurate method to solve Einstein's equations for binary black holes, is slow, limiting the number of followup simulations that can be carried out to mimic new events. These highly-accurate solutions are also required: they include physics not incorporated in phenomenological models. Fortunately, NR solutions can be bridged by surrogate methods, which reliably interpolate between these solutions.

In a new paper, we introduce a fast method to compare the data to these NR surrogates. We demonstrate that physics uniquely available to NR or NR-surrogates significantly influences our interpretation of the gravitational wave data.

For experts: We introduce several technical improvements of use for GW parameter estimation. Our method circumvents ILE's previous need to use a discrete grid, enabling embarassingly-parallel PE for generic sources. Too, our extensions now mean ILE can use very accurate models anywhere in parameter space, being limited neither by systematic limitations of models nor discrete placement of NR simulations.

Too, we extended the `gwsurrogate` interface to provide direct access to the basis functions; developed tools to ``re-ROM" existing surrogates into the necessary linear basis; and built a new basis for an NR surrogate.

Most interesting, however, are the prospects for the future: this approach is very fast, scalable, accurate, and generic. With tighter integration (e.g., pre-filtering the data against a ROM basis) and GPU integration, this approach could enable streaming PE, providing the best parameter estimates in real time!

For more information, see

- ROS et al, An architecture for efficient multimodal parameter estimation with linear surrogate models, available at [CQG](http://iopscience.iop.org/article/10.1088/1361-6382/aa7649)

- [Pankow et al, A novel scheme for rapid parallel parameter estimation of gravitational waves from compact binary coalescences](http://arxiv.org/abs/1502.04370) (PRD 92 3002; arxiv:1502.04370), for comparison

- [gwsurrogate](https://pypi.python.org/pypi/gwsurrogate/), a surrogate waveform package used and extended for this work.
