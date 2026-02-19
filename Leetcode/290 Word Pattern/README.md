<h2><a href="https://leetcode.com/problems/word-pattern">290. Word Pattern</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a pattern and a string <code>s</code>, return <code>true</code> if <code>s</code> follows the same pattern.</p>

<p>Here, "follow" means there is a bijection between a letter in <code>pattern</code> and a non-empty word in <code>s</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= pattern.length &lt;= 300</li>
  <li>pattern contains only lowercase English letters.</li>
  <li>1 &lt;= s.length &lt;= 3000</li>
  <li>s contains only lowercase English letters and spaces <code>' '</code>.</li>
  <li>Words in <code>s</code> are separated by a single space.</li>
  <li>No leading or trailing spaces.</li>
</ul>

---

### Solution

**Approach:**  
- Split the string `s` into words.  
- Check if the number of words matches the length of the pattern.  
- Use two dictionaries (or a single mapping with checking) to map pattern letters to words and words to pattern letters.  
- If any inconsistency is found, return False; otherwise, return True.

**Complexity:**  
- Time: O(n) — n = number of words (or length of pattern)  
- Space: O(n) — for storing mappings  

---
