<i>Parts:</i> <b>1</b> <a href="/2023/06/26/finishing-the-bitx40-case/">2</a>

My [BITX40][BITX40] needs a proper case. It's an amateur radio transceiver kit
for the 40 meter band by Ashhar Farhan VU2ESE. I originally tested the kit by
mounting it to an MDF board. It's not very ergonomic nor very portable.

[BITX40]: https://www.hfsignals.com/index.php/bitx40/ "BITX40 Website"

<div class="figure">
  <p><a href="files/al_fresco.jpg"><img src="files/al_fresco_thumbnail.jpg"></a></p>
  <p>Figure 1. BITX40 test build on an MDF board</p>
</div>

I finally decided on a new case: a Bahar BDA 40004-A6(W200). I bought mine on
AliExpress. It's very blue! I consider it to be an homage to [Pete Juliano
N6QW][N6QW] who uses his "[Juliano Blue][blue]" paint for his homebrewed rigs.

[N6QW]: https://www.n6qw.com/Bitx40.html "The Bitx40 Project as built by N6QW"
[blue]: https://www.n6qw.com/Images/Bitx40/20161211_175811.jpg "Example of Juliano Blue"

<div class="figure">
  <p><a href="files/BDA-40004-A6W200-1-705x705.jpg"><img src="files/BDA-40004-A6W200-1-705x705_thumbnail.jpg"></a></p>
  <p>Figure 2. The new Bahar BDA 40004-A6(W200) enclosure</p>
</div>

The blue top and bottom parts are made from steel, and the front and back panels
are made from black plastic, about 2.5 – 3.0 mm thick. It is all held together
with eight screws. The inside of the panel has a convenient 0.5 × 0.5 mm grid.

<div class="figure">
  <p><a href="files/panel_back.jpg"><img src="files/panel_back_thumbnail.jpg"></a></p>
  <p>Figure 3. Back side of one of the plastic panels (unrelated <a href="https://tokipona.org/">toki pona hieroglyphs</a> in the background)</p>
</div>

It took a while to figure out the placement of the components on the front
panel. There was not much space left in the end. I cut out the rectangle for the
LCD first using a rotary tool and a file. Then I drilled the holes. I don't have
a drill stand, so upon close inspection you'll see that the holes aren't lined
up perfectly straight.

<div class="figure">
  <p><a href="files/front_panel_holes.jpg"><img src="files/front_panel_holes_thumbnail.jpg"></a></p>
  <p>Figure 4. Front panel holes</p>
</div>

Of all the components I mounted, I had most problems with the four 3.5 mm jacks.
It turns out that most jacks I could find were made for much thinner panels.
They were probably made for metal, not plastic. The jacks I got also broke.
Maybe the fastening nut deformed, or the threads wore out (I could only use the
outermost bit). In any way, some of the nuts popped loose when I tightened them
or when I pulled out a plug. I had bought ten of them and ended up using the the
four of them that seemed to be intact the most.

<div class="figure">
  <p><a href="files/front_panel_holes_and_components.jpg"><img src="files/front_panel_holes_and_components_thumbnail.jpg"></a></p>
  <p>Figure 5. Front panel holes and components</p>
</div>

The front panel components are as follows. To the left:

* Top: Function button
* Middle: Fine tune button
* Bottom: Volume knob

In the middle:

* Top: LCD display
* Bottom: 3.5 mm jacks, left to right:
  * Headphones
  * Microphone
  * PTT button
  * Iambic key

To the right:

* Top left: TX indicator LED
* Top right: PTT switch
* Bottom: Frequency knob

<div class="figure">
  <p><a href="files/mounted_front_panel.jpg"><img src="files/mounted_front_panel_thumbnail.jpg"></a></p>
  <p>Figure 6. Front panel with components mounted</p>
</div>

I tried to place the components so that it would be easy to use both hands
simultaneously. I had some uses cases in mind:

* **Tuning around and listening.** Tune with the right hand, and continuously
  adjust volume with the left (due to the lack of AGC)
* **Talking.** Flip the PTT switch back and forth with the right hand, and
  adjust volume with the left.
* **Fine-tuning and adjusting settings.** Hold the fine tune button (or press
  the function button) with the right hand and adjust the tuning knob with the
  right.

I added extra room between the PTT switch and the tuning knob. It was barely
enough. If the switch is in the down position it is slightly in the way.
Originally, I wanted "up" to be "transmit" (as in, the signal goes up into the
air), but I now I'll make "up" be "receive" so that the switch is least in the
way while tuning.

<!--div class="figure">
  <p><a href="files/mounted_front_panel_back.jpg"><img src="files/mounted_front_panel_back_thumbnail.jpg"></a></p>
  <p>Figure X. FIXME</p>
</div-->

Next I drilled four holes in the bottom side for M3 screws. The case has rubber
feet that conveniently keep the screw heads from touching any surface the case
stands on.

<div class="figure">
  <p><a href="files/underneath.jpg"><img src="files/underneath_thumbnail.jpg"></a></p>
  <p>Figure 7. Bottom of the case</p>
</div>

I mounted the circuit board on hexagonal brass standoffs. It sits very securely!
In the future I would like to be able to stack more boards on top of the main
one. (I've been thinking about making it work on more bands.)

<div class="figure">
  <p><a href="files/mounted_pcb.jpg"><img src="files/mounted_pcb_thumbnail.jpg"></a></p>
  <p>Figure 8. The BITX circuit board mounted in the case</p>
</div>

I've just started wiring up everything. Previously I used the wires that came
with the kit. I had twisted pairs of wires to reduce interference. This time I
will use shielded cable for the headphone and microphone signals as well as
RG316 coaxial cable for the VFO and antenna signals.

The Raduino is a small board that sits on the back of the display. The original
one is a simple VFO made from an Arduino Nano, a potentiometer for input, and an
Si5351 for frequency synthesis. Allard Munters PE1NWL has since added many new
features in [his sophisticated variant][amunters] of the Raduino software.

[amunters]: https://github.com/amunters/bitx40 "BITX40 sketch for Raduino by Allard Munters PE1NWL"

Many of the new features require hardware modifications and I plan to apply most
of them. That means a few extra components and a lot of extra wires than need to
be attached down to the connectors on the back of the Raduino. To manage that I
desoldered the connectors, added pin headers, and soldered a prototype board on
the back of the Raduino. That way there should be plenty of room for attaching
the new wires and adding the extra components.

<div class="figure">
  <p><a href="files/testing.jpg"><img src="files/testing_thumbnail.jpg"></a></p>
  <p>Figure 9. Testing (the lack of) extra voltage regulator capacitors on the Raduino</p>
</div>

At the moment I'm experimenting with fixing the well known "tuning tick" problem
of the BITX40. The Raduino needs more power filtering. Otherwise loud clicks are
heard whenever the frequency is adjusted. Now that I have the extra protoboard I
decided to redo my previous fix and add the components to the board instead.

## Links

* [Topic on Groups.io for this blog post](https://groups.io/g/BITX20/topic/97590084)
