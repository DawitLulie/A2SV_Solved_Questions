<h2><a href="https://leetcode.com/problems/optimal-partition-of-string">2405. Optimal Partition of String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a string <code>s</code>. You need to partition the string into one or more substrings such that the characters in each substring are unique. Return the <strong>minimum number of substrings</strong> in such a partition.</p>

<p>Notice that each character should belong to exactly one substring in a partition.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "abac"
Output: 2
Explanation: Two substrings can be "ab" and "ac".
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "world"
Output: 1
Explanation: All characters in "world" are unique, so only one substring is needed.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "dddd"
Output: 4
Explanation: Each "d" must be in a separate substring to keep characters unique.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ s.length ≤ 10⁵</li>
  <li><code>s</code> consists of only lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
- Use a set to keep track of characters in the current substring.  
- Iterate through the string:  
  - If the character is already in the set, start a new substring and clear the set.  
  - Otherwise, add the character to the set.  
- Count the total number of substrings formed.

**Complexity:**  
- Time: O(n) — we visit each character once  
- Space: O(1) — the set can have at most 26 characters  

---