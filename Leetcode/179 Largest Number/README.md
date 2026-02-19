<h2><a href="https://leetcode.com/problems/largest-number">179. Largest Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number and return it as a string.</p>

<p>Since the result may be very large, return it as a string instead of an integer.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [10,2]
Output: "210"
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [3,30,34,5,9]
Output: "9534330"
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1]
Output: "1"
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 100</li>
  <li>0 &lt;= nums[i] &lt;= 10⁹</li>
  <li>The result is guaranteed to fit in a 32-bit integer when concatenated as a number, but should be returned as a string.</li>
</ul>

---

### Solution

**Approach:**  
- Convert all numbers to strings.  
- Sort the strings using a custom comparator: for two numbers a and b, compare <code>a+b</code> and <code>b+a</code>.  
- Concatenate the sorted strings.  
- Handle the edge case where the first character is '0' (all numbers are zeros).

**Complexity:**  
- Time: O(n log n) — sorting n numbers with string comparison  
- Space: O(n) — for storing string representations  

---
