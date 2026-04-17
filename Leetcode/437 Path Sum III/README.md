<h2><a href="https://leetcode.com/problems/path-sum-iii">437. Path Sum III</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return the number of paths where the sum of the values along the path equals <code>targetSum</code>.
</p>

<p>
The path does not need to start or end at the root, but it must go downward (parent to child).
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
<b>Output:</b> 3
</pre>

<pre>
<b>Input:</b> root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
<b>Output:</b> 3
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li>The number of nodes in the tree is in the range <code>[0, 1000]</code></li>
<li><code>-10⁹ ≤ Node.val ≤ 10⁹</code></li>
<li><code>-1000 ≤ targetSum ≤ 1000</code></li>
</ul>

<hr>

<h3>Approach (Prefix Sum + DFS):</h3>

<p>
We use a prefix sum technique with DFS.
</p>

<ul>
<li>Keep track of the current path sum</li>
<li>Check how many previous prefix sums satisfy:
    <br>
    <code>current_sum - previous_sum = target</code>
</li>
</ul>

<hr>

<h3>Steps:</h3>

<ol>
<li>Use a hashmap to store prefix sums and their counts</li>
<li>Initialize with <code>{0: 1}</code></li>
<li>Traverse the tree using DFS</li>
<li>At each node:
    <ul>
        <li>Add node value to current sum</li>
        <li>Check if <code>current_sum - target</code> exists in hashmap</li>
        <li>Add that count to result</li>
    </ul>
</li>
<li>Update hashmap with current sum</li>
<li>Recurse left and right</li>
<li>Backtrack (remove current sum from hashmap)</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Instead of checking all paths, we reuse prefix sums to quickly find valid paths.
</p>

<p>
This reduces the time complexity significantly.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Tree, DFS, Prefix Sum, HashMap</p>