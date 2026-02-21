<h2><a href="https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii">462. Minimum Moves to Equal Array Elements II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> of length <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment or decrement any element by 1.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3]
Output: 2
Explanation: Move 1 → 2 (1 move), Move 3 → 2 (1 move), total 2 moves.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,10,2,9]
Output: 16
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 10⁵</li>
  <li>-10⁹ ≤ nums[i] ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**

- The minimum number of moves is achieved by moving all numbers to the **median** of the array.  
- Steps:
  1. Sort the array.
  2. Find the median element.
  3. Sum the absolute differences between each element and the median.

**Why median works:**  
- The sum of absolute differences is minimized when all numbers are moved to the median.

**Complexity:**

- Time: O(n log n) — sorting  
- Space: O(1) extra  

---