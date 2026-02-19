<h2><a href="https://leetcode.com/problems/longest-common-prefix">14. Longest Common Prefix</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: strs = ["flower","flow","flight"]
Output: "fl"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= strs.length &lt;= 200</li>
  <li>0 &lt;= strs[i].length &lt;= 200</li>
  <li><code>strs[i]</code> consists of only lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
- Compare characters column by column among all strings.  
- Stop when a mismatch is found or any string ends.

**Complexity:**  
- Time: O(n * m) — n = number of strings, m = length of shortest string  
- Space: O(1)  

---
