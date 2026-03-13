<h2><a href="https://leetcode.com/problems/minimum-moves-to-reach-target-score">2139. Minimum Moves to Reach Target Score</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are playing a game with a starting score of 0. On each move, you can either:</p>

<ul>
<li>Add 1 to your score.</li>
<li>Double your current score (only if you have at least 1 move left and maxDoubles > 0).</li>
</ul>

<p>Given two integers <code>target</code> and <code>maxDoubles</code>, return the <strong>minimum number of moves</strong> required to reach <code>target</code>.</p>

---

### Example 1

<pre>
Input: target = 5, maxDoubles = 0
Output: 5
Explanation: No doubles allowed, so we add 1 five times.
</pre>

### Example 2

<pre>
Input: target = 19, maxDoubles = 2
Output: 7
Explanation:
- Start at 0
- Add 1 → 1
- Double → 2
- Add 1 → 3
- Double → 6
- Add 1 → 7
- Add 1 → 8
- Add 1 → 9
- Add 1 → 10
- Continue until 19
Minimum moves = 7
</pre>

---

### Constraints

<ul>
<li>1 ≤ target ≤ 10<sup>9</sup></li>
<li>0 ≤ maxDoubles ≤ 100</li>
</ul>

---

# Solution

### Approach (Greedy Reverse)

Instead of building up from 0, work backwards from <code>target</code>:

1. While <code>target > 1</code>:
   - If <code>maxDoubles > 0</code> and <code>target % 2 == 0</code>:
     - Divide <code>target</code> by 2
     - Decrement <code>maxDoubles</code>
   - Else:
     - Subtract 1 from <code>target</code>
   - Increment moves by 1
2. Return total moves.

**Why this works:**  
Working backwards ensures we maximize the usage of doubling, reducing total moves.

---

### Complexity

- **Time Complexity:** O(log(target) + maxDoubles)  
- **Space Complexity:** O(1)

---

### Tags

greedy, math, implementation
