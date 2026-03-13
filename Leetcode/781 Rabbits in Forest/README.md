<h2><a href="https://leetcode.com/problems/rabbits-in-forest">781. Rabbits in Forest</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>In a forest, each rabbit tells you how many other rabbits have the same color as itself. You are given an integer array <code>answers</code> where <code>answers[i]</code> is the answer of the <code>i-th</code> rabbit.</p>

<p>Return <strong>the minimum number of rabbits</strong that could be in the forest.</p>

---

### Example 1

<pre>
Input: answers = [1,1,2]
Output: 5
Explanation:
- The two rabbits that answered "1" could be of the same color (2 rabbits in total).
- The rabbit that answered "2" implies there are 3 rabbits of that color.
- So minimum rabbits = 2 + 3 = 5
</pre>

### Example 2

<pre>
Input: answers = [10,10,10]
Output: 11
</pre>

---

### Constraints

<ul>
<li>1 ≤ answers.length ≤ 1000</li>
<li>0 ≤ answers[i] ≤ 1000</li>
</ul>

---

# Solution

### Approach (Hash Map / Counting)

Key ideas:

1. If a rabbit says <code>x</code>, there are <code>x + 1</code> rabbits of that color.
2. Count how many rabbits give the same answer.
3. For each unique answer:
   - Divide the count by <code>x + 1</code> to get the number of groups.
   - Round up using ceiling to cover all rabbits.
   - Multiply by <code>x + 1</code> to get total rabbits for this color.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

### Tags

hash table, math, greedy, counting
