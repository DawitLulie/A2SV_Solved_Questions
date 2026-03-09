<h2><a href="https://leetcode.com/problems/daily-temperatures">739. Daily Temperatures</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array <code>temperatures</code> represents the daily temperatures, return an array <code>answer</code> such that <code>answer[i]</code> is the number of days you have to wait after the <code>i<sup>th</sup></code> day to get a warmer temperature. If there is no future day for which this is possible, put <code>0</code> in <code>answer[i]</code>.</p>

---

### Example 1

<pre>
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
</pre>

### Example 2

<pre>
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
</pre>

### Example 3

<pre>
Input: temperatures = [30,60,90]
Output: [1,1,0]
</pre>

---

### Constraints

<ul>
<li>1 ≤ temperatures.length ≤ 10⁵</li>
<li>30 ≤ temperatures[i] ≤ 100</li>
</ul>

---

### Solution

**Approach (Monotonic Stack):**

We use a **monotonic decreasing stack** to efficiently find the next warmer day.

Steps:

1. Initialize a stack to store indices of temperatures.
2. Traverse each day:
   - While the stack is not empty and the current temperature is **greater** than the temperature at the index on top of the stack:
     - Pop the index from the stack.
     - Set `answer[index] = current_index - index`.
   - Push the current index onto the stack.
3. Any remaining indices in the stack have no warmer future days → they remain `0`.

This works because the stack always keeps indices of days waiting for a warmer temperature.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Where `n` is the number of days.

---

### Tags

stack, monotonic stack, array