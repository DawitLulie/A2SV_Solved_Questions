<h2><a href="https://leetcode.com/problems/decode-string">394. Decode String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an encoded string, return its decoded string.</p>

<p>The encoding rule is:</p>

<pre>
k[encoded_string]
</pre>

<p>where the <code>encoded_string</code> inside the square brackets is repeated exactly <code>k</code> times. Note that <code>k</code> is guaranteed to be a positive integer.</p>

<p>You may assume that the input string is always valid, meaning:</p>

<ul>
<li>No extra white spaces</li>
<li>Square brackets are well-formed</li>
<li>Digits are only used for repeat numbers</li>
</ul>

<p>The decoded string will not exceed <code>10⁵</code> characters.</p>

---

### Example 1

<pre>
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
</pre>

### Example 2

<pre>
Input: s = "3[a2[c]]"
Output: "accaccacc"
</pre>

### Example 3

<pre>
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
</pre>

---

### Constraints

<ul>
<li>1 ≤ s.length ≤ 30</li>
<li>s consists of lowercase English letters, digits, and square brackets <code>[]</code></li>
<li>1 ≤ k ≤ 300</li>
</ul>

---

### Solution

**Approach (Stack):**

We use a stack to handle nested encoded patterns.

Steps:

1. Traverse the string character by character.
2. If the character is not `]`, push it onto the stack.
3. When `]` appears:
   - Pop characters until `[` to get the encoded string.
   - Pop digits to determine the repeat number `k`.
   - Repeat the substring `k` times.
   - Push the expanded string back to the stack.
4. At the end, join all elements in the stack to form the final decoded string.

This approach naturally handles nested structures like `3[a2[c]]`.

---

### Complexity

- **Time Complexity:** O(n * k) in the worst case  
- **Space Complexity:** O(n)

Where `n` is the length of the string.

---

### Tags

stack, string, recursion