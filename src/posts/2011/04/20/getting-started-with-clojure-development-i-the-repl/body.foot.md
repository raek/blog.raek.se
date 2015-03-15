<em>This is the first post of one my ongoing attempt to write a series
of blog posts about how to get started with development in
Clojure. This post will cover a beginner's first encounter with the
Clojure Read Eval Print Loop.</em>

<em>This post assumes a UNIX-like environment. Some details might vary
from OS to OS (especially for Windows). In those cases, study the
documentation</em><em> related to your platform </em><em> for the
mentioned applications.  </em>

<strong>So, you've heard some interesting things about this language
called Clojure...</strong> Good. When you play around with an
<em>interactive</em> programming language (which Clojure is a prime
example of) you usually do it though a shell of some sort. In Lisp
languages, this shell is traditionally called the REPL, which stands
for Read Eval Print Loop.

The question I can almost hear you think is: <strong>"How do I install
Clojure?"</strong> The answer to that question, which is somewhat
unusual, is: <strong>"You don't."</strong> Clojure's approach to
language and library versions is similar to Virtualenv of Python or
RVM of Ruby. To launch Clojure you use what's usually called a build
tool. Since they do more than just build tasks, so you can think of
them as "Clojure environment tools". Two of the most common ones are
Leiningen and Cake. Here, I will only cover Leiningen, but Cake works
nearly identically for basic tasks.

Now, what you <em>do</em> install is <strong>Leiningen</strong>:

<ul>
	<li>Download the <a href="https://github.com/technomancy/leiningen/raw/stable/bin/lein"><code>lein</code> script</a> available <a href="https://github.com/technomancy/leiningen">from the project page</a>.</li>
	<li>Put the file in a directory where you keep executables. I keep mine in <code>~/.bin/</code></li>
	<li>Make it executable: <code>chmod a+x lein</code></li>
	<li>Ensure that directory with executables is on the PATH. I do this by having the following in my <code>~/.profile</code> file:
<pre><code>PATH=$PATH:/home/raek/.bin
export PATH</code></pre>
This makes lein available both in applications started from Bash and in Gnome((restart)); just change the <code>/home/raek/</code> to your own home directory.</li>
	<li>Run <code>lein</code> once to let it download the files it needs. The files are placed in <code>~/.lein</code> and <code>~/.m2</code></li>
	<li>Run <code>lein repl</code> to get a Clojure REPL!</li>
	<li><em>Optional:</em> Install <code>rlwrap</code> using the package manager of your OS to get a better REPL experience. Otherwise JLine is used which does not support UTF-8.</li>
</ul>

((restart)): You might need to restart the X server for this change to be effective.

With a bare REPL in a terminal you can do much, but the lack of
editing and saving abilities can make it tiresome in the long run. I
therefore recommend to use an ordinary text editor to write the code
and then send the code to the REPL. The simplest way to accomplish
this is to simply copy and paste the code, but more sophisticated
editors provide more convenient methods (I will shortly show this can
done in Emacs).

Restricting oneself to only the REPL has some serious limitations and
because of this I don't recommend this approach in general, except for
learning (for that it may indeed be very useful) and trivial
projects. So far I haven't mentioned how divide code into multiple
files, how to use third party libraries or how to specify the version
of Clojure to use. For that, you need to set up a Leiningen
project. This is the topic for the next (upcoming) part of this blog
post series.

In Emacs, you can interact with the REPL by following these steps:

<ul>
	<li>Install <code>clojure-mode</code> using <code>package.el</code> by following the instructions on the official <a href="http://dev.clojure.org/display/doc/Getting+Started+with+Emacs">Getting Started with Emacs</a> wiki page.</li>
	<li>Execute <code>M-x customize-variable RET inferior-lisp-program</code> and configure it to use <code>lein repl</code> as the program.</li>
	<li>Open a <code>.clj</code> file, or run <code>M-x clojure-mode</code> in a buffer (e.g. <code>*scratch*</code>).</li>
	<li>Press <code>C-c C-z</code> to start the Clojure REPL.</li>
	<li>Use <code>C-x C-e</code> at the end of an expresison to evaluate it or <code>C-M-x</code> to evaluate the expression spanning between the outermost parentheses surrounding the point.</li>
</ul>

This is it for now. Happy hacking!

`;; raek`
