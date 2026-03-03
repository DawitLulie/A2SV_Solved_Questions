<h2><a href="https://leetcode.com/problems/continuous-subarray-sum">523. Continuous Subarray Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <strong>true</strong> if <code>nums</code> has a continuous subarray of size at least two whose elements sum up to a multiple of <code>k</code>, or <strong>false</strong> otherwise.</p>

<p>In other words, find if there exists a subarray <code>nums[i..j]</code> (i < j) such that:</p>

<pre>
sum(nums[i..j]) = n * k, where n is an integer.
</pre>

---

### Example 1

<pre>
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] sums to 6, which is a multiple of 6.
</pre>

### Example 2

<pre>
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23,2,6,4,7] sums to 42, which is a multiple of 6.
</pre>

### Example 3

<pre>
Input: nums = [23,2,6,4,7], k = 13
Output: false
</pre>

---

### Constraints

<ul>
  <li>1 ≤ nums.length ≤ 10⁵</li>
  <li>0 ≤ nums[i] ≤ 10⁹</li>
  <li>0 ≤ k ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Prefix Sum + Remainder Hash Map):**

1. Compute prefix sums modulo <code>k</code>.
2. Use a dictionary to store the first occurrence index of each remainder.
3. If the same remainder appears again with at least one element in between, a subarray sum multiple of <code>k</code> exists.
4. Handle edge case when <code>k=0</code> by checking consecutive zeros.

**Why this works:**  
If `(prefix_sum[i] - prefix_sum[j]) % k == 0`, then subarray nums[j+1..i] sum is a multiple of k.

---

### Complexity

- Time: O(n) — single pass
- Space: O(min(n, k)) — hashmap for remainders

---

### Tags

array, hash map, prefix sum