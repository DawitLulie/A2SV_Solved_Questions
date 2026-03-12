<h2><a href="https://leetcode.com/problems/jump-game">55. Jump Game</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an integer array <code>nums</code>. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.</p>

<p>Return <code>true</code> if you can reach the last index, or <code>false</code> otherwise.</p>

---

### Example 1

<pre>
Input: nums = [2,3,1,1,4]
Output: true
Explanation:
Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

### Example 2

<pre>
Input: nums = [3,2,1,0,4]
Output: false
Explanation:
You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁴</li>
<li>0 ≤ nums[i] ≤ 10⁵</li>
</ul>

---

### Solution

**Approach (Greedy):**

Instead of trying every possible jump, we track the **farthest index we can reach** while scanning the array.

Steps:

1. Initialize a variable `max_reach = 0`.
2. Iterate through the array:
   - If the current index `i` is greater than `max_reach`, we cannot reach this position → return `False`.
   - Update `max_reach = max(max_reach, i + nums[i])`.
3. If we finish the loop, it means we can reach the last index.

The idea is that as long as we can keep extending the farthest reachable position, we can eventually reach the end.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

### Tags

greedy, array