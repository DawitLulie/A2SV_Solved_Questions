<h2><a href="https://leetcode.com/problems/roman-to-integer">13. Roman to Integer</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a Roman numeral string <code>s</code>, convert it to an integer.</p>

<p>Roman numerals are represented by these symbols:</p>
<ul>
  <li>I = 1</li>
  <li>V = 5</li>
  <li>X = 10</li>
  <li>L = 50</li>
  <li>C = 100</li>
  <li>D = 500</li>
  <li>M = 1000</li>
</ul>

<p>Roman numerals are usually written largest to smallest from left to right.  
However, some numbers are formed by placing a smaller numeral before a larger one, for example:</p>
<ul>
  <li>IV = 4</li>
  <li>IX = 9</li>
  <li>XL = 40</li>
  <li>XC = 90</li>
  <li>CD = 400</li>
  <li>CM = 900</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "III"
Output: 3
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 15</li>
  <li><code>s</code> contains only the characters ('I','V','X','L','C','D','M').</li>
  <li>It is guaranteed that <code>s</code> is a valid Roman numeral in the range [1, 3999].</li>
</ul>

---

### Solution

**Approach:**  
- Use a dictionary mapping Roman symbols to integer values.  
- Iterate through the string. If the current symbol is smaller than the next one, subtract it; otherwise, add it.

**Complexity:**  
- Time: O(n) — length of the string  
- Space: O(1)  

---
