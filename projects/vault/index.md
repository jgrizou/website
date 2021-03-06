---
layout: default
---

# This interface can read your mind

Last update: August 2019

*A web-app to explain self-calibrating interfaces.*

> UPDATE: I am working on an [interactive paper to explain self-calibrating interface](https://docs.google.com/document/d/1ExWC2IDRwSTDM3E_KOHTg1AtcucBwccSggV3tad3ciA/edit?usp=sharing). The information below will be better understood in light of the draft paper linked above. Comments welcomed directly in the document.

## Introduction

Below is a typical user interface. It is a code entering device. To enter a code, you look at the digit you want to type, if it is yellow you click on the yellow button. If it is grey, you click on the grey button. And the machine will find out the digit you have in mind by elimination.

<div class="container">
  <div class="row align-items-center justify-content-center">
    <div class="col-lg-4 col-md-6 col-sm-8 col-12">
      {% include image.html src='img/demo_1x2_2.gif' sub='The user clicks on two colored buttons.'%}
    </div>
  </div>
</div>

With two big colored buttons, this interface is designed to remove most user choices and channel you to behave in one standardized way. The aim is normative, it is more efficient and convenient for the designers if we all behave the same way, and it is also easier to predict your future actions. Think of apps like Instagram or Twitter, designers have done a great job at funneling our interaction there.

But let me show you another way to interact with digital devices.

Below is the same interface but buttons have no predefined colors. You get to decide the buttons' color in your mind, and the machine adapts to your preferences on the fly.

<div class="container">
  <div class="row align-items-center justify-content-center">

    <div class="col-lg col-md-4 col-sm-4 col-6">
    {% include image.html src='img/demo_3x3_fullpad_1.gif' sub='User 1 choice.' %}
    </div>

    <div class="col-lg col-md-4 col-sm-4 col-6">
    {% include image.html src='img/demo_3x3_fullpad_2.gif' sub='User 2 choice.' %}
    </div>

    <div class="col-lg col-md-4 col-sm-4 col-6">
    {% include image.html src='img/demo_3x3_fullpad_3.gif' sub='User 3 choice.' %}
    </div>

  </div>
</div>

Notice how, once revealed, the color patterns on buttons are different for each user. This reflects their personal preferences. Each user typed in the same digit but they used the buttons differently to do so. Yet the machine was able to adapt, finding both what the user wanted to do (enter the digit 1) and how it was trying to do it (the colors associated to each button).

I call these *self-calibrating interfaces* because they adapt to your preferences while you are using them.

You will find below several options to play with these interfaces and gain a deeper understanding of how they work.

## Learning tracks

Quick access: [[Crack it]](#crack-it) [[Try it]](#try-it) [[Grasp it]](#grasp-it)

{% include anchor.html id="crack-it" %}
### Crack it - the open vault challenge

> When you teach a child something you take away forever his chance of discovering it for himself - Jean Piaget

If you want to really get it, you should reinvent it for yourself. So I have designed a challenge tailored for participants to gain an intuitive understanding of self-calibrating interfaces.

In this challenge, you will see me entering a secret code in various interfaces. Your goal is to crack the code and enter it correctly into the interface. By doing so you are forced to think like the machine.

The challenge is divided into levels of increasing complexity, designed for a progressive learning experience. Clues and take home messages are available if you get stuck.

<a href="challenge" class="btn btn-light btn-lg active" role="button" aria-pressed="true">Go to challenge</a>

{% include anchor.html id="try-it" %}
### Try it

If you do not have time for the challenge, you can directly try any version below.

{% include vault_demo_quick_access.html %}

For each version, a small explanatory text is provided along with a didactic video. If this is your first time, I recommend going through each version in order.

<a href="demo" class="btn btn-light btn-lg active" role="button" aria-pressed="true">Go to demo</a>

{% include anchor.html id="grasp-it" %}
### Grasp it - look under the hood

If you want to see how it works, I have built a little window into the machinery powering the interface. It provides detailed feedback about the current state of the machine.

It also allows you to challenge the interface in complex ways. For example, I sometimes use these advanced versions to fool the machine into making a false prediction, or to select my actions such that it takes the longest possible time to identify a digit.

<a href="tuto" class="btn btn-light btn-lg active" role="button" aria-pressed="true">Go to tutorial</a>


## Wait but why?

Because I have consistently failed to explain what a self-calibrating interface does to other researchers, friends or family in a few minutes. This web application is my attempt at explaining, showing, and getting people to feel what a self-calibrating interface does in one minute on my phone.

I also have the intuition that this technology can be useful. But I cannot figure out how on my own, I am too involved in the research and find it hard to think outside the box. By implementing this technology into an easy-to-share demonstration, I am hoping to reach a variety of people. And maybe one day someone will figure out a place to apply it for good. If you think of some application, feel free to [contact me]({{ site.baseurl }}/about/#standing-invitation).

## Resources

1. **The Open Vault Challenge - Learning how to build calibration-free interactive systems by cracking the code of a vault.** Grizou, J. (2019). *International Joint Conferences on Artificial Intelligence.*
[[pdf]](https://arxiv.org/pdf/1906.02485.pdf)
[[doi]](https://doi.org/10.24963/ijcai.2019/942)
[[project]]({{ site.baseurl }}/projects/vault)

Detailed information, papers and code available on [this project page]({{ site.baseurl }}/projects/thesis).

Feel free to [get in touch]({{ site.baseurl }}/about/#standing-invitation).
