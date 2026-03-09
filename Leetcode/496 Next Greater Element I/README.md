<h2><a href="https://leetcode.com/problems/next-greater-element-i">496. Next Greater Element I</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code> with <code>nums1</code>’s elements being a subset of <code>nums2</code>. Find all the next greater numbers for <code>nums1</code>'s elements in the corresponding places of <code>nums2</code>.</p>

<p>The next greater number of a number <code>x</code> in <code>nums1</code> is the first greater number to its right in <code>nums2</code>. If it does not exist, return <code>-1</code> for this number.</p>

---

### Example 1

<pre>
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
For 4, there is no number to its right in nums2 that is greater → -1
For 1, the next greater number is 3
For 2, there is no number to its right → -1
</pre>

### Example 2

<pre>
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums1.length ≤ nums2.length ≤ 1000</li>
<li>0 ≤ nums1[i], nums2[i] ≤ 10⁴</li>
<li>All integers in nums1 and nums2 are unique.</li>
<li>All elements of nums1 appear in nums2.</li>
</ul>

---

### Solution

**Approach (Monotonic Stack + Hash Map):**

1. Use a **stack** to find next greater elements for all numbers in `nums2`.
2. Store the mapping of `number → next greater number` in a dictionary.
3. For each element in `nums1`, return its mapped next greater number (or `-1` if none exists).

Steps:

- Initialize an empty stack and a dictionary `next_greater`.
- Iterate through `nums2`:
  - While the stack is not empty and the current number is greater than the top of the stack:
    - Pop the top number and set `next_greater[top] = current number`.
  - Push the current number onto the stack.
- For remaining numbers in the stack, set their next greater as `-1`.
- Return `[next_greater[x] for x in nums1]`.

---

### Complexity

- **Time Complexity:** O(n + m), where n = len(nums2), m = len(nums1)  
- **Space Complexity:** O(n)  

---

### Tags

stack, hash map, monotonic stack, array