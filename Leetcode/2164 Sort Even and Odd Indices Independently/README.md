<h2><a href="https://leetcode.com/problems/sort-even-and-odd-indices-independently">2164. Sort Even and Odd Indices Independently</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given an integer array <code>nums</code>. Rearrange the values at the even indices of <code>nums</code> in <strong>non‑decreasing order</strong>, and the values at the odd indices of <code>nums</code> in <strong>non‑increasing order</strong>.  
Return <em>the resulting array</em>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation:
Even indices are 0 and 2 → values are [4,2] → sorted ascending → [2,4]
Odd indices are 1 and 3 → values are [1,3] → sorted descending → [3,1]
Combine → [2,3,4,1]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [2,1]
Output: [2,1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 100</li>
  <li>1 ≤ nums[i] ≤ 100</li>
</ul>

---

###  Solution

**Approach:**  
- Extract values at even indices and sort them in ascending order.  
- Extract values at odd indices and sort them in descending order.  
- Reassign the sorted values back to their original positions.

**Complexity:**  
- Time: O(n log n) — for sorting each group  
- Space: O(n) — for storing separated lists  

---
