<h2><a href="https://leetcode.com/problems/largest-rectangle-in-histogram">84. Largest Rectangle in Histogram</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given an array of integers <code>heights</code> representing the histogram's bar height where the width of each bar is <code>1</code>, return the area of the <strong>largest rectangle</strong> in the histogram.</p>

---

### Example 1

<pre>
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation:
The largest rectangle is formed by heights [5,6] with width 2 → area = 10
</pre>

### Example 2

<pre>
Input: heights = [2,4]
Output: 4
</pre>

---

### Constraints

<ul>
<li>1 ≤ heights.length ≤ 10⁵</li>
<li>0 ≤ heights[i] ≤ 10⁴</li>
</ul>

---

# Solution

### Approach (Monotonic Stack)

Key idea:

For each bar, we want to find:
- The first smaller element to the left
- The first smaller element to the right

Instead of computing separately, we use a **monotonic increasing stack**.

Steps:

1. Iterate through the array.
2. Maintain a stack storing indices of increasing heights.
3. When the current height is smaller than the top of the stack:
   - Pop from stack
   - Calculate area:
     - height = popped height
     - width = current index - previous smaller index - 1
4. After finishing the array, process remaining elements in stack.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(n)

---

### Tags

stack, monotonic stack, array