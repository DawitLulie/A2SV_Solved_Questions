<h2><a href="https://leetcode.com/problems/valid-anagram">242. Valid Anagram</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise.</p>

<p>An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "anagram", t = "nagaram"
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "rat", t = "car"
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length, t.length &lt;= 5 * 10⁴</li>
  <li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
- Use a hash map (Counter) to count characters in both strings.  
- Compare the counts; if they are equal, the strings are anagrams.  
- Alternatively, sort both strings and compare.

**Complexity:**  
- Time: O(n) — n = length of strings (for counting)  
- Space: O(1) — at most 26 characters  

---
