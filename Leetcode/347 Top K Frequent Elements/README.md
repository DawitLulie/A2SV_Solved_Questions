<h2><a href="https://leetcode.com/problems/top-k-frequent-elements">347. Top K Frequent Elements</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the <strong>k most frequent elements</strong>. You may return the answer in any order.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [1], k = 1
Output: [1]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 10⁵</li>
  <li>k is in the range [1, number of unique elements in the array]</li>
  <li>The answer is unique.</li>
</ul>

<p><strong>Follow-up:</strong> Can you solve it in <code>O(n)</code> time?</p>

---

### Solution

**Approach:**  
- Use a hash map (Counter) to count frequency of each element.  
- Use a heap (priority queue) or bucket sort to find the top k frequent elements efficiently.  
- Return the k elements with highest frequency.

**Complexity:**  
- Time: O(n log k) — using a heap  
- Space: O(n) — for storing counts  

---
