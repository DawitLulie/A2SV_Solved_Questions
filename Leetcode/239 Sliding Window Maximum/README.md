<h2><a href="https://leetcode.com/problems/sliding-window-maximum">239. Sliding Window Maximum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, there is a sliding window of size <code>k</code> which moves from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position, return the maximum of the window.</p>

---

### Example 1

<pre>
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window positions and their maximums:
[1,3,-1] → 3
[3,-1,-3] → 3
[-1,-3,5] → 5
[-3,5,3] → 5
[5,3,6] → 6
[3,6,7] → 7
</pre>

### Example 2

<pre>
Input: nums = [1], k = 1
Output: [1]
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁵</li>
<li>-10⁴ ≤ nums[i] ≤ 10⁴</li>
<li>1 ≤ k ≤ nums.length</li>
</ul>

---

### Solution

**Approach (Monotonic Deque):**

Use a deque to maintain indices of elements in the current window. The deque stores elements in **decreasing order** so the front is always the maximum.

Steps:

1. Initialize an empty deque and a result array.
2. Iterate through the array:
   - Remove indices from the front if they are out of the current window (`i - k + 1`).
   - Remove indices from the back if `nums[i]` is greater than `nums[deque[-1]]`.
   - Append current index `i` to the deque.
   - If the window has at least `k` elements, append `nums[deque[0]]` to the result.
3. Return the result array.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(k)

Where `n` is the length of `nums`.

---

### Tags

deque, sliding window, monotonic queue