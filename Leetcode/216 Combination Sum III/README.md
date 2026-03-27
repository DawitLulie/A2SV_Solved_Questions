<h2><a href="https://leetcode.com/problems/combination-sum-iii/">216. Combination Sum III</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />
<hr>

<p>
Find all valid combinations of <b>k</b> numbers that add up to <b>n</b> such that:
</p>

<ul>
<li>Only numbers from <code>1</code> to <code>9</code> are used</li>
<li>Each number is used <b>at most once</b></li>
<li>Return all possible valid combinations</li>
</ul>

<hr>

<h3>📌 Example 1:</h3>

<pre>
Input: k = 3, n = 7
Output: [[1,2,4]]
</pre>

<h3>📌 Example 2:</h3>

<pre>
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
</pre>

<hr>

<h3>⚡ Constraints:</h3>

<ul>
<li>2 ≤ k ≤ 9</li>
<li>1 ≤ n ≤ 60</li>
</ul>

<hr>

<h3>💡 Approach (Backtracking):</h3>

<p>
We use <b>backtracking</b> to try all possible combinations.
</p>

<h4>Step-by-step:</h4>

<ol>
<li>We try numbers from <code>1</code> to <code>9</code></li>
<li>We build combinations step by step</li>
<li>Keep track of:
  <ul>
    <li>current sum</li>
    <li>current path (combination)</li>
  </ul>
</li>
<li>If:
  <ul>
    <li>path size == k AND sum == n → valid answer</li>
    <li>sum > n OR path size > k → stop</li>
  </ul>
</li>
<li>Use <code>start</code> to avoid reusing numbers</li>
</ol>

<hr>

<h3>🧠 Why This Works:</h3>

<p>
Backtracking explores all possibilities but stops early when:
</p>

<ul>
<li>Sum becomes too large</li>
<li>We already picked k numbers</li>
</ul>

<p>
This avoids unnecessary work and keeps the solution efficient.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>

<p>
O(C(9, k)) → choosing k numbers from 1..9
</p>

<h3>💾 Space Complexity:</h3>

<p>
O(k) → recursion stack + path storage
</p>

<hr>

<h3>🏷️ Tags:</h3>

<p>Backtracking, Recursion</p>