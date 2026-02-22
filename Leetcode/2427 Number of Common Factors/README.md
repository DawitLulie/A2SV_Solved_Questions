<h2><a href="https://leetcode.com/problems/number-of-common-factors">2427. Number of Common Factors</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given two positive integers <code>a</code> and <code>b</code>, return <em>the number of common factors of a and b</em>.</p>

<p>A factor of a number is an integer that divides it evenly.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: a = 12, b = 6
Output: 4
Explanation: The common factors are 1, 2, 3, 6
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: a = 25, b = 30
Output: 2
Explanation: The common factors are 1 and 5
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ a, b ≤ 1000</li>
</ul>

---

###  Solution

**Approach:**  
- Iterate from 1 to min(a, b).  
- Count numbers that divide both a and b evenly.

**Complexity:**  
- Time: O(min(a, b))  
- Space: O(1)  

---