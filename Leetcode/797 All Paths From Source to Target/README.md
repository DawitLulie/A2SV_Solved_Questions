<h2><a href="https://leetcode.com/problems/all-paths-from-source-to-target">797. All Paths From Source to Target</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
Given a directed acyclic graph (DAG) of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>, find all possible paths from node <code>0</code> to node <code>n - 1</code>.
</p>

<p>
The graph is given as <code>graph[i]</code> = list of all nodes you can visit from node <code>i</code>.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> graph = [[1,2],[3],[3],[]]
<b>Output:</b> [[0,1,3],[0,2,3]]
</pre>

<pre>
<b>Input:</b> graph = [[4,3,1],[3,2,4],[3],[4],[]]
<b>Output:</b> [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4]]
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>n == graph.length</code></li>
<li><code>2 ≤ n ≤ 15</code></li>
<li><code>0 ≤ graph[i][j] < n</code></li>
<li>The graph is a <b>DAG</b> (no cycles)</li>
</ul>

<hr>

<h3>Approach (DFS + Backtracking):</h3>

<p>
We use DFS to explore all possible paths from node <code>0</code> to node <code>n-1</code>.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Start DFS from node <code>0</code></li>
<li>Keep track of the current path</li>
<li>If we reach node <code>n-1</code>, add the path to the result</li>
<li>For each neighbor:
    <ul>
        <li>Add it to path</li>
        <li>Recurse</li>
        <li>Backtrack (remove it)</li>
    </ul>
</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Since the graph is a DAG, there are no cycles.
So DFS safely explores all paths without worrying about infinite loops.
</p>

<p>
Backtracking ensures we explore every possible path correctly.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(2^n * n)</code> (all possible paths)</p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code> (recursion stack)</p>

<hr>

<h3>🏷️ Tags:</h3>
<p>DFS, Backtracking, Graph</p>