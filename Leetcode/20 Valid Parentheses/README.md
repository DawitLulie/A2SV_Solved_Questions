<h2><a href="https://leetcode.com/problems/valid-parentheses">20. Valid Parentheses</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>Given a string <code>s</code> containing just the characters 
<code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, <code>'['</code> and <code>']'</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ul>
<li>Open brackets must be closed by the same type of brackets.</li>
<li>Open brackets must be closed in the correct order.</li>
<li>Every closing bracket has a corresponding open bracket of the same type.</li>
</ul>

---

### Example 1

<pre>
Input: s = "()"
Output: true
</pre>

### Example 2

<pre>
Input: s = "()[]{}"
Output: true
</pre>

### Example 3

<pre>
Input: s = "(]"
Output: false
</pre>

---

### Constraints

<ul>
<li>1 ≤ s.length ≤ 10⁴</li>
<li>s consists of parentheses only: <code>()[]{}</code>.</li>
</ul>

---

### Solution

**Approach (Stack):**

We use a **stack** to track opening brackets.

Steps:

1. Traverse the string character by character.
2. If the character is an **opening bracket** (`(`, `{`, `[`), push it onto the stack.
3. If it is a **closing bracket** (`)`, `}`, `]`):
   - Check if the stack is empty → return `False`.
   - Pop the top element and verify it matches the corresponding opening bracket.
4. After processing the entire string:
   - If the stack is empty → the string is valid.
   - Otherwise → invalid.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Where `n` is the length of the string.

---

### Tags

stack, string