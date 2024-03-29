I made a new antenna back in August and it's time to write about it. I began the
project because I was not very pleased with my antenna on the balcony. It had
some parts close to the ground (and stuff made of metal), some parts
inconveniently high up (barely reachable with a ladder), was not cut to the
right length, and had a feedpoint outdoors. I wanted something more properly
constructed, with convenient access, and the possibility of future
modifications. The solution was to put an antenna in the attic.


## Description

Figure 1 shows a sketch of the new attic antenna, which is an end-fed halfwave
antenna (EFHW) for the 40m, 20m, 15m, and 10m bands.

<div class="figure">
  <p><a href="files/attic_antenna.png"><img src="files/attic_antenna_thumbnail.png"></a></p>
  <p>Figure 1. Sketch of the attic antenna</p>
</div>

The main radiating element is immediately under the ridge of the roof – as high
up it can be while still indoors. The roof is only 12 meters long, so the end
portions of the wire bend back down. I was very fortunate that there was a
plastic conduit for the old TV antenna from the attic south end down to a outlet
right next to my shack bench. This is a perfect feedpoint location for an
end-fed antenna.

The "feedpoint box" in the drawing contains two things: a common mode choke
(a.k.a. "balun") and a 49:1 impedance transformer (a.k.a. "unun"). The schematic
can be found in figure 2 and figure 3 shows what it looked like before I hot
glued down the toroids. The box is a cheap food box that I mostly used to keep
moisture out and make it easy to open and inspect.

<div class="figure">
  <p><a href="files/feedpoint_box_schematic.jpg"><img src="files/feedpoint_box_schematic_thumbnail.jpg"></a></p>
  <p>Figure 2. Schematic of the feedpoint box</p>
</div>

<div class="figure">
  <p><a href="files/feedpoint_box_photo.jpg"><img src="files/feedpoint_box_photo_thumbnail.jpg"></a></p>
  <p>Figure 3. Photo of the feedpoint box</p>
</div>

The common mode choke and the impedance transformer are interesting topics on
their own, so I will write about those in separate posts.


## Build

I had a 25 meter spool of 1.5 mm² houshold wire. I cut a 22 meter main part and
a 2.5 meter counterpoise from it and marked every five meters and every one
meter with some tape. I put the long part up in the ridge of the roof – there
was a small gap at the end of the beams where I could snake it though.

After I had built the feedpoint box, I invited a friend over for an antenna
trimming night. We used a NanoVNA H4 and a laptop to measure the SWR of the
antenna over the HF range.

<div class="figure">
  <p><a href="files/me_in_the_attic.jpg"><img src="files/me_in_the_attic_thumbnail.jpg"></a></p>
  <p>Figure 4: Me in the attic</p>
</div>

The main wire was far too long at the beginning and the resonsances were too low
in frequency (as expected). We ended up cutting and measuring at these lengths:

* 22.0 m – the starting length
* 21.5 m
* 21.0 m
* 20.5 m
* 20.25 m
* 20.125 m
* 20.0 m
* 19.75 m
* 19.5 m
* 19.4 m
* 19.3 m
* 19.2 m
* 19.1 m
* 19.0 m
* 18.9 m
* 18.8 m
* 18.7 m – final length

I was aiming for good SWR in the 40 meter band, but I also kept an eye on the
20, 15, and 10 meter bands. I was surprised that the resonance for 40 meters was
slightly lower in frequency comparing to the ones of 20, 15 and 10 meters. I
don't know why this happens, but I have heard Callum McCormick M0MCX (the DX
Commander guy) mention "the end effect". Maybe that has something to do with it?
I haven't researched this yet. Another mystery is why there seems to be some
kind of resonance at 80 meters. Maybe it acts as a quaterwave antenna there?

I had to choose between good SWR on the 40 meter band or on the other bands. I
chose 40 meters because it was the only band I had a working transceiver for at
the time. Plus, I figured I could always add a short extension wire in the
future, if needed. The final SWR plot can be seen in figure 5. There is [a
Touchstone file of the measurements][s1p] as well.

<div class="figure">
  <p><a href="files/efhw_swr.png"><img src="files/efhw_swr_thumbnail.png"></a></p>
  <p>Figure 5. Attic antenna SWR plot</p>
</div>

[s1p]: files/efhw_18.7m.s1p "Attic antenna SWR measurement"

Lastly, I ran an RG-58 coax down the plastic conduit which used to hold the TV
antenna coax. I had to crimp one end up in the heat and dust of the attic
(figure 6 gives you an idea), but it went pretty smoothly.

<div class="figure">
  <p><a href="files/crimp_in_the_attic.jpg"><img src="files/crimp_in_the_attic_thumbnail.jpg"></a></p>
  <p>Figure 6. Crimp in the attic</p>
</div>

Down by the shack desk, I removed the old TV antenna outlet, put a lid in its
place, and ran the coax along the skirting to the shack desk. All this is hidden
behind a bookshelf. Neat, if I may say so!

<div class="figure">
  <p><a href="files/outlet.jpg"><img src="files/outlet_thumbnail.jpg"></a></p>
  <p>Figure 7. Antenna outlet behind bookshelf</p>
</div>



## Usage

I tested the antenna briefly when I finished it using my monoband BITX40
transceiver. It seemed to work equally well in receive. I did not call CQ that
many times because I quickly got into my next project: building the multiband
QMX transceiver kit from QRP Labs. I built the QMX in the autumn and started
using FT8 on it in the winter. At first I only used the 40 meter band, but later
on I also worked 20 meters, 30 meters and 60 meters. I've used a Z-match tuner
(my own clone of the EMTECH ZM-2) in the shack, which worked susprisingly well
for the 60 and 30 meter bands which the antenna was not made for.

Overall, I'm very happy with the antenna. The biggest win is that I now have a
coax at my desk permanently. No more rolling out the coax across the floor and
out the balcony door! I still have many things left to do. It's February now,
and I should probably measure the SWR again and see if it has changed. I think
it has, because I get lower SWR on 20 meters than 40 meters now. I should also
try to call CQ on SSB again. FT8 (and also FT4) has just been so much fun! I
don't have much leisure at the moment, so the digital modes have really given me
a chance to make contacts in the time I have.
