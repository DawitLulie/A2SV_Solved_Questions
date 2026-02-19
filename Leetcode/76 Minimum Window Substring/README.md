<h2><a href="https://leetcode.com/problems/minimum-window-substring">76. Minimum Window Substring</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given two strings <code>s</code> and <code>t</code>, return the minimum window substring of <code>s</code> such that every character in <code>t</code> (including duplicates) is included in the window. If there is no such substring, return <code>""</code>.</p>

<p>The testcases will be generated such that the answer is unique.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" contains all characters A, B, and C.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "a", t = "a"
Output: "a"
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "a", t = "aa"
Output: ""
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length, t.length &lt;= 10⁵</li>
  <li><code>s</code> and <code>t</code> consist of English letters.</li>
</ul>

---

### Solution

**Approach:**  
- Use the sliding window technique with two pointers (left and right).  
- Maintain a frequency counter for characters in <code>t</code>.  
- Expand the window by moving the right pointer and shrink from left to minimize the window while still covering all characters.  
- Keep track of the minimum length and update the result.

**Complexity:**  
- Time: O(n + m) — n = length of s, m = length of t  
- Space: O(1) — fixed alphabet size for frequency counts  

---
