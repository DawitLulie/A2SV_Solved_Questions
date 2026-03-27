<h2><a href="https://leetcode.com/problems/permutations-ii/">47. Permutations II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3>🧩 Problem Description</h3>
<p>
Given a collection of numbers <code>nums</code>, that might contain duplicates, return <b>all possible unique permutations</b>.
</p>

<p>
Return the answer in any order.
</p>

<hr>

<h3>📌 Examples</h3>

<pre>
Input: nums = [1,1,2]
Output:
[
 [1,1,2],
 [1,2,1],
 [2,1,1]
]
</pre>

<pre>
Input: nums = [1,2,3]
Output:
[
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
</pre>

<hr>

<h3>⚙️ Constraints</h3>
<ul>
<li>1 ≤ nums.length ≤ 8</li>
<li>-10 ≤ nums[i] ≤ 10</li>
</ul>

<hr>

<h3>💡 Approach (Backtracking + Duplicate Handling)</h3>

<p>
This is a <b>backtracking</b> problem where we generate permutations step by step.
</p>

<h4>🔑 Key Idea:</h4>
<ul>
<li>Sort the array → helps detect duplicates</li>
<li>Use a <code>used[]</code> array to track visited elements</li>
<li>Skip duplicates carefully</li>
</ul>

<h4>🚀 Steps:</h4>
<ol>
<li>Sort the array</li>
<li>Create a <code>used[]</code> array initialized with False</li>
<li>For each recursion:
    <ul>
        <li>If path length == n → add to result</li>
        <li>Loop through elements</li>
        <li>Skip if already used</li>
        <li>Skip duplicates:
        <code>if i > 0 and nums[i] == nums[i-1] and not used[i-1]</code></li>
        <li>Choose element</li>
        <li>Recurse</li>
        <li>Backtrack</li>
    </ul>
</li>
</ol>

<hr>

<h3> Why This Works</h3>

<p>
Sorting puts duplicates together.
</p>

<p>
The condition:
<code>not used[i-1]</code> ensures we only use duplicates in a specific order,
avoiding repeated permutations.
</p>

<hr>

<h3>⏱️ Time Complexity</h3>
<p>
O(n! ) → generating permutations
</p>

<h3> Space Complexity</h3>
<p>
O(n) → recursion stack + used array
</p>

<hr>

<h3>🏷️ Tags</h3>
<p>
Backtracking, Recursion, Array
</p>