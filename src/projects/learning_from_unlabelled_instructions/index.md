---
style: Default
---

## Learning from Unlabelled Instructions

<div class="well"> Can a robot learn a new task if it does not known how to interpret human instructions? </div>

The challenge we addressed in this work is how a system/agent/robot learning a new task can be instructed by a human using its own preferred teaching signals and where the mapping between these signals and their meanings is unknown to the robot before hand. In such cases, the system/agent/robot needs to estimate simultaneously what the task is and the mapping from signals received from the user to their meanings. We assume the number of possible meanings is known in advance.

To quickly understand the principles and specific challenges related to this work, you can watch the following videos. I should however warn you, they are only slides and me talking, watch at your own risk! You should also have a look at the related publication at the end of the page.

<a class="btn btn-block btn-github btn-lg center" href="https://github.com/jgrizou/lfui" target="_blank">
<i class="fa fa-github"></i> Code is available on GitHub
</a>

### Part 1: Introduction

In this fisrt video, I am presenting the global scientific challenge behind this work as well as the specific framework we will consider.

{{ "rPGYqylud1k" | youtube }}

### Part 2: How it works

In this video, I explain how we tackled this problem in a toy scenario, provide an intuitive visualization of the algorithm principle, and present experimental results from simulated and online experiments.

{{ "NFKh6V9zgaY" | youtube }}

### Part 3: Planning

In this video, I investigate how the robot can act in order to learn faster. Our problem is different from usual learning problems and we will discover that it therefore requires a specific approach.

{{ "1sshBzWM7u8" | youtube }}

### Related Publications

{{ ["grizou2014learning", "iturrate2015exploiting", "grizou2014calibration", "grizou2014interactive", "grizou2013robot"] | pub_list}}

---

#### Let me explain the project title:

**Learning:** means the system/agent/robot should be able to perform something new at the end of the day, which should not be programmed by hand in the system.

**Learning  from Instructions:** means the system/agent/robot will learn by receiving concrete instructions (e.g. “go left”, “go right”, “it was correct”, “it was incorrect”). Such instructions are conveyed by a human (or another machine/system/agent/robot) through the form of a symbolic event or a raw signal (speech, gesture, brain activity, …) represented by a feature vector.

**Learning  from Unlabelled Instructions:** means the instructions are known to be of a specific set, i.e. there exist hidden labels (e.g. only feedback instruction  of type correct/incorrect). However the system/agent/robot do not known in advance the mapping between raw instruction signals (speech, gesture, brain activity, …) and their labels/meanings.
