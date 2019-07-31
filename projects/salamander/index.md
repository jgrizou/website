---
layout: default
---

# Modeling the salamander swimming gait with virtual muscles on a robotic platform

_Note: See the project as of 2011 on the BioRob website: [https://biorob.epfl.ch/grizou](https://biorob.epfl.ch/grizou). For memory sake, I have kept the same structure and text as my original 2011 version, and simply added relevant videos within the text._

{% include image.html src='img/salamander.png' col='col-lg-10' sub='The salamander robot used in this work.'%}

## Abstract

This project intends to model the interaction between muscle activation and body curvature for salamander locomotion. The final objective is to reproduce a swimming dynamic on the salamander robot, a nine segments bio-inspired robot capable of swimming and walking, by driving the resulting musculoskeletal model with recorded electromyography.

At first, it has been extracted kinematics of several salamanders from slow motion X-ray movies. Afterwards the musculoskeletal model architecture has been developed based on previous works and robot constraints. Then, using the Webots simulator, the model parameters have been optimized according to statistical electromyography and kinematics. Finally, the model has been successfully tested on the salamander robot in the lab.


## Summary

**Why:** The BIOROB laboratory is well known for its work on central pattern generators (CPG), which are neuronal circuits in charge of animal locomotion. Unfortunately the link between neural activity and body dynamics is not yet modeled for the salamander robot which makes it impossible to control based on a realistic neuronal CPG. This project intends to make a new step in this direction in order to be able to study CPG networks in real interaction conditions and studying how feedback informations could be integrated in this network.

**What :** Trying to obtain a realistic swimming gait with a realistic pattern in muscle activation

**How :** Optimization process on the morphological model (muscle/joint model)

**Needs :**  
- Realistic data for muscle activation
- Realistic data for the swimming gate

**Tools :**
- Webots robotic simulation software
- Salamander robot


## Overview

Realistic data for muscles activations (EMG) have been extracted from : I. Delvolvé, T. Bem, and J.M. Cabelguen. Epaxial and limb muscle activity during swimming and terrestrial stepping in the adult newt, pleurodeles waltl. Journal of neurophysiology, 78(2): 638, 1997.

{% include image.html src='img/EMG.png' col='col-lg-10'%}

Realistic data for the swimming gate have been extracted from slow motion X-Ray movies recorded by Kostas Karakasiliotis (BIOROB) in collaboration with Prof Martin Fischer, Jena University.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
{% include youtube.html id='t6hQE4Kf4iQ' sub='Real Salamander Swimming.' %}    
    </div>
    <div class="col-md">
    {% include youtube.html id='5iywdtXVkq0' sub='X-Ray of a swimming salamander.' %}
    </div>
  </div>
</div>

Muscles properties and muscle to body interaction are simulated based on the current body position and the muscles activation level.

{% include image.html src='img/models.png' col='col-lg-10' %}

The resulting parameters are joints torques that can be applied on the robotic platform or on the simulated robot. Depending on the interaction condition, a new body position is defined and the process can be repeated again.

{% include image.html src='img/computational_steps.png' col='col-lg-10' %}

The optimization process help us finding the best set of morphological parameters which can reproduce a realistic swimming gait based on a realistic pattern in muscle activation.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
{% include youtube.html id='Vw7jM3cd5Hs' sub='Optimization Result Webots' %}    
    </div>
    <div class="col-md">
    {% include youtube.html id='0LADFUyRaHU' sub='Optimization Result Matlab Processing' %}
    </div>
  </div>
</div>

Once a reasonable set of parameters is found, we can start implementing the morphological model on the robotic platform. This part is more difficult because we have to deal with real time, real interaction condition, torque control and hardware limitation (i.e. maximal torque limit). One interesting point for switching to real world is the ability to feel the robot. Muscles give passive properties to the robot that are hard to feel in the simulated world.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include youtube.html id='KU0XrAa6Gws' sub='Lamprey Passive Properties' %}
    </div>
    <div class="col-md">
    {% include youtube.html id='uGtc3DciIhg' sub='Salamander Passive Properties' %}
    </div>
  </div>
</div>

Below are two additional videos of the robot swimming in water using the simulated muscle model.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
{% include youtube.html id='wM-HoDmEPBA' sub='Salamander Swim 0.5Hz' %}
    </div>
    <div class="col-md">
{% include youtube.html id='zasxxgAcjLM' sub='Salamander Turns 0.5Hz' %}
    </div>
  </div>
</div>


## Resources

The thesis, reports, and presentations are available at [https://github.com/jgrizou/publications/tree/master/thesis/master](https://github.com/jgrizou/publications/tree/master/thesis/master)
