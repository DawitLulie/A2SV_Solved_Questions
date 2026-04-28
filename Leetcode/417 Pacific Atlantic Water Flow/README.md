<h2><a href="https://leetcode.com/problems/pacific-atlantic-water-flow">417. Pacific Atlantic Water Flow</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
You are given an <code>m × n</code> matrix of heights.
</p>

<p>
Water can flow from a cell to another if the next cell has height <b>less than or equal</b> to the current cell.
</p>

<p>
Find all coordinates where water can flow to <b>both</b>:
</p>

<ul>
<li><b>Pacific Ocean</b> (top and left edges)</li>
<li><b>Atlantic Ocean</b> (bottom and right edges)</li>
</ul>

<hr>

<h3>Example:</h3>

<pre>
<b>Input:</b>
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]

<b>Output:</b>
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
</pre>

<hr>

<h3>Approach (Reverse DFS / BFS):</h3>

<p>
Instead of starting from every cell and checking if it reaches oceans (slow),
we do the <b>reverse idea</b>.
</p>

<p>
Start from oceans and move inward.
</p>

<hr>

<h3>Key Idea:</h3>

<ul>
<li>Water flows from high → low</li>
<li>So in reverse, we move from low → high</li>
</ul>

<p>
That means:
</p>

<ul>
<li>From ocean cells, we can go to neighbors with <code>height >= current</code></li>
</ul>

<hr>

<h3>Steps:</h3>

<ol>
<li>Create two visited sets:
    <ul>
        <li><code>pacific</code></li>
        <li><code>atlantic</code></li>
    </ul>
</li>

<li>Run DFS/BFS from:
    <ul>
        <li>Top row + left column → Pacific</li>
        <li>Bottom row + right column → Atlantic</li>
    </ul>
</li>

<li>While traversing:
    <ul>
        <li>Only move to cells with height ≥ current</li>
    </ul>
</li>

<li>Final answer = intersection of both sets</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Instead of checking every path from each cell, we find all cells that can reach each ocean.
</p>

<p>
The intersection gives cells that can reach both oceans.
</p>

<p>
This reduces redundant work significantly.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(m × n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(m × n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>DFS, BFS, Matrix, Graph</p>