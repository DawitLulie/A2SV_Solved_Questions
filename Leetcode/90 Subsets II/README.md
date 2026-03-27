<h2><a href="https://leetcode.com/problems/subsets-ii/">90. Subsets II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3>🧩 Problem Description</h3>
<p>
Given an integer array <code>nums</code> that may contain duplicates, return <b>all possible subsets</b> (the power set).
</p>

<p>
The solution set must <b>not contain duplicate subsets</b>. Return the solution in any order.
</p>

<hr>

<h3>📌 Examples</h3>

<pre>
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre>

<pre>
Input: nums = [0]
Output: [[],[0]]
</pre>

<hr>

<h3>⚙️ Constraints</h3>
<ul>
<li>1 ≤ nums.length ≤ 10</li>
<li>-10 ≤ nums[i] ≤ 10</li>
</ul>

<hr>

<h3>💡 Approach (Backtracking)</h3>

<p>
This is a <b>backtracking</b> problem. We try to generate all subsets step by step.
</p>

<h4>🔑 Key Idea:</h4>
<ul>
<li>Sort the array first → this helps detect duplicates</li>
<li>While building subsets, skip duplicate elements</li>
</ul>

<h4>🚀 Steps:</h4>
<ol>
<li>Sort the input array</li>
<li>Start with an empty subset</li>
<li>At each step:
    <ul>
        <li>Add current subset to result</li>
        <li>Loop through remaining elements</li>
        <li>Skip duplicates using:
        <code>if i > start and nums[i] == nums[i-1]</code></li>
        <li>Include current number and recurse</li>
        <li>Backtrack (remove last element)</li>
    </ul>
</li>
</ol>

<hr>

<h3>🧠 Why This Works</h3>

<p>
Sorting ensures that duplicates are next to each other.
</p>

<p>
So when we see the same number again in the same recursion level, we skip it to avoid duplicate subsets.
</p>

<hr>

<h3>⏱️ Time Complexity</h3>
<p>
O(2ⁿ) → we generate all possible subsets
</p>

<h3> Space Complexity</h3>
<p>
O(n) → recursion stack
</p>

<hr>

<h3>🏷️ Tags</h3>
<p>
Backtracking, Recursion, Array
</p>