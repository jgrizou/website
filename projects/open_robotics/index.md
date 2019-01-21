---
layout: default
---

# Open source robotics

Last update: January 2019

*Robots are coming! Or so they say. I have been interested in robotics for as long as I can remember. Over the years, I struggled my way through the understanding of all technical parts of robot building. And once I became an expert, I grew frustrated by how unnecessarily painful it was to put a robot together. With some friends and colleagues, we have decided to take our part into making robotics more accessible. Below are our attempts, from an open source robotics community of makers, artists, educators and scientists, to accessible tools for chemists, we even created a start-up.*

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md-4">
    {% include image.html src='img/poppy_ergojr_jumping.gif' sub="The first Poppy ErgoJr robot jumping."%}
    </div>
    <div class="col-md-8">
    {% include image.html src='img/cronin_dropfactory.gif' sub="Open source laboratory robot I developed."%}
    </div>
  </div>
</div>

## Content

- [Approach](#approach)
- [Team](#team)
- [Projects](#projects)
  - [Poppy Project - Open source robots for art, science, and education](#poppy-project)
  - [Laboratory Robotics - Tools for open research in chemistry labs](#laboratory-robotics)
  - [Startup - Pollen Robotics & Luos](#start-up)
  - [Personal Projects](#personal-projects)
- [Resources](#additional-resources)

## Approach

In all projects presented below, we strived to develop empowering tools, both software and hardware, that reduce the complexity required for developing robotic devices. But we did not stop there.

We relentlessly worked to make these tools accessible to all. Our creations are available online for free and with a documentation. And we strived to provide demonstration of our technology in various application domains, from art to science, one of our project saw an important development in school education in France.

On a personal level, I have learnt that technology alone can't make an impact. It needs to be embedded into meaningful products that make what was previously impossible possible, or inaccessible accessible, in our everyday lives.


## Team

The [Poppy Project](#poppy-project) was initiated by: Matthieu Lapeyre, Pierre Rouanet, Pierre-Yves Oudeyer, while are INRIA. Didier Roy joined and developed the poppy education project that went into many schools in France. I was part of the founding team and was very active during the period 2012 - 2016.

The [laboratory robotics work](#laboratory-robotics) was developed while working as a research associate and team leader in a chemistry lab (2015-2017). See [associated project page]({{ site.baseurl}}/projects/chemobot) for more info.

The start-up [Pollen Robotics](#start-up) was co-founded by Matthieu Lapeyre, Pierre Rouanet, Nicolas Rabault, Jonathan Grizou. I acted as COO and departed for new adventures in 2018.

## Projects

### Poppy Project

#### History

The [Poppy Project](https://www.poppy-project.org/en/) was born in 2012 in the Flowers laboratory at Inria Bordeaux Sud-Ouest. It was initiated during Matthieu Lapeyre’s PhD Thesis surpervised by Pierre-Yves Oudeyer. At the beginning, the development team was composed by Matthieu Lapeyre (mechanics & design), Pierre Rouanet (software) and Jonathan Grizou (electronics).

{% include image.html src='img/poppy_matthieu.jpg' sub="Matthieu Lapeyre with the first version of Poppy Humanoid."%}

The project grew organically into an international open source project and gathered a [community](https://forum.poppy-project.org/) of makers, artists, educators, and scientists.

{% include image.html src='img/poppy_family.png' sub="Left: A Poppy Humanoid kit. Middle: Poppy Torso and Poppy ErgoJr. Right: Poppy ErgoJr."%}

Our robots were then used in a national education program to teach robotics and programming in schools. Didier Roy and Pierre-Yves Oudeyer lead this effort and formed the [Poppy Education](https://www.poppy-education.org/) project while working at INRIA. This effort has been recognized at the national level and an educator association, called [Poppy Station](https://www.poppystation.org/), has been created to give the project its independence.

_Fun fact:_ Our Humanoid robot met François Hollande, the President of France.

{% include image.html src='img/poppy_president.jpeg' sub="The first Poppy ErgoJr robot jumping."%}

#### Flagship projects

**Poppy Humanoid** is an open-source and 3D printed humanoid robot, designed by Matthieu Lapeyre. Optimized for research and education purposes, its modularity allows for a wide range of applications and experimentations. More information, code, 3D design and documentation are available on Github (>280 stars): [https://github.com/poppy-project/poppy-humanoid](https://github.com/poppy-project/poppy-humanoid).

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include youtube.html id='qs6-Ei8K8iY' sub="First video introducing Poppy Humanoid"%}
    </div>
    <div class="col-md">
    {% include youtube.html id='wvu1SD-FM60' sub="Building of a Poppy Humanoid."%}
    </div>
  </div>
</div>

**Pypot** is a Python library for controlling dynamixel motors, designed by Pierre Rouanet. Dynamixel motors are the main building blocks of our robots and this library allow for quickly and effortlessly controlling many such motors. Code, documentation, and examples are available on Github (>170 stars): [https://github.com/poppy-project/pypot](https://github.com/poppy-project/pypot)

**Poppy ErgoJr** is a small and low cost 6-degree-of-freedom robot arm. It consists of very simple shapes which can be easily 3D printed with FDM printers. More information, code, 3D design and documentation are available on Github (>75 stars): [https://github.com/poppy-project/poppy-ergo-jr](https://github.com/poppy-project/poppy-ergo-jr).

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
      {% include image.html src='img/poppy_ergojr_jumping.gif' sub="The first Poppy ErgoJr robot jumping."%}
    </div>
    <div class="col-md">
      {% include image.html src='img/poppy_ergojr.jpg' sub="ErgoJr robot with different tool ending."%}
    </div>
  </div>
</div>

The ErgoJr robot is the main robot used by the [Poppy Education](https://www.poppy-education.org/). It has been used by thousands of French students.

{% include youtube.html id='cXHeD8XeZTc' col="col-lg-10" sub="Poppy Education video showcasing various educational activities and visual programming."%}


_Websites:_ [[Poppy Project]](https://www.poppy-project.org/en/) [[Poppy Education]](https://www.poppy-education.org/) [[Poppy Station]](https://www.poppystation.org/) [[Poppy Forum]](https://forum.poppy-project.org/) [[GitHub]](https://github.com/poppy-project)

#### Personal contributions

Between 2012 and 2016, as part of founding team, I had an active role in the development of the project. I was especially active on the [forum](https://forum.poppy-project.org/) to develop the community. I built, and contributed to, several tools and robots.

**First ErgoJr** - I build the first version of the ErgoJr robot. In the quest of modular robot design, I developed a set of OpenScad libraries to develop parametric robotic parts using code. Full details on the [dedicated project page](../parametric_parts).

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
      {% include image.html src='img/poppy_ergojr_jumping.gif' sub="The first Poppy ErgoJr robot jumping."%}
    </div>
    <div class="col-md">
      {% include image.html src='../parametric_parts/img/poppy_mini_familly.png' sub="Robots designed by code."%}
    </div>
  </div>
</div>

**ErgoJr in the browser** - Using [three.js](https://threejs.org/), I developed a ErgoJr model that can be interacted with directly in the browser. This enable students to play and test code on the robot without having access to a physical robot. Thanks to Pierre Rouanet, the web simulator can be controlled with exactly the same code library than the physical robot.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
      {% include image.html src='img/poppy_visu.png' sub="ErgoJr in the browser."%}
    </div>
    <div class="col-md">
      {% include youtube.html id='T9FwFOBoz7Y' sub="Pierre Rouanet demo the link between the physical and the simulated robot."%}
    </div>
  </div>
</div>

For more information: [[Demo]](http://simu.poppy-project.org/poppy-ergo-jr/) [[Getting Started]](https://docs.poppy-project.org/en/getting-started/visualize.html#using-our-web-visualizer) [[Website]](http://simu.poppy-project.org/) [[Forum Thread]](https://forum.poppy-project.org/t/ergojr-in-the-browser/1609)

**Soft robots** - I developed a method to integrate flexible silicon parts that can be easily design and built at a very low cost (>1$). I designed a soft starfish robot as a proof of principle.

{% include image.html src='img/poppy_soft.gif' col='col-md-8' sub="A robot with flexible parts."%}

For more information: [[Github soft starfish]](https://github.com/poppy-project/poppy-soft-starfish) [[Github soft connector]](https://github.com/poppy-project/poppy-soft-connector) [[Forum Thread]](https://forum.poppy-project.org/t/poppy-soft-connector/2152)

### Laboratory Robotics

Between 2015 and 2018, I lead a team of interdisciplinary researchers in a Chemistry lab on the [digitization of Chemistry](../chemobot). As a trained roboticist, I developed a set of tools to help less experienced programmers develop automated laboratory devices and robots in the lab. I present below the tools I have developed, but more are accessible on the [Cronin group Github page](https://github.com/croningp).

{% include anchor.html id="commanduino" %}
#### Commanduino - Arduino control in Python

The [Commanduino](https://github.com/croningp/commanduino) library is a Python library which is used to communicate with Arduino devices via Python, as opposed to hardcoding the desired behavior onto the Arduino itself.

I wanted to introduce modularity in the design of Arduino based robots. To add a new device (motor, servo, sensor), one should only need to add a few lines of code on the Arduino board. The device would then be controllable via Python on the connected computer. Strangely, this was not available off-the-shelf when I started this work, it required to build an Arduino library functioning like an object oriented library, which is not feasible by default. The following diagram shows the design of Commanduino, highlighting the layers of communication.

{% include image.html src='img/cronin_arduino.png' col="col-md-10" sub="Architecture of the Commanduino layers of communication."%}

With Commanduino, an Arduino main file becomes very simple to write as you only have to focus on the device you want to control. In the example below we register one servo on pin 9.

{% include image.html src='img/cronin_code_arduino.png' col="col-md-10" sub="Code on the Arduino side."%}

That's it, and adding a new device will only be a few lines of code, typically 2 lines and the associated library imports. You can now plug the board to a computer, and use the following code to control and read from the servo.

{% include image.html src='img/cronin_code_python.png' col="col-md-8" sub="Code on the Python side."%}

Commanduino makes quick iterative development possible using Arduino and Python, even for beginners. It is particularly useful when designing new robots without well defined specification, as it requires to adapt on the fly to the problem you encounter.

However, that amount of user side readability on an Arduino code, required fairly complex code architecture, and adding new devices is a job for advanced programmers.

**Libraries:** [[Commanduino]](https://github.com/croningp/commanduino) [[Arduino CommandTools]](https://github.com/croningp/Arduino-CommandTools) [[Arduino CommandHandler]](https://github.com/croningp/Arduino-CommandHandler). [Graham Keenan](https://github.com/ShinRa26) wrote the documentation and coded additional devices.

#### Pump control

I developed pycont, a Python library to control Tricontinent C3000 pumps. It is meant to be easy to use, and transparent such that when reading your program you can actually know what is going on. [Graham Keenan](https://github.com/ShinRa26) wrote the documentation. More details on [[GitHub]](https://github.com/croningp/pycont).

#### Modular syringe driver

I designed a small linear actuator with interchangeable tools that is very handy to develop custom laboratory robots. The appeal of this device is its modularity, as many different additions can be designed and printed. [Graham Keenan](https://github.com/ShinRa26) wrote the documentation. More details on [[GitHub]](https://github.com/croningp/ModularSyringeDriver) and [[OnShape]](https://cad.onshape.com/documents/56ab4447e4b0dff6d869c7ac/w/10403a3c4431f66501924e81/e/ad868b310df8ef7bb56f2516).


<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
{% include image.html src='img/cronin_syringe.png' sub="3D design of the modular actuator with interchangeable tools."%}
    </div>
    <div class="col-md">
{% include image.html src='img/cronin_syringe_real.png' sub="A modular syringe fully assembled."%}
    </div>
  </div>
</div>

#### Droplet tracking

A collection of software tools to handle various video related tasks, including recording a video, setting webcam parameters, and tracking moving droplets in a petri dish. More details on [[GitHub]](https://github.com/croningp/chemobot_tools).

#### Dropfactory robot

The [Dropfactory robot](https://github.com/croningp/dropfactory) is a great example of what can be made when combining the above tools. The design and code is entirely open source, see [[GitHub]](https://github.com/croningp/dropfactory).

{% include image.html src='img/cronin_dropfactory.gif' sub="Open source laboratory robot I developed."%}

I developed this robot to undertake [research on the efficiency of curious algorithm on the exploration of Chemical systems]('../chemobot#dropfactory'). Dropfactory can perform 300 droplet experiments a day in full autonomy (each experiment needs recording of 1m30s). Compared to previous robots, this is a 6-fold improvement and a major leap in reliability. This robot performed more than 20k droplet experiments while I worked in the Cronin group and routinely functioned for 12 hours per day.

{% include anchor.html id="start-up" %}
### Startup - Pollen Robotics and Luos

Together with Matthieu Lapeyre, Pierre Rouanet, and Nicolas Rabault, we co-founded [Pollen Robotics](http://pollen-robotics.com/).

{% include image.html src='img/pollen_team.jpg' col="col-lg-10" sub="The co-founders. From left to right: Pierre Rouanet, Jonathan Grizou, Nicolas Rabault, Matthieu Lapeyre"%}

Our objective was to make robotics more accessible by commercializing our tools for the quick creation of robots. Specifically a technology for modular robotic comprising a communication bus called Robus. Below was our attempt to explain that technology.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include youtube.html id='EwVGfkn3y_k' sub="Luos pitch to YC Startup School."%}
    </div>
    <div class="col-md">
    {% include youtube.html id='ula16zdZgDk' sub="Luos technology principle and example."%}
    </div>
  </div>
</div>

While I was at Pollen Robotics, we developed a variety of robots to showcase the technology versatility. Among which was a human size robotic arm and a small dynamic quadruped robot.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include youtube.html id='L4fB0rVJI8g' sub="Reachy - Human size robotic arm"%}
    </div>
    <div class="col-md">
    {% include youtube.html id='wQul6ANDb80' sub="Doggy - Robotic gaming platform"%}
    </div>
  </div>
</div>

The team took on another challenge to design a very cheap (<2$ in parts) educational robot in collaboration with the [Nathan](https://editions.nathan.fr/) french publishing house. The resulting product is called [Robot Labo](http://robotlabo.nathan.fr/) and has been commercialized in physical shops all over France for Christmas 2018.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
    {% include youtube.html id='fZtLp7vPts0' sub="Promotional video of Robot Labo."%}
    </div>
    <div class="col-md">
    {% include image.html src='http://robotlabo.nathan.fr/images/presentation/coffret-robot-labo.png' col="col-md-8" sub="Packaging of Robot Labo."%}
    </div>
  </div>
</div>

I voluntary departed from Pollen Robotics in 2018 following a pivot. This pivot lead to a split in the activities and the creation of a second start-up [Luos Robotics](https://www.luos-robotics.com). At the time of this writing, [Pollen Robotics](https://www.pollen-robotics.com/) is a robotic design studio that starts from an idea to develop a functioning product. [Luos Robotics](https://www.luos-robotics.com) is a start-up aiming to commercialize the Robus modular technology. We were awarded a [European SME Instrument h2020 grant](https://ec.europa.eu/programmes/horizon2020/en/h2020-section/sme-instrument) for this project.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-md">
{% include image.html src='img/pollen_logo.png' sub="Logo of Pollen Robotics."%}
    </div>
    <div class="col-md">
{% include image.html src='img/luos_logo.png' sub="Logo of Luos Robotics."%}
    </div>
  </div>
</div>

### Personal Projects

Personal projects are listed on the project page, under the ["Stuff I built"]({{ site.baseurl}}/projects#robot) section.

<div align="center">
  <a href="#">[Back To Top]</a>
</div>

---

<div align="center">
  {% include social-link.html %}
</div>
