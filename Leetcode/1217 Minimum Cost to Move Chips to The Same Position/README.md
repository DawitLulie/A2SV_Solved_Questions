<h2><a href="https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position">1217. Minimum Cost to Move Chips to The Same Position</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>We have <code>n</code> chips, where the position of the <code>i<sup>th</sup></code> chip is <code>position[i]</code>.</p>

<p>We need to move all the chips to the same position. In one step, we can change the position of the <code>i<sup>th</sup></code> chip from <code>position[i]</code> to:</p>

<ul>
<li><code>position[i] + 2</code> with cost = <code>0</code></li>
<li><code>position[i] - 2</code> with cost = <code>0</code></li>
<li><code>position[i] + 1</code> with cost = <code>1</code></li>
<li><code>position[i] - 1</code> with cost = <code>1</code></li>
</ul>

<p>Return the <strong>minimum cost</strong> needed to move all the chips to the same position.</p>

---

### Example 1

<pre>
Input: position = [1,2,3]
Output: 1
Explanation:
Move chip at position 2 → 3 with cost 1.
Now all chips are at positions [1,3,3] which can move to 3 with cost 0.
</pre>

### Example 2

<pre>
Input: position = [2,2,2,3,3]
Output: 2
</pre>

---

### Constraints

<ul>
<li>1 ≤ position.length ≤ 100</li>
<li>1 ≤ position[i] ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Greedy / Parity Observation):**

Key idea:

- Moving a chip by **2 positions costs 0**, so chips can move freely among **even positions** or among **odd positions**.
- Moving between **even and odd** positions costs **1**.

Steps:

1. Count how many chips are at **even positions**.
2. Count how many chips are at **odd positions**.
3. Move the smaller group to the larger group.

Minimum cost = `min(even_count, odd_count)`.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

### Tags

greedy, array, math