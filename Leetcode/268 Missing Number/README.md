<h2><a href="https://leetcode.com/problems/missing-number">268. Missing Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return the only number in the range that is missing from the array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3, numbers are [0,1,2,3], missing number is 2.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,1]
Output: 2
Explanation: n = 2, numbers are [0,1,2], missing number is 2.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>n == nums.length</li>
  <li>1 &lt;= n &lt;= 10⁴</li>
  <li>0 &lt;= nums[i] &lt;= n</li>
  <li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

---

### Solution

**Approach:**  
- Use the formula for the sum of first n natural numbers: `sum_expected = n * (n + 1) / 2`.  
- Subtract the sum of elements in `nums` from `sum_expected` to get the missing number.  
- Alternatively, use XOR to find the missing number in O(n) time and O(1) space.

**Complexity:**  
- Time: O(n) — sum or XOR over all elements  
- Space: O(1) — constant space  

---
