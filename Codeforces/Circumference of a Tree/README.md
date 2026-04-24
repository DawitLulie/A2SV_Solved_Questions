<h2><a href="https://codeforces.com/gym/102694/problem/A">A. Circumference of a Tree</a></h2>
<img src='https://img.shields.io/badge/Codeforces-1200-blue' alt='Rating: 1200' />
<hr>

<p>
You are given a tree with <code>n</code> nodes.
</p>

<p>
Normally, circumference = π × diameter.  
But in this problem, <b>π = 3</b>.
</p>

<p>
So the task becomes:
</p>

<p><b>Find the diameter of the tree, then multiply it by 3.</b></p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b>
1

<b>Output:</b>
0
</pre>

<pre>
<b>Input:</b>
3
3 2
2 1

<b>Output:</b>
6
</pre>

<pre>
<b>Input:</b>
5
4 2
1 4
5 4
3 4

<b>Output:</b>
6
</pre>

<hr>

<h3>Key Idea:</h3>

<p>
The problem is actually asking for:
</p>

<p><b>3 × (diameter of the tree)</b></p>

<hr>

<h3>How to Find Tree Diameter:</h3>

<p>
Use the classic <b>2 BFS (or DFS)</b> method.
</p>

<ol>
<li>Start BFS from any node (e.g., node 1)</li>
<li>Find the farthest node from it → call it <code>A</code></li>
<li>Start BFS from <code>A</code></li>
<li>The farthest node from <code>A</code> gives the <b>diameter</b></li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
In a tree:
</p>

<ul>
<li>The farthest node from any node lies on the diameter</li>
<li>Running BFS twice guarantees finding the longest path</li>
</ul>

<hr>

<h3>Edge Case:</h3>

<ul>
<li>If <code>n = 1</code> → diameter = 0 → answer = 0</li>
</ul>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Tree, BFS, Diameter</p>