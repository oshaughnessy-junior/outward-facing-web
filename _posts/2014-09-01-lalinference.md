---
layout: post
title: "lalinference"
date: 2014-09-01
---

Gravitational wave astronomy begins with  inference : figuring out what kind of astrophysical source was responsible for the implausible event in our data.   By exhaustively comparing that  data against all  candidate signals, we can reconstruct how consistent with that data any any proposed source is.   In other words, we can use gravitational waves to measure the properties of the sources responsible for each gravitational wave signal we detect!  
  These  measurements will tell us how often different types of compact objects mege throughout the universe, revolutionizing our understanding of how stars and stellar systems evolve to produce these exotic binaries.   And might also let us probe the nature of nuclear matter; resolve longstanding astrophysical mysteries like short gamma ray bursts; and even challenge our understanding of gravity itself.  







Through the persistent efforts of several key colleagues (notably John Veitch; Vivien Raymond; and Ben and Will Farr), a subset of the LIGO Scientific Collaboration has consolidated its expertise in gravitational wave parameter estimation into a single authoritative library, `lalinference`.    




 For experts: LALInference provides a general library for accessing data and waveform libraries; evaluating the likelihood of the data, assuming gaussian noise;  exploring the likelihood surface, via Markov Chain Monte Carlo or nested sampling;  transforming the results of that exploration into robust statements about the posterior distribution of source parameters, given a model; and ranking different models, via their evidence. 
Though systematically limited by  the accuracy of approximations  to strong field binary motion and by ideosyncratic correlations unique to gravitational physics, gravitational wave measurements will constrain compact object masses and spins to a previously unattainable accuracy.




 For more information, see  



* Our paper:  Veitch et al (2014)  
 
* Sample applications of `lalinference`-based parameter estimation (PE):   
 [Singer et al (2014), The First Two Years of Electromagnetic Follow-Up with Advanced LIGO and Virgo](http://arxiv.org/1404.5623): PE for multimessenger astronomy

  * [Wade et al (2014)](http://adsabs.harvard.edu/abs/2014PhRvD..89j3012W): PE to measure the equation of state of nuclear matter

  * [Aasi et al (2014)](http://adsabs.harvard.edu/abs/2014CQGra..31k5004A): PE applied to numerical relativity
