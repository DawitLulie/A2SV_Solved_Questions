<h2><a href="https://leetcode.com/problems/integer-to-roman">12. Integer to Roman</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer <code>num</code>, convert it to a Roman numeral.</p>

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

<p>Roman numerals are usually written largest to smallest from left to right. However, certain numbers are formed by placing a smaller numeral before a larger one, for example:</p>
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
Input: num = 3
Output: "III"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90, IV = 4.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= num &lt;= 3999</li>
</ul>

---

### Solution

**Approach:**  
- Use a list of tuples mapping Roman numerals to their integer values in descending order.  
- Iterate through the list and append symbols while subtracting values from <code>num</code>.

**Complexity:**  
- Time: O(1) — constant because <code>num &lt;= 3999</code>  
- Space: O(1)  

---
