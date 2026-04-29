<h2><a href="https://codeforces.com/contest/510/problem/C">510C. Fox And Names</a></h2>
<img src='https://img.shields.io/badge/Codeforces-1500-blue' alt='Rating: 1500' />
<hr>

<p>
You are given a list of <code>n</code> names sorted in lexicographical order according to an <b>unknown alphabet order</b>.
</p>

<p>
Your task is to determine a possible order of the English lowercase letters that is consistent with this sorting.
</p>

<p>
If no such order exists, print <code>"Impossible"</code>.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b>
5
baa
abcd
abca
cab
cad

<b>Output:</b>
bdacfeghijklmnopqrstuvwxyz
</pre>

<pre>
<b>Input:</b>
3
abc
ab

<b>Output:</b>
Impossible
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>1 ≤ n ≤ 100</code></li>
<li>Total length of all strings ≤ 1000</li>
<li>Strings contain only lowercase English letters</li>
</ul>

<hr>

<h3>Approach (Graph + Topological Sort):</h3>

<p>
This problem is a classic <b>topological sorting</b> problem.
</p>

<p>
We want to determine the relative order of letters based on the given sorted words.
</p>

<hr>

<h3>Key Idea:</h3>

<p>
Compare each pair of adjacent words and find the <b>first position where they differ</b>.
</p>

<ul>
<li>If <code>word1[j] ≠ word2[j]</code>, then:</li>
</ul>

<pre>
word1[j] → word2[j]
</pre>

<p>
This gives us a directed edge in the graph.
</p>

<hr>

<h3>Important Edge Case:</h3>

<p>
If:
</p>

<pre>
word1 = "abc"
word2 = "ab"
</pre>

<p>
Then it is <b>impossible</b>, because a longer word comes before its prefix.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Build a graph of 26 letters</li>
<li>Compare adjacent words to create edges</li>
<li>Track indegree of each node</li>
<li>Run Kahn’s algorithm (BFS)</li>
<li>If we get all 26 letters → valid order</li>
<li>Otherwise → cycle → <code>Impossible</code></li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
The sorted word list gives us constraints between letters. These constraints form a DAG (if valid).
</p>

<p>
Topological sorting finds an order that satisfies all constraints.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n * L + 26²)</code></p>

<ul>
<li><code>n</code> → number of words</li>
<li><code>L</code> → average length of words</li>
</ul>

<h3>💾 Space Complexity:</h3>
<p><code>O(26²)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Graph, Topological Sort, BFS, Strings</p>