<h2><a href="https://codeforces.com/problemset/problem/5/C">5C. Longest Regular Bracket Sequence</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1900-red' alt='Difficulty: 1900' />
<hr>

<p>Given a string <code>s</code> consisting of characters <code>'('</code> and <code>')'</code>, find the length of the <strong>longest regular bracket sequence</strong> (valid parentheses substring).</p>

<p>Also, count how many such substrings of maximum length exist. If no valid substring exists, output <code>0 1</code>.</p>

---

### Example 1

<pre>
Input: s = "((())))(()())"
Output: 6 2
Explanation:
The longest valid bracket substrings are "((()))" and "(()())", both of length 6.
</pre>

### Example 2

<pre>
Input: s = "))))"
Output: 0 1
Explanation:
No valid substrings exist.
</pre>

---

### Constraints

<ul>
<li>1 ≤ |s| ≤ 10⁶</li>
<li>s consists only of '(' and ')'</li>
</ul>

---

# Solution

### Approach (Stack + Index)

We use a stack of indices to track the positions of '(' and help calculate lengths of valid substrings.

1. Initialize a stack with <code>stack = [-1]</code> to handle the base for lengths.
2. Iterate over the string:
   - If <code>s[i] == '('</code>, push <code>i</code> onto the stack.
   - If <code>s[i] == ')'</code>:
     - Pop the top of the stack.
     - If the stack becomes empty, push the current index <code>i</code> as a new base.
     - Else, calculate <code>length = i - stack[-1]</code> and update:
       - <code>max_len</code> if length > max_len
       - Count of max length substrings if length == max_len
3. If no valid substrings, return <code>0 1</code>.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

---

### Tags

stack, string, greedy, implementation
