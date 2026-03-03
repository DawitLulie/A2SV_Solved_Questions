<h2><a href="https://leetcode.com/problems/subarray-sum-equals-k">560. Subarray Sum Equals K</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the total number of continuous subarrays whose sum equals <code>k</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: The subarrays [1,1] at indices [0,1] and [1,2] sum to 2.
</pre>

### Example 2

<pre>
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarrays [1,2] and [3] sum to 3.
</pre>

---

### Constraints

<ul>
  <li>1 ≤ nums.length ≤ 2 * 10⁴</li>
  <li>-1000 ≤ nums[i] ≤ 1000</li>
  <li>-10⁷ ≤ k ≤ 10⁷</li>
</ul>

---

### Solution

**Approach (Prefix Sum + Hash Map):**

1. Keep a running sum (`prefix_sum`) while iterating through the array.
2. Maintain a hash map `count` of how many times each prefix_sum occurs.
3. For each index, check if `(prefix_sum - k)` exists in the map.
   - If yes, it indicates there is a subarray ending at current index summing to `k`.
4. Increment result by the count of `(prefix_sum - k)`.

**Why this works:**  
The difference between prefix sums of two indices equals the sum of the subarray between them.

---

### Complexity

- Time: O(n) — iterate through the array once
- Space: O(n) — hash map to store prefix sums

---

### Tags

array, hash map, prefix sum