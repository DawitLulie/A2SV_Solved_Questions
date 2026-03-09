<h2><a href="https://leetcode.com/problems/next-greater-element-ii">503. Next Greater Element II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a <strong>circular integer array</strong> <code>nums</code> (i.e., the next element of <code>nums[nums.length - 1]</code> is <code>nums[0]</code>), return the <strong>next greater number</strong> for every element in <code>nums</code>.</p>

<p>The next greater number of a number <code>x</code> is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return <code>-1</code> for that number.</p>

---

### Example 1

<pre>
Input: nums = [1,2,1]
Output: [2,-1,2]
</pre>

### Example 2

<pre>
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁴</li>
<li>-10⁹ ≤ nums[i] ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Monotonic Stack + Circular Array):**

To find the next greater element efficiently, we use a **monotonic decreasing stack**.

Key ideas:

- Traverse the array **twice** to simulate circular behavior.
- The stack stores **indices** of elements whose next greater element hasn't been found yet.
- When the current number is greater than the element indexed at the top of the stack, we update the result.

Steps:

1. Initialize a result array filled with `-1`.
2. Use a stack to store indices.
3. Iterate through `2 * n` elements:
   - Use `i % n` to access the circular index.
4. While the stack is not empty and the current element is greater than the element at the stack’s top index:
   - Pop the index and update its next greater value.
5. Push the index into the stack only during the first pass (`i < n`).

This ensures every element finds the next greater element if it exists.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Where `n` is the number of elements in `nums`.

---

### Tags

stack, monotonic stack, array