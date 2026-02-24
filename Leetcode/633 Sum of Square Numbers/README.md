<h2><a href="https://leetcode.com/problems/sum-of-square-numbers">633. Sum of Square Numbers</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a non-negative integer <code>c</code>, return <code>true</code> if there exist two integers <code>a</code> and <code>b</code> such that:</p>

<pre>
a² + b² = c
</pre>

Otherwise, return <code>false</code>.</p>

---

<h3>Example 1:</h3>

<pre>
Input: c = 5
Output: true
Explanation: 1² + 2² = 1 + 4 = 5
</pre>

<h3>Example 2:</h3>

<pre>
Input: c = 3
Output: false
</pre>

---

<h3>Constraints:</h3>

<ul>
<li>0 ≤ c ≤ 2³¹ − 1</li>
</ul>

---

<h3>Approach (Two Pointers)</h3>

<ol>
<li>Initialize <code>left = 0</code></li>
<li>Initialize <code>right = int(sqrt(c))</code></li>
<li>While <code>left ≤ right</code>:</li>
<ul>
<li>Compute <code>current = left² + right²</code></li>
<li>If <code>current == c</code> → return true</li>
<li>If <code>current < c</code> → increase <code>left</code></li>
<li>If <code>current > c</code> → decrease <code>right</code></li>
</ul>
</ol>

---

<h3>Time Complexity:</h3>
<p>O(√c)</p>

<h3>Space Complexity:</h3>
<p>O(1)</p>