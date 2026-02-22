<h2><a href="https://leetcode.com/problems/minimum-moves-to-equal-array-elements">453. Minimum Moves to Equal Array Elements</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code> of length <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment <strong>n - 1</strong> elements by 1.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3]
Output: 3
Explanation: 
[1,2,3] → [2,3,3] (move 1)
[2,3,3] → [3,4,3] (move 2)
[3,4,3] → [4,4,4] (move 3)
Total moves = 3
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,1,1]
Output: 0
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 10⁵</li>
  <li>-10⁹ ≤ nums[i] ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**

- Incrementing n - 1 elements by 1 is equivalent to decrementing 1 element by 1.  
- Therefore, the minimum moves = sum(nums) - n × min(nums).  
- Steps:
  1. Find the minimum element in the array.
  2. Compute the sum of differences between each element and the minimum.

**Complexity:**

- Time: O(n) — one pass for sum and min  
- Space: O(1) extra  

---