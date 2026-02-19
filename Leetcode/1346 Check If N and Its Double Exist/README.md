<h2><a href="https://leetcode.com/problems/check-if-n-and-its-double-exist">1346. Check If N and Its Double Exist</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array of integers <code>arr</code>, return <code>true</code> <strong>if and only if</strong> there exist two integers <code>N</code> and <code>M</code> such that:</p>
<ul>
  <li><code>N</code> and <code>M</code> are <strong>both elements</strong> of <code>arr</code>, and</li>
  <li><code>N = 2 * M</code></li>
</ul>

<p>Note that <code>N = M = 0</code> is valid.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: arr = [10,2,5,3]
Output: true
Explanation: 10 = 2 * 5
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: arr = [7,1,14,11]
Output: true
Explanation: 14 = 2 * 7
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: arr = [3,1,7,11]
Output: false
Explanation: No such pair exists.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 &lt;= arr.length &lt;= 500</li>
  <li>-10³ &lt;= arr[i] &lt;= 10³</li>
</ul>

---

### 🚀 Solution

**Approach:**  
- Use a hash set to store seen values.  
- For each element <code>x</code> in the array:
  - If <code>2 * x</code> is in the set, return `true`.  
  - If <code>x</code> is even and <code>x / 2</code> is in the set, return `true`.
  - Add <code>x</code> to the set.
- If no such pair is found, return `false`.

**Complexity:**  
- Time: O(n) — check each element once  
- Space: O(n) — extra set for history  

---
