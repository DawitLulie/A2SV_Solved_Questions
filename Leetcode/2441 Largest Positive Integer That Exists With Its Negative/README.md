<h2><a href="https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative">2441. Largest Positive Integer That Exists With Its Negative</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code> that does not contain any zeros, find the largest positive integer <code>k</code> such that both <code>k</code> and <code>-k</code> exist in the array.</p>

<p>Return the largest such integer. If there is no such integer, return <code>-1</code>.</p>

---

### Example 1

<pre>
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k. Both 3 and -3 exist in the array.
</pre>

### Example 2

<pre>
Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and -1 exist, and both 7 and -7 exist.
The largest valid k is 7.
</pre>

### Example 3

<pre>
Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no positive integer k such that both k and -k exist.
</pre>

---

### Constraints

<ul>
  <li>1 ≤ nums.length ≤ 1000</li>
  <li>-1000 ≤ nums[i] ≤ 1000</li>
  <li>nums[i] ≠ 0</li>
</ul>

---

### Solution

**Approach (Hash Set):**

1. Insert all numbers into a set for O(1) lookup.
2. Iterate through the array.
3. For every positive number <code>x</code>, check if <code>-x</code> exists in the set.
4. Keep track of the maximum valid <code>x</code>.
5. If none found, return <code>-1</code>.

**Why this works:**  
A set allows constant-time checks to verify whether both <code>k</code> and <code>-k</code> exist.

---

### Complexity

- **Time:** O(n)  
- **Space:** O(n)

---

### Tags

array, hash table