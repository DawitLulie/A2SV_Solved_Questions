<h2><a href="https://leetcode.com/problems/majority-element-ii">229. Majority Element II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, find all elements that appear more than ⌊n / 3⌋ times. You must implement an algorithm with linear time complexity and O(1) space complexity.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [3,2,3]
Output: [3]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1,1,1,3,3,2,2,2]
Output: [1,2]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 5 * 10⁴</li>
  <li>-10⁹ &lt;= nums[i] &lt;= 10⁹</li>
</ul>

---

### Solution

**Approach:**  
- Use the Boyer-Moore Voting Algorithm extension for n/3 majority elements.  
- Maintain two candidate elements and their counts.  
- First pass: find potential candidates.  
- Second pass: verify which candidates appear more than n/3 times.

**Complexity:**  
- Time: O(n) — two passes through the array  
- Space: O(1) — only storing two candidates and counts  

---
