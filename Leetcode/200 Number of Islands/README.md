<h2><a href="https://leetcode.com/problems/number-of-islands">200. Number of Islands</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <b>'1'</b>s (land) and <b>'0'</b>s (water), return the number of islands.
</p>

<p>
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b>
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

<b>Output:</b> 1
</pre>

<pre>
<b>Input:</b>
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

<b>Output:</b> 3
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>m == grid.length</code></li>
<li><code>n == grid[i].length</code></li>
<li><code>1 ≤ m, n ≤ 300</code></li>
<li><code>grid[i][j] is '0' or '1'</code></li>
</ul>

<hr>

<h3>Approach (DFS Flood Fill):</h3>

<p>
We treat the grid as a graph.
Each land cell (<code>'1'</code>) is a node.
We perform DFS to "sink" an entire island once we find it.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Loop through every cell in the grid</li>
<li>If we find a <code>'1'</code>, it means a new island</li>
<li>Run DFS to mark all connected land as visited</li>
<li>Increase island count</li>
</ol>

<hr>

<h3>DFS Logic:</h3>
<ul>
<li>Check boundaries</li>
<li>Stop if cell is water or already visited</li>
<li>Mark current cell as visited</li>
<li>Explore 4 directions (up, down, left, right)</li>
</ul>

<hr>

<h3>Why This Works:</h3>

<p>
Each DFS call completely removes one island from the grid.
So every time we start DFS, we count exactly one new island.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(m × n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(m × n)</code> (recursion stack in worst case)</p>

<hr>

<h3>🏷️ Tags:</h3>
<p>DFS, BFS, Graph, Flood Fill, Matrix</p>