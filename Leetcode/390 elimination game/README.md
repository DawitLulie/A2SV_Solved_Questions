<h2><a href="https://leetcode.com/problems/elimination-game">390. Elimination Game</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
You have a list of integers from <code>1</code> to <code>n</code>.
Starting from the left, remove the first number and every other number afterward.
Then reverse the direction and repeat the process until only one number remains.
</p>

<p>
Return the last remaining number.
</p>

---

### Example 1

<pre>
Input: n = 9

Process:
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output: 6
</pre>

### Example 2

<pre>
Input: n = 1
Output: 1
</pre>

---

### Constraints

<ul>
<li>1 ≤ n ≤ 10<sup>9</sup></li>
</ul>

---

### Solution

**Approach (Mathematical Simulation):**

A direct simulation using an array is not possible because <code>n</code> can be very large.

Instead, we track the remaining sequence using four variables:

<ul>
<li><code>head</code>: The first remaining number.</li>
<li><code>step</code>: The distance between consecutive remaining numbers.</li>
<li><code>remaining</code>: The number of elements currently left.</li>
<li><code>left</code>: The current elimination direction.</li>
</ul>

<p>
After each elimination round, the remaining numbers still form an arithmetic sequence, but the distance between numbers doubles.
</p>

<p>
For each round:
</p>

<ol>
<li>
If we are eliminating from the left, the head always moves forward.
</li>

<li>
If we are eliminating from the right, the head moves only when the number of remaining elements is odd.
</li>

<li>
The number of remaining elements is divided by two.
</li>

<li>
The step size is doubled.
</li>

<li>
The direction is reversed.
</li>
</ol>

<p>
When only one number remains, <code>head</code> contains the answer.
</p>

---

### Complexity

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

---

### Tags

math, simulation, divide-and-conquer