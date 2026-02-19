<h2><a href="https://leetcode.com/problems/group-anagrams">49. Group Anagrams</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of strings <code>strs</code>, group the anagrams together. You can return the answer in any order.</p>

<p>An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: strs = [""]
Output: [[""]]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: strs = ["a"]
Output: [["a"]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= strs.length &lt;= 10⁴</li>
  <li>0 &lt;= strs[i].length &lt;= 100</li>
  <li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
- Use a dictionary to map a sorted tuple of each string to all strings that match that key.  
- All strings that are anagrams will have the same sorted character tuple.

**Complexity:**  
- Time: O(n * k log k) — n = number of strings, k = max length of string (sorting each string)  
- Space: O(n * k) — storing grouped strings  

---
