<h2><a href="https://leetcode.com/problems/132-pattern">456. 132 Pattern</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of <code>n</code> integers <code>nums</code>, a <strong>132 pattern</strong> is a subsequence of three integers <code>nums[i]</code>, <code>nums[j]</code>, and <code>nums[k]</code> such that:</p>

<ul>
<li><code>i &lt; j &lt; k</code></li>
<li><code>nums[i] &lt; nums[k] &lt; nums[j]</code></li>
</ul>

<p>Return <code>true</code> if there is a <strong>132 pattern</strong> in <code>nums</code>, otherwise return <code>false</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
</pre>

### Example 2

<pre>
Input: nums = [3,1,4,2]
Output: true
Explanation: The 132 pattern is [1,4,2].
</pre>

### Example 3

<pre>
Input: nums = [-1,3,2,0]
Output: true
Explanation: The 132 patterns are [-1,3,2], [-1,3,0], and [-1,2,0].
</pre>

---

### Constraints

<ul>
<li>n == nums.length</li>
<li>1 ≤ n ≤ 2 × 10⁵</li>
<li>-10⁹ ≤ nums[i] ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Monotonic Stack):**

We traverse the array from **right to left** while maintaining a stack to track possible `nums[j]` values and a variable to store the possible `nums[k]`.

Steps:

1. Initialize an empty stack.
2. Keep a variable `second` representing the candidate for `nums[k]`.
3. Iterate from the end of the array:
   - If `nums[i] < second`, we found the **132 pattern**.
   - While the stack is not empty and `nums[i] > stack[-1]`:
     - Pop from the stack and update `second`.
   - Push `nums[i]` into the stack.
4. If no pattern is found, return `False`.

The stack keeps decreasing values representing potential `nums[j]`, and `second` stores the best candidate for `nums[k]`.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

### Tags

stack, monotonic stack, array