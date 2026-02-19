<h2><a href="https://leetcode.com/problems/happy-number">202. Happy Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>A <strong>happy number</strong> is defined by the following process:</p>
<ul>
  <li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
  <li>Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.</li>
</ul>

<p>Return <code>true</code> if <code>n</code> is a happy number, otherwise return <code>false</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 19
Output: true
Explanation: 
1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 2
Output: false
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= n &lt;= 2³¹ - 1</li>
</ul>

---

### Solution

**Approach:**  
- Use a set to detect cycles while repeatedly computing the sum of squares of digits.  
- If the sum reaches 1, return True.  
- If a repeated number is encountered, return False.

**Complexity:**  
- Time: O(log n) per iteration — number of digits in n  
- Space: O(log n) — to store visited numbers in a set  

---
