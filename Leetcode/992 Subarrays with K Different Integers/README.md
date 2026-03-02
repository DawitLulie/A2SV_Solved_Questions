<h2><a href="https://leetcode.com/problems/subarrays-with-k-different-integers">992. Subarrays with K Different Integers</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the <strong>number of subarrays</strong> that contain exactly <strong>k distinct integers</strong>.</p>

<p>A subarray is a contiguous part of an array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays with exactly 2 distinct integers are:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,2,1,3,4], k = 3
Output: 3
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 2 * 10⁴</li>
  <li>1 ≤ nums[i], k ≤ nums.length</li>
</ul>

---

### Solution

**Approach (Sliding Window + At Most K):**  
- Count subarrays with **at most K distinct integers**, then count subarrays with **at most K-1 distinct integers**.  
- Subtract to get exactly K distinct:  
- Use a sliding window and a frequency map to implement `atMost(K)`.  

**Complexity:**  
- Time: O(n) — each element is visited once  
- Space: O(n) — for frequency map  