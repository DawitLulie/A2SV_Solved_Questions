<h2><a href="https://leetcode.com/problems/palindrome-number">9. Palindrome Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a palindrome, and <code>false</code> otherwise.</p>

<p>An integer is a palindrome when it reads the same backward as forward.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and right to left.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: x = 10
Output: false
Explanation: Reads 10 from left to right, 01 from right to left.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</li>
</ul>

<p><strong>Follow-up:</strong> Could you solve it without converting the integer to a string?</p>

---

### Solution

**Approach:**  
- Convert the number to a string and check if it equals its reverse.  
- Or reverse half of the number mathematically and compare with the other half (no string conversion).

**Complexity:**  
- Time: O(log₁₀(n)) — number of digits  
- Space: O(1)  

---
