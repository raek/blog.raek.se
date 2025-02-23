I'm getting ready to operate portable with my QMX. For that I built and trimmed
yet another EFHW antenna.

The materials I used were:

* 22m (before trimming) of Sotabeams lightweight antenna wire (bright yellow)
* Two 15m of 2mm paracord (bright blue)
* Two tent stakes (bright red)
* 7m of RG58 coax
* One homemade UNUN (see Figure 1)

## 49:1 UNUN

<div class="figure">
  <p><a href="files/portable_unun.jpg"><img src="files/portable_unun_thumbnail.jpg"></a></p>
  <p>Figure 1. Homemade portable 49:1 UNUN without lid</p>
</div>

The UNUN is eye-catching for several reasons. First, it's fairly large and heavy
due to the Fair-Rite 2643251002 core (same weight as a FT240-43). I had a spare
transformer lying around since the attic antenna build (I built two to test them
back-to-back).

Second, the antenna wire connector is pretty unconventional: it's an alligator
clip mounted on the surface of the box. I used it as a binding post (mostly
because I didn't have any good ones lying around). Actually, I quite like it. It
has a built in spring, it is easy to open and close, and it works very well with
"raw" wire stripped in the field.

Third, the box didn't have any flanges with holes where I could tie the paracord
and wire, so I simply bolted a wooden "flange" on top. It works.

## Taking the antenna outside

I packed my bag with the antenna, some tools, my QMX and all its paraphernalia.
I'm surprised the stuff managed filled the whole bag. Then I went about 50
meters to the closest playground and strung up the antenna between two trees
(see Figure 2).

<div class="figure">
  <p><a href="files/antenna.jpg"><img src="files/antenna_thumbnail.jpg"></a></p>
  <p>Figure 2. Antenna put up between two trees</p>
</div>

My original idea was to use an inverted vee configuration, but in a previous
attempt the top segment of my 6 meter high fishing pole snapped. So I this time
I used the trees as support instead. The antenna wire was about two meters above
ground. Not ideal, but what I could accomplish easily.

I also got to improve my skills for tying knots. For both pieces of paracords, I
used a taught line hitch on the tent stake side and a bowline on the antenna
wire side.

## Trimming the antenna

I intentionally cut the antenna wire way to long. Similarly to the attic
antenna, I cut off a piece at a time and measured the SWR on my NanoVNA, which I
had also brought outdoors. This time I only care dabout the 40m and 20m bands,
and prioritized 20m over 40m. The 20m band seemed to be a favorite for portable
operation among the hosts of The European Ham Radio Show. I've also had great
luck with the 20m band at daytime.

I got the SWR minimum at 20m roughly at the digimodes part of the band (around
14.074 MHz). From memory (I forgot to store the results) I recall that I got
less than 1.2:1 SWR at the minimum and decided it was good enough. The 40m SWR
minimum was clearly a bit below the low band edge (the dreaded "end effect"
strikes again?) and the SWR at the minimum was surprisingly bad, above 2:1 if I
recall correctly. I have no idea why the SWR was worse one the fundamental
compared to the first overtone.

## A quick test run

When the antenna was trimmed, I wanted to try it out! I unpacked my laptop and
my QMX and its paraphernalia onto a park bench (see Figure 3). I planned to use
a 12V moped battery, but I had left the PowerPole to DC plug cable at home.

<div class="figure">
  <p><a href="files/bench.jpg"><img src="files/bench_thumbnail.jpg"></a></p>
  <p>Figure 3. QMX and laptop on a park bench</p>
</div>

Luckily, I had also packed a 8 × AA battery pack with the connector that 9V
batteries usually have, as well as a matching cable (See Figure 4). The QMX runs
just fine off of AA batteries (but I haven't tested for how long yet).

<div class="figure">
  <p><a href="files/qmx.jpg"><img src="files/qmx_thumbnail.jpg"></a></p>
  <p>Figure 4. Closeup of the QMX and the AA battery pack</p>
</div>

Then I started WSJT-X and GridTracker on the laptop. I made a contact with PD7RF
on 20m FT8. Happy with that, I put down the antenna and packed everything back
into the bag. The whole thing took a little bit longer than an hour and fit well
into the family plans for the day.
