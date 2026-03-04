<h2><a href="https://leetcode.com/problems/maximum-subarray">53. Maximum Subarray</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, find the subarray with the largest sum, and return its sum.</p>

---

### Example 1

<pre>
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
</pre>

### Example 2

<pre>
Input: nums = [1]
Output: 1
</pre>

### Example 3

<pre>
Input: nums = [5,4,-1,7,8]
Output: 23
</pre>

---

### Constraints

<ul>
  <li>1 ≤ nums.length ≤ 10⁵</li>
  <li>-10⁴ ≤ nums[i] ≤ 10⁴</li>
</ul>

---

### Solution

**Approach (Kadane’s Algorithm):**

1. Initialize:
   - <code>current_sum = nums[0]</code>
   - <code>max_sum = nums[0]</code>
2. Iterate from index 1 to end:
   - Update <code>current_sum = max(nums[i], current_sum + nums[i])</code>
   - Update <code>max_sum = max(max_sum, current_sum)</code>
3. Return <code>max_sum</code>.

**Why this works:**  
At each index, we decide whether to:
- Start a new subarray from the current element, or  
- Extend the previous subarray.

This ensures we always track the best possible subarray ending at each position.

---

### Complexity

- **Time:** O(n) — single pass  
- **Space:** O(1)

---

### Follow-up

If you have solved the <strong>divide and conquer</strong> approach, you can also implement it in O(n log n) time.

---

### Tags

array, dynamic programming, divide and conquer