<h2><a href="https://leetcode.com/problems/find-the-winner-of-the-circular-game/">1823. Find the Winner of the Circular Game</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />
<hr>

<p>
There are <code>n</code> friends standing in a circle, labeled from <code>1</code> to <code>n</code>.
</p>

<p>
Starting from the first friend, we eliminate every <code>k-th</code> friend in the circle until only one remains.
</p>

<p>
Return the label of the winner.
</p>

---

### Example 1

<pre>
Input: n = 5, k = 2
Output: 3

Explanation:
Step-by-step elimination:
1 2 3 4 5 → remove 2
1 3 4 5 → remove 4
1 3 5 → remove 1
3 5 → remove 5
3 → winner
</pre>

---

### Example 2

<pre>
Input: n = 6, k = 5
Output: 1
</pre>

---

### Constraints

<ul>
<li>1 ≤ n ≤ 500</li>
<li>1 ≤ k ≤ 500</li>
</ul>

---

### Solution

**Approach 1: Simulation using Queue**

We simulate the circular process using a queue.

#### Idea:
- Put all numbers from 1 to n into a queue.
- For each round:
  - Move the first <code>k-1</code> elements to the back.
  - Remove the front element (this is the k-th person).
- Continue until one person remains.

This directly mimics the circular elimination process.

---
