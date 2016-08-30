---
layout: post
title: "Seaglide"
date: 2014-8-12
---

As a part of my summer at Edgerton, I also occasionally helped with the two-week
long [Seaglide](http://edgerton.mit.edu/k-12/sea-glide-camp) workshop.
Students were given the opportunity to build an
[underwater glider](http://seaglide.net); it would take in water and
release it periodically to change its buoyancy and cause it to sink and float.
The lift created by the wings propelled the glider forwards as it sunk and rose.
This was designed over at the Carderock naval base, where full scale gliders
that run for months are deployed over the Atlantic Ocean to collect data
regarding the ocean.

After the program was over, I was able to build one out of the extra materials. I started by preparing the outer casing.

<div class="center">
<img src="{{ site.url }}/assets/seaglide/shell.jpg" style="width: 50vw;">
</div>

Next, I soldered the circuitry unto the protoboard and the Arduino Pro mini and built the pump system controlled by a servo motor that would control the buoyancy change.

<div class="center">
<img src="{{ site.url }}/assets/seaglide/breadboard_arduino.jpg" style="width: 25vw;">
<h6><em> Protoboard and Arduino</em></h6>
</div>

<div class="center">
<img src="{{ site.url }}/assets/seaglide/pump.jpg" style="width: 25vw;">
<h6><em>Syringe system </em></h6>
</div>

The backing of the 100cc syringe was replaced by copper plated bb gun pellets in
a 3D printed case attached to the servo motor. This gives the glider a movable
mass that allows the change in buoyancy. A push button (green and yellow wire
in the picture, button not shown in the picture) is also attached to the
syringe so the glider would be able to sense when to stop taking in
water. Another sensor, the reflective sensor, is used for the glider to sense
when to stop releasing water. The power supply is 5 triple A batteries with a
switch to turn the glider on and off.

<div class="center">
<img src="{{ site.url }}/assets/seaglide/insides.jpg" style="width: 25vw;">

<h6><em>
Above can be seen the internal parts.  
</em></h6>
</div>

<div class="center">
<img src="{{ site.url }}/assets/seaglide/final-glider.jpg" style="width: 25vw;">

<h6><em>
The glider at its completion.
</em></h6>
</div>

The final glider can be seen above. In fact, the students under the Seaglide
program were given the opportunity to also add sensors to the front of their
glider. Those materials ran out, so I did not have a chance to build it. The
students were also given a chance to test their glider out in the MIT tow tank.
Alas, I tested mine out in the kitchen sink. It was successful in the sense that
it sunk and rose, although the reflective sensor required finer calibration.

Building this took me about 3 days to assemble and another day or two to fix
mistakes and to get it to work. The main reason behind my mistakes were due to
my dependence on written instructors instead of an instructor. I did not build
this at the same time the students built this, so many errors I made could have
been avoided with guidance from one of teachers of the workshop. For example,
the reflective sensor is a recent addition to the glider, so there were vague
instructions written up for that part of the glider. After stumbling around and
trying to make sense of the instructions, I taught myself more about the sensor
and was able to figure out where to attach it and how to calibrate it.
