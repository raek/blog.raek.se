I recently realized that of the core Clojure regex functions
(`re-pattern`, `re-matcher`, `re-matches`, `re-groups`, `re-find`,
`re-seq`) I was completely unaware of how `re-matcher`, `re-matches`,
`re-groups` were supposed to be used. Their names hint that they are
useful for something, but I had never needed to use them. To
understand them, I first had to dive into the Javadoc a bit, more
specifically the [`java.util.regex`][java.util.regex] package.

[java.util.regex]: <http://download.oracle.com/javase/6/docs/api/java/util/regex/package-summary.html>

The are two basic concepts in the regex package: the `Pattern` and the
`Matcher`. A Pattern is what a Clojure regex literal produces and
<code>(re-pattern </code><i>pattern-string</i><code>)</code> can be
used to create one from a string.

<pre><code>user=&gt; <b>(def p (re-pattern "abc|def"))</b>
#'user/p</code></pre>

A `Matcher` is a stateful class used to find one or more matching
(sub)sequences of a string. A matcher can be created with
<code>(re-matcher </code><i>pattern</i><code>
</code><i>string</i><code>)</code> and is initially in a state where
the match region is the whole string.

<pre><code>user=&gt; <b>(def m (re-matcher p "defabc"))</b>
#'user/m</code></pre>

There are two methods for trying to match the region against the
pattern: <code>(.find </code><i>matcher</i><code>)</code> and
<code>(.matches </code><i>matcher</i><code>)</code>. Here, "matches"
should be read as in "it matches" and not "the matches". The methods
alter the state of the `Matcher` in the following way: if the
beginning of the region matches the pattern, then true is returned and
the the matched substring is stored internally and popped off the
beginning of the remaining match region. Otherwise false is
returned. The two methods differ in that `.find` will scan the string
for a match but `.matches` requires the whole remaining region to
match.

<pre><code>user=&gt; <b>(.find m)</b>
true</code></pre>

To extract the matched subsequence (or the matched groups) for the
most recent match, `re-groups` is used. If no groups are present in
the patter, the match is returned as a string. If _n_ groups are
present in the pattern, a vector of size _n+1_ is returned, where the
first element is the whole match and the rest the matches of the
groups. The state of the `Matcher` remains unchanged.

<pre><code>user=&gt; <b>(re-groups m)</b>
"def"
user=&gt; <b>(re-groups m)</b>
"def"
user=&gt; <b>(.find m)</b>
true
user=&gt; <b>(re-groups m)</b>
"abc"
user=&gt; <b>(.find m)</b>
false</code></pre>

The `re-find` function is a wrapper for `.find` that in addition to
accept a `Matcher` as an argument can also take a pattern and a string
and create its own `Matcher`. A call like (<code>re-find
</code><i>pattern</i><code> </code><i>string</i><code>)</code> is
equivalent to <code>(let [m (re-matcher </code><i>pattern</i><code>
</code><i>string</i><code>)] (when (.find m) (re-groups m)))</code>.

<pre><code>user=&gt; <b>(re-find #"abc|def" "xdefabcy")</b>
"def"</code></pre>

The `re-matches` function works just like `re-find`, except that it
uses the `.matches` method and does not come with a single argument
variant (that would take a `Matcher`).

<pre><code>user=&gt; <b>(re-matches #"abc|def" "def")</b>
"def"
user=&gt; <b>(re-matches #"abc|def" "defabc")</b>
nil</code></pre>

In addition, there's the `re-seq` function that returns a sequence of
all the matches `re-find` would find. It accepts a pattern and a
string as its arguments: <code>(re-seq </code><i>pattern</i><code>
</code><i>string</i><code>)</code>.

<pre><code>user=&gt; <b>(re-seq #"abc|def" "xdefabcy")</b>
("def" "abc")</code></pre>

In the end, four of the functions turn out to be more useful than the
others for a Clojure programmer:

- To create a regex pattern from a string, use `re-pattern`.
- To match a string completely against a pattern, use `re-matches`.
- To find some part of a string that matches a pattern, use `re-find`.
- To find all the parts of a string that matches a pattern, use `re-seq`.

`;; raek`
