---
layout: post
title: "Lange-RIFT"
date: 2018-05-01
---

RIFT is an algorithm to perform Rapid parameter Inference on gravitational wave sources via Iterative Fitting.  In short, we fit the likelihood as a function of parameters; then, we use the fitted likelihood to infer  source parameters.   RIFT  provides unique capabilities to  use the best available models.  Also, RIFT shares technical roots with a closely related code, to infer BBH parameters via direct comparison with NR simulations.   As we'll demonstrate soon, this investigation corroborates the tools used by and complements the results of direct comparison with NR.






 For experts:  Building off the rapid_pe approach introduced in [Pankow et al 2015](http://adsabs.harvard.edu/abs/2015PhRvD..92b3002P), RIFT adds a concrete fitting and iteration strategy, enabling it to operate robustly.  
 Due to its structure (inherited from the `rapid_pe` approach of Pankow et al 2015, used extensively in comparisons to NR), this method inherits unique technical capabilities to employ costly but accurate waveforms;  to assess model systematics; and to enable unique calculations enabled by direct access to the marginalized likelihood, such as constraints on the equation of state.   We first  demonstrate the code using aligned and precessing binary black holes, including GW150914, and synthetic binary neutron stars.  Then we show how to use RIFT to identify  differences between models; employ a patchwork of models; and constrain the nuclear equation of state.




 For more information, see 



  * Lange, O'Shaughnessy, and Rizzo  	Rapid and accurate parameter inference for coalescing, precessing compact binaries,  available at [arxiv.org](https://arxiv.org/abs/1805.10457) (LIGO DCC [P1800084](https://dcc.ligo.org/LIGO-P1800084))
