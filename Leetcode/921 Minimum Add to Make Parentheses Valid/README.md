<h2><a href="https://leetcode.com/problems/minimum-add-to-make-parentheses-valid">921. Minimum Add to Make Parentheses Valid</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>s</code> of <strong>'('</strong> and <strong>')'</strong> parentheses, return the minimum number of parentheses we must add to make the resulting string valid.</p>

<p>A parentheses string is valid if:</p>
<ul>
  <li>It is the empty string, or</li>
  <li>It can be written as <code>AB</code> (A concatenated with B), where A and B are valid strings, or</li>
  <li>It can be written as <code>(A)</code>, where A is a valid string.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "())"
Output: 1
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "((("
Output: 3
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "()"
Output: 0
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ s.length ≤ 1000</li>
  <li><code>s[i]</code> is either <strong>'('</strong> or <strong>')'</strong>.</li>
</ul>

---

### Solution

**Approach:**  
- Use a counter to track open parentheses balance.  
- Initialize `open_count = 0` and `additions = 0`.  
- Iterate through each character:  
  - If '(', increment `open_count`.  
  - If ')', decrement `open_count`. If `open_count` becomes negative, increment `additions` and reset `open_count` to 0.  
- After iteration, add remaining `open_count` to `additions`.  

**Complexity:**  
- Time: O(n) — iterate through the string once  
- Space: O(1) — only counters are used  

---