<h2><a href="https://leetcode.com/problems/longest-consecutive-sequence">128. Longest Consecutive Sequence</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>Given an unsorted array of integers <code>nums</code>, return the length of the longest consecutive elements sequence.</p>

<p>You must write an algorithm that runs in <strong>O(n)</strong> time.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1,2,3,4]. Therefore its length is 4.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= nums.length &lt;= 10⁵</li>
  <li>-10⁹ &lt;= nums[i] &lt;= 10⁹</li>
</ul>

---

### Solution

**Approach:**  
- Use a set to achieve O(1) lookups.  
- Iterate through numbers and start counting a sequence only from numbers that are the beginning of a sequence (`num - 1` not in set).  
- Expand the sequence by checking consecutive numbers in the set.  
- Keep track of the maximum length.

**Complexity:**  
- Time: O(n) — each number is checked at most twice  
- Space: O(n) — storing numbers in a set  

---
