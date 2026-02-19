<h2><a href="https://leetcode.com/problems/permutations">46. Permutations</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of distinct integers <code>nums</code>, return all possible permutations. You can return the answer in any order.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,1]
Output: [[0,1],[1,0]]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1]
Output: [[1]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 6</li>
  <li>-10 &lt;= nums[i] &lt;= 10</li>
  <li>All integers in <code>nums</code> are unique.</li>
</ul>

---

### Solution

**Approach:**  
- Use backtracking to generate all permutations.  
- Swap elements or build paths recursively to explore all possibilities.

**Complexity:**  
- Time: O(n!) — all possible permutations  
- Space: O(n) — recursion stack  

---
