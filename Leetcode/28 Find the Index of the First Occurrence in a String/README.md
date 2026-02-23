<h2><a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string">28. Find the Index of the First Occurrence in a String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two strings <code>haystack</code> and <code>needle</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs first at index 0.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: haystack = "leetcode", needle = "leeto"
Output: -1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ haystack.length, needle.length ≤ 10⁴</li>
  <li>haystack and needle consist of only lowercase English characters.</li>
</ul>

---

###  Solution

**Approach:**  
- Use built-in string search (`str.find`) in Python for simplicity.
- Alternatively, implement KMP (Knuth–Morris–Pratt) algorithm for O(n) worst-case time.

**Complexity:**  
- Time: O(n * m) in naive search, O(n + m) with KMP (n = length of haystack, m = length of needle)  
- Space: O(1) extra (or O(m) for KMP preprocessing)  

---