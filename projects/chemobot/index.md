---
layout: default
---


# Applying machine learning to the exploration of physicochemical systems

Last update: January 2019

*How can AI help make discoveries on the bench in a chemistry lab? How can chemical systems help devise better AI algorithms? I explored those questions with the team I lead in the [Cronin Group](http://www.chem.gla.ac.uk/cronin/). The group cutting edge knowledge combined with my experience from the developmental sciences allowed us to bring innovative ideas to the field, including the use of active learning, curiosity-driven exploration, and human comparative studies.*

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include youtube.html id='RC_nc0P_crc' sub="Compilation of droplet behaviors - one of the system we studied."%}
    </div>
    <div class="col-md">
    {% include youtube.html id='\_pAtu3atYN8' sub="Compilation of robotic platforms designed by the team."%}
    </div>
  </div>
</div>


## Content

- [Approach](#approach)
- [Team](#team)
- [Projects](#projects)
  - [Curiosity-driven exploration on a laboratory robot](#dropfactory)
  - [Active learning in crystallization experiments](#human-vs-robots)
  - [Hierarchical exploration of gold nanoparticles](#nanobot)
  - [Physical environment as an experiment variable](#flowbot)
  - [AI to better understand self-propelled droplets](#surfbot)
  - [Black-box optimization of self-propelled droplets](#dropbot)
- [Resources](#additional-resources)
- [Personal Notes](#personal-notes)

## Approach

After my PhD, I grew frustrated that most AI research was done on simulated environments. I wanted to see this technology used in the real world on systems we do not ourselves design nor understand - that is not even on robots.

The physical sciences seem fitting. In physics, chemistry, or biology, an important part of everyday research is to understand yet unknown systems. Scientists devise experiments and build instruments to query these systems with the aim to be able to model, and later predict, their evolution.

But because such systems are not yet fully understood, or are massively parallel, they cannot be simulated. There is no cheating with the physical sciences, you cannot speed up experiments, you cannot be 100% sure that you are controlling the right experimental variables, and you do not know the right answer. That is all the fun of it.

This is in sharp contrast with the simulation, big data, and controlled robotic problems AI algorithms are designed on and for. {% include footnote.html to=1 %} If we ought to bring AI advances to experimental research in the labs, we need to drop the habit of thinking that experiments are free, unlimited, and well defined. That habit comes from the extraordinary power of computers and can sometime turn AI research into a parameter tuning and stacking game.

Interestingly, a subfield of robotics, called [developmental robotics](https://en.wikipedia.org/wiki/Developmental_robotics), imposes itself similar constraints. Their aim is to build a robot that can learn like a child. A child has real world constraints, it has limited time to interact with the world and he has no complete built-in knowledge of the world around him. From his own body, to modern objects like smartphones and bikes, a child has to learn it all in a few years by interacting with the world. To do so a child constantly devises his own experiments to test the world around him, much like a scientist in its lab.

As it turns out, I pursued my PhD under the supervision of [Pierre-Yves Oudeyer](http://www.pyoudeyer.com/), one of the pioneers of this field. Once I connected the dots, an ocean of research directions opened to bring principles from developmental robotics into the physical sciences. How can a laboratory robot be curious and devise its own questions about a new systems? How could it learn a hierarchy of skills to produce increasingly more complex molecules autonomously? How could such machines learn from and collaborate with scientists? Could maturational constraints and the concept of embodiment help leverage the exploration power of algorithms on natural systems?

Hence came the decision to join a chemistry lab for a postdoc.

## Team

[Lee Cronin](https://en.wikipedia.org/wiki/Leroy_Cronin), a pioneer in the digitization of chemistry, welcomed me into [his lab](http://www.chem.gla.ac.uk/cronin/) and gave me the responsibility of an internal team to explore these questions. The group had already published a work showcasing the robotically assisted optimization of oil-in-water droplets, a suitable system for our experimentation.

{% include image.html src='img/team.png' sub="The Chemobot team from 2015-2018 within the Cronin group, University of Glasgow. Missing is Kevin Donkers."%}

The team was composed of Lee Cronin (PI), Jonathan Grizou (me), Abhishek Sharma, Jan Szymanski, James W. Taylor, Juan Manuel Parrilla Gutierrez, Laurie J. Points, Vasilios Duros, Sergio Martin Marti, Graham Keenan, Kevin Donkers. A mix of chemists, computer scientists, and material scientists.

The main challenge resided in a good communication between team members. Chemists had to understand the limitation of computers in making sense of data, as well as the limitation of robots in manipulating things. Computer scientists (me above all) had to understand that chemistry is hard, requires time, and that not everything can be created at will. The team was fantastic at sharing their respective constraints which is the main factor of success in the projects we have undertaken.

As the first trained roboticist to join the group, I also took care setting up a culture of AI and robot building, as well as developing the right tools for chemists to use simply, safely, and robustly. These tools are available on the [group GitHub account](https://github.com/croningp) and further described on [this page](../open_robotics/#laboratory-robotics).

## Projects

{% include anchor.html id="dropfactory" %}
### Curiosity driven exploration of oil-in-water droplets

We developed a chemical robotic discovery assistant equipped with a curiosity algorithm (CA) that was set to explore the states a complex chemical system can exhibit searching for novelty. This differ from optimization scenario where a global target is defined beforehand.

{% include youtube.html id='bY5OoRBJkf0' col='col-lg-10' sub="The <a href='https://github.com/croningp/dropfactory'>Dropfactory robot</a> is able to perform, record, and clean 8 droplet experiments in parallel." %}

By applying the CA-robot to the study of self-propelling multicomponent oil-in-water droplets, we are able to observe an order of magnitude more variety of droplet behaviours than possible with a random parameter search and given the same budget. We demonstrate that the CA-robot enabled the discovery of a sudden and highly specific response of droplets to slight temperature changes.

{% include image.html src='img/dropfactory_result.png' col='col-lg-10' sub="Summary of the results. Left: (A) % of explored space. CA explored 3.3 times more than random. (B, C) Observations made by each method for each repeat; each scatter dot represents a single droplet experiment. CA (B) leads to a greater variety of observations than random (C). Right: Effect of temperature. (D) Number of experiments with a speed faster than 3 mms-1. A change of only ca. 4.4°C led to a significant difference in the observed droplet behaviours when using the CA (395 vs 93, p=0.005), which is not observed when using random (28 vs 19, p=0.22). This is confirmed by (E) and (F) which show the distribution of observation. The CA enabled the discovery of the temperature effect." %}

Once the temperature dependance was discovered, six modes of self-propelled droplets motion were identified and classified using a time-temperature phase diagram and probed using a variety of techniques including NMR, which allowed the design of a payload release system triggered by temperature. This work illustrates how target free search can significantly increase the rate of unpredictable observations leading to new discoveries with potential applications in formulation chemistry.

{% include youtube.html id='80yAmBkzdmM' col='col-lg-10' sub="Effect of temperature on droplet motion." %}

#### Resources

1. **A curious formulation robot enables the discovery of a novel protocell behavior.** Grizou, J., Points, L. J., Sharma, A. & Cronin, L. (2020). *Science Advances.*
[[pdf]](https://advances.sciencemag.org/content/6/5/eaay4237.full.pdf)
[[doi]](https://doi.org/10.1126/sciadv.aay4237)
[[robot design]](https://github.com/croningp/dropfactory)
[[experiment code]](https://github.com/croningp/dropfactory_exploration)
[[analysis code]](https://github.com/croningp/dropfactory_analysis)
[[project]]({{ site.baseurl }}/projects/chemobot#dropfactory)

{% include anchor.html id="human-vs-robots" %}
### Active selection of crystallization experiments and comparison with human methodology

The discovery of new gigantic molecules formed by self-assembly and crystal growth is challenging as it combines two contingent events; first is the formation of a new molecule, and second its crystallization. We constructed an automated workflow that can probe both events and employed it for a new polyoxometalate cluster which has a trigonal-ring type architecture.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include image.html src='img/hvr_pom.png' col='col-lg-10' sub="Schematic representation of the
    {Mo120Ce6} wheel from basic building blocks." %}
    </div>
    <div class="col-md">
    {% include image.html src='img/hvr_platform.png' sub="Automated platform in the lab."%}
    </div>
  </div>
</div>


The synthesis and crystallization was probed using an active machine-learning algorithm to explore the crystallization space. The algorithm results were compared with those obtained by human experimenters and a random sampling approach.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include image.html src='img/hvr_diagram.png' sub="Representation of the experimental method showing how the automated and bench work was done."%}
    </div>
    <div class="col-md">
    {% include image.html src='img/hvr_method.png' sub="Schematic diagram of the exploration methods. All experiments are performed crystallization robotic platform."%}
    </div>
  </div>
</div>

A critical constraint was that we could only perform 10 experiments per day. We ran the active learning by batches of 10 experiments and performed 10 iterations for a total of 100 experiments for each method and repeat. Meaning that 10 days and significant reagent were needed just to validate the approach the first time. Our result showed that the active learning algorithmic search increases the crystallization prediction accuracy to 82.4±0.7% over 77.1±0.9% from human experimenters given the same experimental budget.

{% include image.html src='img/hvr_result.png' col='col-lg-10' sub="Average for the crystallization prediction accuracy between the classes of crystals and non-crystals for the three methods, using a RandomForest classifier." %}

#### Resources

1. **Intuition-enabled Machine Learning beats the Competition when Joint Human-Robot Teams per-form Inorganic Chemical Experiments.** Duros, V., Grizou, J., Sharma, A., Mehr, S.H.M., Bubliauskas, A., Frei, P., Miras, H.N. and Cronin, L. (2019). *Journal of chemical information and modeling.*
[[pdf]](https://pubs.acs.org/doi/pdf/10.1021/acs.jcim.9b00304)
[[journal]](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.9b00304)
[[project]]({{ site.baseurl }}/projects/chemobot#human-vs-robots)

1. **Human vs Robots in the Discovery and Crystallization of Gigantic Polyoxometalates.** Grizou, J., Duros, V., Xuan, W., Hosni, Z., Long, D.-L., Miras H., Cronin L. (2017). *Angewandte Chemie 129.36: 10955-10960.*
[[pdf]](https://core.ac.uk/download/pdf/84148587.pdf)
[[SI]](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fanie.201705721&file=anie201705721-sup-0001-misc_information.pdf)
[[code]](https://github.com/croningp/crystal_active_learning)
[[journal]](http://dx.doi.org/10.1002/anie.201705721)


{% include anchor.html id="nanobot" %}
### Hierarchical exploration on gold nanoparticles

We developed a liquid-handling robot built with the aim of evolving the size and shape of gold nanoparticles (AuNPs) as a function of composition via an automated evolutionary process. The robot synthesises nanoparticles by mixing reagents in different ratios, placing them in vials and extraction to in-line UV-Vis analysis that is used to compute a fitness value.

{% include image.html src='img/nano_platform.png' col='col-lg-10' sub="Custom autonomous gold nanoparticles synthesizer. We see the reagents, the pumps, the Geneva wheel design allowing to run 15 reactions simultaneously, the heater that maintain a constant temperature and the in-line UV-Vis cell and spectrometer for the analysis."%}

The project aimed at exploring how we could reuse the result of genetic algorithm experiments (e.g. evolution of nano-spheres) to evolve more complex nanoparticles such as nano-rods. The diagram below illustrate this process.

{% include image.html src='img/nano_diagram.png' col='col-lg-10' sub="Spheres are evolved starting from raw chemicals. The best candidates are reused for the synthesis of rods along with other chemicals. The best rods obtained are reused as seeds to obtain arrow-headed gold nanorods"%}

After several cycles and the application of a genetic algorithm (GA), the fitness factor at each stage increased every generation leading towards the desired outcome. Our system could synthesise recursively gold nanospheres, gold nanorods (AuNRs), and arrow-headed gold nanorods with high reproducibility.

{% include image.html src='img/nano_result.png' col='col-lg-10' sub="Left: Evolution of the median fitness per generation. Middle: Comparison between UV-Vis spectrum of particles described in the literature and the best particles obtained with the robot. Right: TEM image of the particles that correspond to the UV-Vis spectrum shown."%}

Our results show that the evolution of nanomaterials is possible in a fully automated fashion and has the potential to change the way AuNPs are studied and explored.

#### Resources

1. **A Nanomaterials Discovery Robot for the Darwinian Evolution of Shape Programmable Gold Nanoparticles.** Keenan, G., Salley, D., Martín, S., Grizou, J., Sharma, A. and Cronin, L. (2020). *Nature Communications.*
[[pdf]](https://www.nature.com/articles/s41467-020-16501-4.pdf)
[[doi]](https://doi.org/10.1038/s41467-020-16501-4)
[[project]]({{ site.baseurl }}/projects/chemobot#nanobot)


{% include anchor.html id="flowbot" %}
### Physical environment as an experiment variable

Evolution via natural selection is governed by the persistence and propagation of living things in an environment. The environment is important since it contributes in shaping evolution. Although evolution has been widely studied in a variety of fields from biology to computer science, still little is known about the impact of environmental changes on an artificial chemical evolving system outside of computer simulations.

We developed a fully automated 3D-printed chemorobotic fluidic system that is able to generate and select droplet protocells in real time while changing the surroundings where they undergo artificial evolution.

{% include image.html src='img/flowbot_diagram.jpg' col='col-lg-10' sub='Schematic describing the evolutionary process. In the first step, a computer-generates random recipes using ratios of 1-octanol, octanoic acid, 1-pentanol and diethyl phthalate. These oils are then mixed through a serpentine channel, and populations of five droplets are generated in the evolutionary arena. The droplet behaviours are then analysed, and ranked using a fitness function. The best droplets are selected, and new droplet formulations were generated after “mutation” and “crossover” operations.' %}

Compared to our previous work, the use of a 3D-printed device enable us to change the physical environment in which the droplet population evolves. The 3D printed platform also innovates as no moving parts are required to initiate, run, and clean droplet experiments.

{% include image.html src='img/flowbot_platform.jpg' col='col-lg-10' sub='Schematic of the 3D-printed system. Chemical inputs are handled by pumps. Droplet mixtures are formed through a serpentine channel and pushed to form droplets into an evolutionary arena. A camera records the arena from above. Image processing algorithms is used to analyse and categorise the droplets behaviours.'%}

{% include youtube.html id='RzqkPU0Pa3Q' col='col-lg-10' sub='Trailer of the platform in action.'%}

Using such 3D-printed devices, we were able to change the physical environment in which the droplet population evolves. We thus explicitly studied how the genotype is modulated through a programmable environment to express its phenotype, in contrast to the more studied genotype to phenotype direct approach.

{% include youtube.html id='UJSlCrCaaAo' col='col-lg-10' sub="Droplet recipes evolving through a genetic algorithm in different arenas." %}

By successively evolving the droplets from one environment to another, we were able to observe disruption in their evolutionary trajectories, as well as adaptation of their genome.

{% include image.html src='img/flowbot_result.png' col='col-lg-10' sub="Environmental change results. Fitness evolution over generation. The first 10 generations used an empty arena, the following 10 generations used an arena filled with pillars, and the last 10 generations used the arena generated using an L-system. The arena was swapped to the pillars environment between the 10th and 11th generation, inducing a drop in the fitness values, which forced the droplet to adapt and evolve again in the new environment. The arena was swapped to the L-system between generations 20 and 21, introducing no noticeable fitness changes."%}


#### Resources

1. **Adaptive artificial evolution of droplet protocells in a 3D-printed fluidic chemorobotic platform with configurable environments.** Parrilla-Gutierrez, J. M., Tsuda, S., Grizou, J., Taylor, J., Henson, A., & Cronin, L. (2017). *Nature communications, 8(1), 1144.*
[[pdf]](https://www.nature.com/articles/s41467-017-01161-8.pdf)
[[journal]](https://www.nature.com/articles/s41467-017-01161-8)


{% include anchor.html id="surfbot" %}
### AI as a tool to understand complex systems

Exploring and understanding the emergence of complex behaviors is difficult even in “simple” chemical systems since the dynamics can rest on a knife edge between stability and instability.

We study the dynamics of a oil droplets in an aqueous environment using an automated platform equipped with artificial intelligence. Compared to previous work, we increased the number of experimental parameters and allowed the robot to choose both the concentration of oils in the droplets and the concentration of surfactants in the aqueous phase. Our aim was to identify more droplet behaviors and understand better the mechanisms behind them.

{% include youtube.html id='yp5018y_6tM' col='col-lg-10' sub='Operation of the platform.'%}

To test the platform, we started by running evolutionary experiments and comparing them to our previous work.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md-4">
      {% include image.html src='img/surfbot_evospeed.png' sub="Comparison of median fitness values per generation between the oil-only, aqueous-only, and aqueous-oil optimizations."%}
    </div>
    <div class="col-md-8">
      {% include youtube.html id='dO-1Jy1e76g' sub='Comparison of speed achieved with the oil-only, aqueous-only, and aqueous-oil optimizations.'%}
    </div>
  </div>
</div>

By opening the parameters space to the chemical environment of the droplets, we were able to generate faster moving droplets. The recipes and data generated from this process were then used for physicochemical analysis, where traditional chemical analysis, machine learning, and archetypal droplet experiments are used to study the behavioral mechanisms and to predict droplet behaviors.

{% include image.html src='img/surfbot_diagram.jpg' col='col-lg-10' sub="This work combined robotic exploration and AI to identify behaviors with traditional physical chemical analysis augmented with AI."%}

The data acquired were used to build predictive models of the system, of which no physical model, or only inaccurate models, were available.

{% include image.html src='img/surfbot_svm.jpg' col='col-lg-10' sub="Plots of the predicted density (Left), dynamic viscosity (Center), and surface tension (Right) against their measured values. Blue points are predicted using weighted mean (density) and Arrhenius-based method (viscosity) while red values are predicted using an SVM regressor."%}

Physical properties such as viscosity, surface tension, and density are shown to be related to behaviors, as well as to droplet behavioral niches, such as collective swarming. By dying droplets with phenolphthalein, we could observe the internal dynamics within the droplets and depending of their composition. For example, pentanol goes very pink, has rapid flows, and dissolves, while DEP only goes pink at the interface.

{% include youtube.html id='-fqDohfLYTA' col='col-lg-10' sub='Dye experiments showing the complex flow of chemicals inside the droplets.'%}

#### Resources

1. **Adaptive artificial evolution of droplet protocells in a 3D-printed fluidic chemorobotic platform with configurable environments.** Parrilla-Gutierrez, J. M., Tsuda, S., Grizou, J., Taylor, J., Henson, A., & Cronin, L. (2017). *Nature communications, 8(1), 1144.*
[[pdf]](https://www.nature.com/articles/s41467-017-01161-8.pdf)
[[journal]](https://www.nature.com/articles/s41467-017-01161-8)


{% include anchor.html id="dropbot" %}
### Black box optimization of oil-in-water droplets

This work focus on the optimization of dynamic properties of droplets on a robotic platform. It was completed before I joined the Cronin group, and made me realize it became possible to apply a range of new exploration methods freshly developed in computer science research groups directly on physical systems in the lab.

They presented a liquid-handling robot built with the aim of investigating the properties of oil droplets as a function of composition via an automated evolutionary process. The robot makes the droplets by mixing four different compounds in different ratios and placing them in a Petri dish after which they are recorded using a camera and the behaviour of the droplets analysed using image recognition software to give a fitness value.

{% include youtube.html id='JSEZdo29rc8' col='col-lg-10' sub='The first droplet robot made in the Cronin group.'%}

In separate experiments, the fitness function discriminates based on movement, division and vibration over 21 cycles, giving successive fitness increases. Analysis and theoretical modelling of the data yields fitness landscapes analogous to the genotype–phenotype correlations found in biological evolution.

{% include image.html src='img/dropbot_result.jpg' col='col-lg-10' sub="Graphs showing the change in fitness (evolutionary trajectory) over each successive generation of experiments for (a) division, (b) motion and (c) vibration."%}

#### Resources

**Evolution of oil droplets in a chemorobotic platform.** Gutierrez, J. M. P., Hinkley, T., Taylor, J. W., Yanev, K., & Cronin, L. (2014). *Nature communications, 5, 5571.*
[[pdf]](https://www.nature.com/articles/ncomms6571.pdf)
[[journal]](https://www.nature.com/articles/ncomms6571)


{% include anchor.html id="additional-resources" %}
## Resources

### Workshop

In 2017, we organized a [workshop](https://croningp.github.io/tutorial_icdl_epirob_2017/) providing an extensive overview of this research.
[[pdf]](https://croningp.github.io/tutorial_icdl_epirob_2017/tutorial_proposal_final.pdf)
[[slides]](https://github.com/croningp/tutorial_icdl_epirob_2017/releases/tag/slides)
[[website]](https://croningp.github.io/tutorial_icdl_epirob_2017/)

### Code and tools

We have developed a collection of software and hardware tools that has been made open source to help further research in this area. These tools are described on the [open robotics project page]({{ site.baseurl }}/projects/open_robotics/#laboratory-robotics) and available on the [Cronin group GitHub account](https://github.com/croningp).

### Publications

1. **A curious formulation robot enables the discovery of a novel protocell behavior.** Grizou, J., Points, L. J., Sharma, A. & Cronin, L. (2020). *Science Advances.*
[[pdf]](https://advances.sciencemag.org/content/6/5/eaay4237.full.pdf)
[[doi]](https://doi.org/10.1126/sciadv.aay4237)
[[robot design]](https://github.com/croningp/dropfactory)
[[experiment code]](https://github.com/croningp/dropfactory_exploration)
[[analysis code]](https://github.com/croningp/dropfactory_analysis)
[[project]]({{ site.baseurl }}/projects/chemobot#dropfactory)

1. **A Nanomaterials Discovery Robot for the Darwinian Evolution of Shape Programmable Gold Nanoparticles.** Keenan, G., Salley, D., Martín, S., Grizou, J., Sharma, A. and Cronin, L. (2020). *Nature Communications.*
[[pdf]](https://www.nature.com/articles/s41467-020-16501-4.pdf)
[[doi]](https://doi.org/10.1038/s41467-020-16501-4)
[[project]]({{ site.baseurl }}/projects/chemobot#nanobot)

1. **Intuition-enabled Machine Learning beats the Competition when Joint Human-Robot Teams per-form Inorganic Chemical Experiments.** Duros, V., Grizou, J., Sharma, A., Mehr, S.H.M., Bubliauskas, A., Frei, P., Miras, H.N. and Cronin, L. (2019). *Journal of chemical information and modeling.*
[[pdf]](https://pubs.acs.org/doi/pdf/10.1021/acs.jcim.9b00304)
[[journal]](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.9b00304)
[[project]]({{ site.baseurl }}/projects/chemobot#human-vs-robots)

1. **Artificial intelligence exploration of unstable protocells leads to predictable properties and discovery of collective behavior.** Points, L. J., Taylor, J. W., Grizou, J., Donkers, K., & Cronin, L. (2018). *PNAS - Proceedings of the National Academy of Sciences, 201711089.*
[[pdf]](https://www.pnas.org/content/pnas/early/2018/01/09/1711089115.full.pdf)
[[journal]](https://www.pnas.org/content/115/5/885.short)

1. **Adaptive artificial evolution of droplet protocells in a 3D-printed fluidic chemorobotic platform with configurable environments.** Parrilla-Gutierrez, J. M., Tsuda, S., Grizou, J., Taylor, J., Henson, A., & Cronin, L. (2017). *Nature communications, 8(1), 1144.*
[[pdf]](https://www.nature.com/articles/s41467-017-01161-8.pdf)
[[journal]](https://www.nature.com/articles/s41467-017-01161-8)

1. **The evolution of active droplets in chemorobotic platforms.** Points, L. J., Grizou, J., Gutierrez, J. M. P., Taylor, J. W., & Cronin, L. (2017). *Artificial Life Conference Proceedings 14.*
[[pdf]](https://www.mitpressjournals.org/doi/pdfplus/10.1162/isal_a_059)

1. **Human vs Robots in the Discovery and Crystallization of Gigantic Polyoxometalates.** Grizou, J., Duros, V., Xuan, W., Hosni, Z., Long, D.-L., Miras H., Cronin L. (2017). *Angewandte Chemie 129.36: 10955-10960.*
[[pdf]](https://core.ac.uk/download/pdf/84148587.pdf)
[[SI]](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fanie.201705721&file=anie201705721-sup-0001-misc_information.pdf)
[[code]](https://github.com/croningp/crystal_active_learning)
[[journal]](http://dx.doi.org/10.1002/anie.201705721)

1. **Developmental robotics in a chemistry lab.**  Grizou, J., Points L.J., Cronin, L. (2017). *Development and Learning and Epigenetic Robotics (ICDL-Epirob), 2017 Joint IEEE International Conferences on.*
[[pdf]](https://croningp.github.io/tutorial_icdl_epirob_2017/tutorial_proposal_final.pdf)
[[slides]](https://github.com/croningp/tutorial_icdl_epirob_2017/releases/tag/slides)
[[website]](https://croningp.github.io/tutorial_icdl_epirob_2017/)

1. **Evolution of oil droplets in a chemorobotic platform.** Gutierrez, J. M. P., Hinkley, T., Taylor, J. W., Yanev, K., & Cronin, L. (2014). *Nature communications, 5, 5571.*
[[pdf]](https://www.nature.com/articles/ncomms6571.pdf)
[[journal]](https://www.nature.com/articles/ncomms6571)

## Personal Notes

The above work - done between 2015 and 2018 - is the application of ideas from a small subfield of machine learning and robotics, called [developmental robotics](https://en.wikipedia.org/wiki/Developmental_robotics) (see my [PhD lab](https://flowers.inria.fr/)), to an emerging field at the intersection of robotics, AI, and chemistry. 

I believe the projects we showcased provide a good window into future applications of AI and robotics in formulation sciences. More specifically in R&D departments to help find new formulations for consumer goods and medical treatments, under the ever evolving constraints from law enforcement (forbidden compounds, environment preservation), resource exhaustion, and budget optimization. The research presented above can significantly reduce the time and resources needed for the development of new products. Especially useful will be machines that can explore rather than optimize and collaborate with human rather than replace them.

I also believe that constraints from working on physical systems in the labs can be beneficial to the field of AI. When the only solution to querying data is to perform time consuming and costly experiments. It forces AI practitioners to redefine their working methodology and might change the focus of what matters when designing new algorithms.

I am eager to see this research applied to outside the lab. Do not hesitate to get in touch to share ideas or discuss potential projects.

## Footnotes

{% include footnote.html from=1 %} There is good reasons for that, convenience and speed for fundamental research is one, but also because a lot of problems worth solving can be captured adequately by data and simulation. My point focus on hands-on experiments in laboratories.

<div align="center">
  <a href="#">[Back To Top]</a>
</div>

---

<div align="center">
  {% include social-link.html %}
</div>
