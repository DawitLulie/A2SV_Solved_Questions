<h2><a href="https://leetcode.com/problems/permutations-ii">47. Permutations II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a collection of numbers, <code>nums</code>, that might contain duplicates, return all possible unique permutations in any order.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 8</li>
  <li>-10 &lt;= nums[i] &lt;= 10</li>
</ul>

---

### Solution

**Approach:**  
- Use backtracking to generate permutations.  
- Sort the array first and skip duplicates during recursion to ensure uniqueness.

**Complexity:**  
- Time: O(n! / (frequency of duplicates) ) — generates unique permutations  
- Space: O(n) — recursion stack  

---
