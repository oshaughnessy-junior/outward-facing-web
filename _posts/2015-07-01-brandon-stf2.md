---
layout: post
title: "Brandon-STF2"
date: 2015-07-01
---

Multimessenger astronomy with gravitational waves relies  on rapid decisions, as astronomers search for some type of transient afterglow left behind after compact binary mergers.  Given limited telescope time, astronomers want to know where, when, and critically whether to point their telescopes.   Astronomers in particular want to follow up mergers involving  neutron stars, as these could be candidate gamma ray burst sources.  Unfortunately, LIGO does not directly measure the components masses (let alone composition) via detected gravitational waves.  Instead, these source parameters must be inferred by a process of systematically comparing all possible sources with the data.  These exhaustive comparisons can be slow -- days  to produce a reliable answer.  



 In a study led by Brandon Miller  and I at RIT, building upon investigations started by my longstanding collaborators from the Chicago metro area, we demonstrated that a fast but approximate method for parameter estimation produces reliable answers to astrophysical questions.  This method's speed advantage comes from simplified physics (ignoring the smaller object's spin) and, critically, a fast and accurate waveform model that [Andy Lundgren and I introduced in 2013](http://adsabs.harvard.edu/abs/2014PhRvD..89d4021L).  Using existing codes and algorithms, this approach produces rapid and reliable-enough parameter estimates, often within an hour.  
Our approach shows LIGO can rapidly estimate the posterior probability that some  gravitational wave data is consistent with  a tidal disruption event, beamed towards us, and therefore a good candidate for followup with large electromagnetic telescopes.




 For experts  Using a fixed set of sources produced with `SpinTaylorT2`, we compare the performance of parameter estimation using several different approximants and physics, including  `SpinTaylorF2` (a single spin model); double-spin `SpinTaylorT2`;  and single-spin `SpinTaylorT2` and T4.   Given the still-large systematic uncertainties in precessing waveform models, these approximations produce consistent predictions for posterior parameter distributions and astrophysically-motivated questions.






* [Miller et al.,Systematic uncertainties in parameter estimation with the SpinTaylorF2 approximation](http://arxiv.org/abs/1506.06032), Submitted to PRD
