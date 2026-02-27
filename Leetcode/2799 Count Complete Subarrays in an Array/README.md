<h2><a href="https://leetcode.com/problems/count-complete-subarrays-in-an-array/">2799. Count Complete Subarrays in an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, a <strong>complete subarray</strong> is a contiguous subarray that contains all distinct elements of <code>nums</code>.</p>

<p>Return the number of complete subarrays in <code>nums</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The distinct elements of nums are [1,2,3].
The complete subarrays are: [1,3,1,2], [3,1,2], [1,2,2], [1,3,1,2,2].
</pre>

---

### Example 2

<pre>
Input: nums = [5,5,5,5]
Output: 10
Explanation: The only distinct element is [5], so every subarray is complete.
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 1000</li>
<li>1 ≤ nums[i] ≤ 2000</li>
</ul>

---

### Approach (Sliding Window with HashMap)

Your solution works using a **sliding window**:

1. Count all distinct elements in the array using `Counter(nums)` and store the count in `length`.
2. Use two pointers `left` and `right` to maintain a window.
3. Expand the `right` pointer and add `nums[right]` to the window `dic`.
4. Whenever the window contains all distinct elements (i.e., `len(dic) == length`):
   - All subarrays starting at `left` and ending at any index ≥ `right` are complete.
   - Add `len(nums) - right` to `count`.
   - Shrink the window from the left by decrementing `dic[nums[left]]` and removing it if zero.
5. Continue until the end of the array.

This efficiently counts all complete subarrays in **O(n)** time.

---

### Complexity

- **Time:** O(n) — each element enters and leaves the sliding window at most once  
- **Space:** O(n) — to store counts of elements in the current window