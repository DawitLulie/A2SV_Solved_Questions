<h2><a href="https://leetcode.com/problems/score-of-parentheses">856. Score of Parentheses</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a balanced parentheses string <code>s</code>, return the score of the string.</p>

<p>The score of a balanced parentheses string is based on the following rules:</p>

<ul>
<li><code>()</code> has score <strong>1</strong>.</li>
<li><code>AB</code> has score <code>A + B</code>, where <code>A</code> and <code>B</code> are balanced parentheses strings.</li>
<li><code>(A)</code> has score <code>2 × A</code>, where <code>A</code> is a balanced parentheses string.</li>
</ul>

---

### Example 1

<pre>
Input: s = "()"
Output: 1
</pre>

### Example 2

<pre>
Input: s = "(())"
Output: 2
</pre>

### Example 3

<pre>
Input: s = "()()"
Output: 2
</pre>

### Example 4

<pre>
Input: s = "(()(()))"
Output: 6
</pre>

---

### Constraints

<ul>
<li>2 ≤ s.length ≤ 50</li>
<li>s consists only of '(' and ')'</li>
<li>s is a balanced parentheses string</li>
</ul>

---

### Solution

**Approach (Stack):**

We use a stack to compute the score based on the structure of the parentheses.

Steps:

1. Initialize a stack and push `0` to represent the current score level.
2. Traverse each character in the string:
   - If `'('`, push `0` onto the stack to start a new score level.
   - If `')'`:
     - Pop the top value `v`.
     - If `v == 0`, it means we found `"()"`, so the score is `1`.
     - Otherwise the score becomes `2 * v`.
     - Add this score to the previous level on the stack.
3. The final score will be the remaining value in the stack.

This works because the stack naturally handles nested parentheses.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Where `n` is the length of the string.

---

### Tags

stack, string