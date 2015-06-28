---
style: Default
---

## 2 Wheel Drive Robot

I developed a small 2 wheel drive robot. It is Arduino based with most of the mechanical and electronic parts coming from the [polulu website](https://www.pololu.com/).  There is a small gripper in front that is convenient to perform small tasks with the robot.

I did most of the code on-board including the communication protocol, the encoder management, the speed and position control, LED control, gripper control. The communication with the computer is via Xbee, there is a Python library to control the robot. Finally, there are some Matlab tools to simulate the robot and make it follow a virtual line.

<a class="btn btn-block btn-github btn-lg center" href="https://github.com/jgrizou/robot_2WD" target="_blank">
<i class="fa fa-github"></i> The robot on GitHub
</a>

<div class="grid">
  <div class="media-item media-item--width2"> {{ "qQ2ebGT-qu8" | youtube }} </div>
  <div class="media-item"> <img src="img/front_1.jpg"> </div>
  <div class="media-item"> <img src="img/top.jpg"> </div>
  <div class="media-item"> <img src="img/left.jpg"> </div>
  <div class="media-item"> <img src="img/right.jpg"> </div>
  <div class="media-item"> <img src="img/back.jpg"> </div>
  <div class="media-item"> <img src="img/front_2.jpg"> </div>
</div>

<script>
$(window).ready( function() {
  // init Isotope
  var $grid = $('.grid').isotope({
  layoutMode: 'packery',
  itemSelector: '.media-item',
  packery: {
  gutter: 5
  }
  });
});
</script>
