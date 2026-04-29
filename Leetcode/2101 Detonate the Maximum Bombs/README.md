<h2><a href="https://leetcode.com/problems/detonate-the-maximum-bombs">2101. Detonate the Maximum Bombs</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
You are given a list of bombs. Each bomb is represented as:
<code>[x, y, r]</code>
where:
</p>

<ul>
<li><code>(x, y)</code> → location of the bomb</li>
<li><code>r</code> → radius of explosion</li>
</ul>

<p>
When a bomb explodes, it can detonate other bombs within its radius. This can create a chain reaction.
</p>

<p>
Return the <b>maximum number of bombs</b> that can be detonated if you choose exactly one bomb to start.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> bombs = [[2,1,3],[6,1,4]]
<b>Output:</b> 2
</pre>

<pre>
<b>Input:</b> bombs = [[1,1,5],[10,10,5]]
<b>Output:</b> 1
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>1 ≤ bombs.length ≤ 100</code></li>
<li><code>bombs[i].length == 3</code></li>
<li><code>1 ≤ x, y, r ≤ 10⁵</code></li>
</ul>

<hr>

<h3>Approach (Graph + DFS):</h3>

<p>
This problem is a <b>graph problem</b>.
</p>

<p>
Think of each bomb as a node. If bomb <code>i</code> can detonate bomb <code>j</code>, we create a directed edge:
</p>

<pre>
i → j
</pre>

<hr>

<h3>Step 1: Build Graph</h3>

<ul>
<li>For every pair of bombs <code>(i, j)</code>:</li>
<li>Calculate distance between them:</li>
</ul>

<pre>
dx = x1 - x2
dy = y1 - y2
distance² = dx² + dy²
</pre>

<ul>
<li>If:</li>
</ul>

<pre>
dx² + dy² ≤ r²
</pre>

<p>
Then bomb <code>i</code> can detonate bomb <code>j</code>.
</p>

<hr>

<h3>Step 2: Try Each Bomb as Starting Point</h3>

<ul>
<li>Run DFS from each bomb</li>
<li>Count how many bombs can be reached</li>
<li>Keep track of the maximum</li>
</ul>

<hr>

<h3>Why This Works:</h3>

<p>
We simulate every possible starting bomb and follow the chain reaction using DFS.
</p>

<p>
Since each bomb can trigger others, this naturally forms a graph traversal problem.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p>
<code>O(n² + n*(n + e)) ≈ O(n³)</code>
</p>

<p>
But since <code>n ≤ 100</code>, this is efficient enough.
</p>

<h3>💾 Space Complexity:</h3>
<p>
<code>O(n²)</code> for graph
</p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Graph, DFS, BFS, Geometry</p>