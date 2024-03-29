I've hosted a Gemini capsule for a month now. I'd like to add
something to my capsule that is not just static text, so I decided to
make an orbit. An orbit is a bunch of Gemini capsules linking to each
other in a ring. Each page has a link to the next and the previous
page in the ring. This was popular on the early web under the name
"webrings". To make the orbit resilient to link rot, each navigation
link goes via a central orbit service.

The orbit is called [Omloppsbanan] [Omloppsbanan] ("the orbit" in
Swedish) and is now live. At the time of writing only my own page is
in it. The bar for participating in the orbit is very low. If you have
any relation to Sweden or the Swedish language, you are welcome to
join. Please do!

[Omloppsbanan]: <https://portal.mozz.us/gemini/raek.se/orbits/omloppsbanan/>

Why make this orbit? During my first days browsing around on Gemini I
found several capsules by Swedes. Is Gemini especially popular here? I
don't know. My goal for Omloppsbanan is for Swedish geminauts to be
able to find each other. Chances are that many of them live in the big
university cities. Maybe your neighbor in Gemini space is also your
neighbor AFK?

To the orbit main page I added some ASCII art and a bit of poetry that
I made. I had an idea about the logo and I found [a good tutorial for
ASCII art] [ASCII] on YouTube. (I had never done ASCII art before. I don't
usually write poetry either.) I really like when people adorn their
pages with beautiful (ASCII) art and playful writing, so I hope I
could contribute something myself.

[ASCII]: <https://www.youtube.com/watch?v=o5v-NS9o4yc> "ASCII-art Techniques & Animation Tutorial - Part 1"

## Retrograde

I decided to write my own software called [Retrograde] [Retrograde] to
serve the orbit. [LEO] [LEO], the original Gemini orbit, uses a
software called Molniya. So why not use that? The biggest reason is
that I enjoy coding in Python. So coding it is just fun in its own
right.

[Retrograde]: <https://portal.mozz.us/gemini/raek.se/projects/retrograde/>
[LEO]: <https://portal.mozz.us/gemini/tilde.team/~khuxkm/leo/> "Low Earth Orbit (LEO)"
[Molniya]: <https://tildegit.org/khuxkm/molniya>

A second reason is that I had just read how Antenna – a "reverse"
aggregator – managed to collect new posts in Gemini space so quickly
without any crawling. The trick was letting the user submit their feed
to Antenna when a new post was made. Page discovery becomes
immediate. Molniya works by checking backlinks from geminispace.info,
which are updated weekly. I wanted to combine the two ideas: an orbit
updated by user submissions where the join delay is at most a few
minutes.

I also added some ergonomic features. The links required by the orbit
to be in the page contain the page URL in the query. Escaping URLs by
hand is simply not very fun, so I also added a way for the orbit to
automatically generate all the correct links given the non-escaped
(and non-normalized) URL as an input.

[I put the code on GitHub] [gh-retrograde] mostly so that anyone who
is interested can read it. I haven't put any effort into the
documentation yet, so I don't expect anyone to figure out how to use
it. [The source for my capsule] [gh-capsule] is on GitHub as well. My
ambition is to at least add installation instructions and release
Retrograde on PyPI.

[gh-retrograde]: <https://github.com/raek/retrograde> "Retrograde Source Code"
[gh-capsule]: <https://github.com/raek/raek-gemini-capsule> "Source Code for my Capsule"

While working on Retrograde, I also released a small Python library
called [gemurl] [pypi-gemurl]. Its main feature is a URL normalization
function, which is useful to have and took some time to write. It was
supposed to be a part of an unfinished Gemini client, but I needed the
code for Retrograde. It's well tested, has documentation and is
published to PyPI.

[pypi-gemurl]: <https://pypi.org/project/gemurl/> "gemurl on PyPI"
