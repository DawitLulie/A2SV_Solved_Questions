<h2><a href="https://leetcode.com/problems/removing-stars-from-a-string">2390. Removing Stars From a String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a string <code>s</code>, which contains stars <code>*</code>.</p>

<p>In one operation, you can:</p>

<ul>
<li>Choose a star in <code>s</code>.</li>
<li>Remove the closest <strong>non-star</strong> character to its left, as well as remove the star itself.</li>
</ul>

<p>Return the string after <strong>all stars have been removed</strong>.</p>

<p><strong>Note:</strong></p>
<ul>
<li>The input will be generated such that the operation is always possible.</li>
<li>It can be shown that the resulting string will always be unique.</li>
</ul>

---

### Example 1

<pre>
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation:
Remove stars one by one:
"leet**cod*e"
→ "lee*cod*e"
→ "lecod*e"
→ "lecoe"
</pre>

### Example 2

<pre>
Input: s = "erase*****"
Output: ""
Explanation:
Each star removes one character to its left.
</pre>

---

### Constraints

<ul>
<li>1 ≤ s.length ≤ 10⁵</li>
<li><code>s</code> consists of lowercase English letters and stars <code>*</code>.</li>
<li>The operation above can always be performed.</li>
</ul>

---

### Solution

**Approach (Stack):**

We use a **stack** to simulate removing characters.

Steps:

1. Traverse the string character by character.
2. If the character is not `'*'`, push it onto the stack.
3. If the character is `'*'`, pop the last character from the stack (this removes the closest non-star character to the left).
4. After processing the entire string, join the stack to form the final string.

This works because the stack always keeps track of the characters that remain after processing previous stars.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Where `n` is the length of the string.

---

### Tags

stack, string, simulation