<h2><a href="https://leetcode.com/problems/combination-sum/">39. Combination Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3>🧩 Problem Description</h3>
<p>
Given an array of <b>distinct integers</b> <code>candidates</code> and a target integer <code>target</code>, return a list of all <b>unique combinations</b> where the chosen numbers sum to <code>target</code>.
</p>

<p>
You may use the <b>same number multiple times</b>. The combinations can be returned in any order.
</p>

<hr>

<h3>📌 Examples</h3>

<pre>
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
</pre>

<pre>
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
</pre>

<hr>

<h3>⚙️ Constraints</h3>
<ul>
<li>1 ≤ candidates.length ≤ 30</li>
<li>2 ≤ candidates[i] ≤ 40</li>
<li>All elements are distinct</li>
<li>1 ≤ target ≤ 40</li>
</ul>

<hr>

<h3>💡 Approach (Backtracking)</h3>

<p>
This is a classic <b>backtracking</b> problem where we try all possible combinations.
</p>

<h4>🔑 Key Idea:</h4>
<ul>
<li>We can reuse the same number → so we don't move to next index after choosing</li>
<li>Stop when sum exceeds target</li>
</ul>

<h4> Steps:</h4>
<ol>
<li>Start from index 0</li>
<li>At each step:
    <ul>
        <li>If target == 0 → valid combination → add to result</li>
        <li>If target < 0 → stop (invalid path)</li>
        <li>Loop through candidates starting from current index</li>
        <li>Choose element</li>
        <li>Recurse with reduced target</li>
        <li><b>Do not move index forward</b> (because reuse allowed)</li>
        <li>Backtrack</li>
    </ul>
</li>
</ol>

<hr>

<h3> Why This Works</h3>

<p>
We explore all possibilities using recursion.
</p>

<p>
Since we only move forward in the array, we avoid duplicate combinations like [2,3] and [3,2].
</p>

<hr>

<h3>⏱️ Time Complexity</h3>
<p>
O(2ⁿ) (approx) → depends on branching and recursion
</p>

<h3> Space Complexity</h3>
<p>
O(target) → recursion depth
</p>

<hr>

<h3>🏷️ Tags</h3>
<p>
Backtracking, Recursion, Array
</p>