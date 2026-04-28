<h2><a href="https://leetcode.com/problems/surrounded-regions">130. Surrounded Regions</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3>🧠 Problem Understanding</h3>

<p>
You are given a 2D board of size <code>m × n</code> containing:
</p>

<ul>
<li><code>'X'</code> → blocked cell</li>
<li><code>'O'</code> → open cell</li>
</ul>

<p>
Your task is to capture all regions of <code>'O'</code> that are completely surrounded by <code>'X'</code>.
</p>

<p>
A region is considered <b>surrounded</b> if:
</p>

<ul>
<li>It is fully enclosed by <code>'X'</code> on all sides</li>
<li>It does NOT touch the boundary of the board</li>
</ul>

<hr>

<h3>📌 Important Observation</h3>

<p>
The key idea that makes this problem easy:
</p>

<ul>
<li><b>Any 'O' on the boundary can NEVER be surrounded</b></li>
<li><b>Any 'O' connected to a boundary 'O' is also safe</b></li>
</ul>

<p>
So instead of trying to find surrounded regions directly (which is hard),
we do the opposite:
</p>

<p><b>👉 Find all SAFE regions first</b></p>

<hr>

<h3>💡 Intuition</h3>

<p>
Think of the board like an island:
</p>

<ul>
<li>Boundary = connected to ocean → cannot be captured</li>
<li>Inside regions = can be captured if isolated</li>
</ul>

<p>
So:
</p>

<ul>
<li>Start from the boundary</li>
<li>Mark everything reachable from boundary as safe</li>
</ul>

<hr>

<h3>🚀 Approach (DFS from Boundary)</h3>

<p>
We use Depth-First Search (DFS) to mark safe regions.
</p>

<h4>Step 1: Mark Safe Cells</h4>
<ul>
<li>Traverse all boundary cells</li>
<li>If a cell is <code>'O'</code>, run DFS</li>
<li>Mark visited cells as <code>'S'</code> (Safe)</li>
</ul>

<h4>Step 2: Flip Captured Regions</h4>
<ul>
<li>Traverse the entire board</li>
<li>If <code>'O'</code> → change to <code>'X'</code> (captured)</li>
<li>If <code>'S'</code> → change back to <code>'O'</code></li>
</ul>

<hr>

<h3>🔁 DFS Logic</h3>

<ul>
<li>Start from a boundary <code>'O'</code></li>
<li>Mark it as <code>'S'</code></li>
<li>Move in 4 directions:
    <ul>
        <li>Up</li>
        <li>Down</li>
        <li>Left</li>
        <li>Right</li>
    </ul>
</li>
<li>Continue DFS for connected <code>'O'</code></li>
</ul>

<hr>

<h3>🧪 Example Walkthrough</h3>

<pre>
Input:
X X X X
X O O X
X X O X
X O X X
</pre>

<p>
Step 1: Find boundary 'O'
</p>

<ul>
<li>(3,1) is on boundary → start DFS</li>
</ul>

<p>
After DFS marking:
</p>

<pre>
X X X X
X O O X
X X O X
X S X X
</pre>

<p>
Step 2: Flip:
</p>

<ul>
<li>Remaining 'O' → 'X'</li>
<li>'S' → 'O'</li>
</ul>

<pre>
Final Output:
X X X X
X X X X
X X X X
X O X X
</pre>

<hr>

<h3>⚠️ Common Mistake</h3>

<p>
Many try:
</p>

<ul>
<li>Start DFS from every 'O'</li>
<li>Check if it is surrounded</li>
</ul>

<p>
❌ This is inefficient and complex.
</p>

<p>
✔️ Instead, always start from the boundary.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p>
Each cell is visited at most once → <code>O(m × n)</code>
</p>

<h3>💾 Space Complexity:</h3>
<p>
DFS recursion stack → <code>O(m × n)</code>
</p>

<hr>

<h3>🏷️ Tags:</h3>
<p>DFS, Graph, Matrix, Flood Fill</p>