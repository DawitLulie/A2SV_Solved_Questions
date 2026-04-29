<h2><a href="https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph">2192. All Ancestors of a Node in a Directed Acyclic Graph</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>
You are given a DAG with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code> and a list of directed edges.
</p>

<p>
Return a list where <code>answer[i]</code> is a sorted list of all ancestors of node <code>i</code>.
</p>

<p>
A node <code>u</code> is an ancestor of <code>v</code> if there is a directed path from <code>u</code> to <code>v</code>.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
<b>Output:</b> [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li>1 ≤ n ≤ 1000</li>
<li>0 ≤ edges.length ≤ min(2000, n(n-1)/2)</li>
<li>0 ≤ edges[i][0], edges[i][1] < n</li>
<li>The graph is a DAG</li>
</ul>

<hr>

<h3>Approach (Topological Sort + Propagation):</h3>

<p>
We use a <b>reverse graph idea</b> with topological sorting.
</p>

<h4>Key Idea:</h4>
<p>
Instead of searching ancestors backward each time, we propagate ancestor sets forward in topological order.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Build adjacency list and indegree array</li>
<li>Initialize ancestor list: <code>anc[i] = set()</code></li>
<li>Run Kahn’s algorithm (topological sort)</li>
<li>For each node u → v:</li>
<ul>
<li>Add u to ancestors of v</li>
<li>Also add all ancestors of u to v</li>
</ul>
<li>Convert sets to sorted lists</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Since the graph is a DAG, processing nodes in topological order guarantees that all ancestors of a node are already computed before propagating forward.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n² + e)</code> worst case (due to set merging)</p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n²)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Graph, Topological Sort, DAG, Set Propagation</p>