---
layout: default
---

# Parametric Parts

I designed a set of libraries in OpenScad allowing to quickly design 3D printable robotic parts for the Poppy Project.

{% include image.html src='../open_robotics/img/poppy_ergojr_jumping.gif' col='col-lg-10' sub='The first ErgoJr robot, designed from parametric parts.'%}

Poppy creatures are built from [XL320 motors](http://support.robotis.com/en/product/dynamixel/xl-series/xl-320.htm) from [Robotis](http://en.robotis.com/). Motors are linked together with [parametrable frames](https://github.com/jgrizou/robotis-scad) that I designed with [OpenScad](http://www.openscad.org/). The resulting robots are controlled using the [pypot library](https://github.com/poppy-project/pypot), typically running on a Raspberry Pi. These robots aim at being low cost and easy to modify.

{% include image.html src='img/ergojr_variation.jpg' col='col-lg-10' sub='Robots built using parametric parts.'%}

## Libraries

OpenScad libraries for parametric parts:
- [[robotis-scad]](https://github.com/jgrizou/robotis-scad)
- [[segment-scad]](https://github.com/jgrizou/segment-scad)
- [[lego-scad]](https://github.com/jgrizou/lego-scad)
- [[raspberry-scad]](https://github.com/jgrizou/raspberry-scad)

## Robots

Example of robots made with the parametric part libraries:
- [[poppy-multipod-mini]](https://github.com/poppy-project/poppy-multipod-mini)
- [[poppy-snake-mini]](https://github.com/poppy-project/poppy-snake-mini)
- [[poppy-4wheels-mini]](https://github.com/poppy-project/poppy-4wheels-mini)
- [[poppy-dragster-mini]](https://github.com/poppy-project/poppy-dragster-mini)

{% include image.html src='img/poppy_mini_familly.png' col='col-lg-10' sub='The family of Poppy mini-creatures.'%}

The [poppy-ergo-jr](https://github.com/poppy-project/poppy-ergo-jr) and [poppy-ergo-starter](https://github.com/poppy-project/poppy-ergo-starter) robots started with parametric parts. Their latest version are now made with [onshape](https://www.onshape.com/) by [Matthieu Lapeyre](https://github.com/matthieu-lapeyre). See the hardware/README.md file of each repo to find back the openscad version.

## Contribute

Our robots are all open-source, [you are welcome to contribute!](https://forum.poppy-project.org/t/cfc-extending-the-poppy-mini-family-we-need-your-help/1346)
