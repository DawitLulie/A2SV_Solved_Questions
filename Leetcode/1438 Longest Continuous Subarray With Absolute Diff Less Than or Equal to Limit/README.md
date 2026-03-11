<h2><a href="https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit">1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of integers <code>nums</code> and an integer <code>limit</code>, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to <code>limit</code>.</p>

<p>In other words, the difference between the maximum and minimum element in the subarray must be ≤ <code>limit</code>.</p>

---

### Example 1

<pre>
Input: nums = [8,2,4,7], limit = 4
Output: 2

Explanation:
The longest valid subarrays are [2,4] and [4,7].
</pre>

### Example 2

<pre>
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4

Explanation:
The subarray [2,4,7,2] has max = 7 and min = 2.
7 - 2 = 5 ≤ limit.
</pre>

### Example 3

<pre>
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁵</li>
<li>1 ≤ nums[i] ≤ 10⁹</li>
<li>0 ≤ limit ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Sliding Window + Monotonic Deques):**

We maintain a sliding window and track the **maximum** and **minimum** values inside the window using two deques.

- `maxDeque` keeps elements in **decreasing order** (front is maximum).
- `minDeque` keeps elements in **increasing order** (front is minimum).

Steps:

1. Initialize two deques and a `left` pointer.
2. Iterate through the array using `right`.
3. Maintain the monotonic property:
   - Remove smaller values from `maxDeque`.
   - Remove larger values from `minDeque`.
4. Add the current element index to both deques.
5. If `nums[maxDeque[0]] - nums[minDeque[0]] > limit`, move `left` forward and remove outdated indices.
6. Update the maximum window length.

This ensures the window always satisfies the condition that the difference between the maximum and minimum values is within the limit.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

### Tags

sliding window, monotonic queue, deque, array