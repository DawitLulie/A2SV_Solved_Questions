<h2><a href="https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum">1413. Minimum Value to Get Positive Step by Step Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code>, you start with a positive integer <code>startValue</code>.</p>

<p>In each iteration, you add the current array element to <code>startValue</code>. Return the minimum positive integer <code>startValue</code> such that the step-by-step sum is never less than 1.</p>

---

### Example 1

<pre>
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: startValue = 5
Step-by-step sum: 5 -> 2 -> 4 -> 1 -> 5 -> 7 (all ≥ 1)
</pre>

### Example 2

<pre>
Input: nums = [1,2]
Output: 1
Explanation: startValue = 1 is enough
Step-by-step sum: 1 -> 2 -> 4
</pre>

### Example 3

<pre>
Input: nums = [1,-2,-3]
Output: 5
Explanation: startValue = 5
Step-by-step sum: 5 -> 6 -> 4 -> 1 (all ≥ 1)
</pre>

---

### Constraints

<ul>
  <li>1 ≤ nums.length ≤ 100</li>
  <li>-100 ≤ nums[i] ≤ 100</li>
</ul>

---

### Solution

**Approach (Prefix Sum Minimum):**

1. Initialize <code>total = 0</code> and <code>min_sum = 0</code>.
2. Iterate through <code>nums</code>, update <code>total += nums[i]</code> and track <code>min_sum = min(min_sum, total)</code>.
3. The minimum <code>startValue</code> required is <code>1 - min_sum</code> (to ensure sum never drops below 1).

**Why this works:**  
- The step-by-step sum is always ≥ 1 if <code>startValue + min_prefix_sum ≥ 1</code>.

---

### Complexity

- **Time:** O(n) — single pass through the array  
- **Space:** O(1)

---

### Tags

array, prefix sum, greedy