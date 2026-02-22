<h2><a href="https://leetcode.com/problems/count-the-digits-that-divide-a-number">2520. Count the Digits That Divide a Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer <code>num</code>, return <em>the number of digits in <code>num</code> that divide <code>num</code> evenly</em>.</p>

<p>A digit divides <code>num</code> if the remainder of <code>num</code> divided by that digit is 0.  
Digits 0 should be ignored.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: num = 1012
Output: 3
Explanation:
Digits are 1,0,1,2
1 divides 1012 → yes
0 → ignore
1 divides 1012 → yes
2 divides 1012 → yes
Total count = 3
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: num = 12
Output: 2
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ num ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**  
- Convert number to string to iterate its digits.  
- For each digit d (≠ 0), check if <code>num % d == 0</code>.  
- Count all digits that divide num.

**Complexity:**  
- Time: O(log₁₀(num)) — proportional to number of digits  
- Space: O(1) extra  

---