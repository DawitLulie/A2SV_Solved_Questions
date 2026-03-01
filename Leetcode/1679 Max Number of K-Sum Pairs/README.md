<h2><a href="https://leetcode.com/problems/max-number-of-k-sum-pairs">1679. Max Number of K-Sum Pairs</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. In one operation, you can pick two numbers from the array whose sum equals <code>k</code> and remove them from the array.</p>

<p>Return the <strong>maximum number of operations</strong> you can perform on the array.</p> :contentReference[oaicite:0]{index=0}

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3,4], k = 5
Output: 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [3,1,3,4,3], k = 6
Output: 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 10⁵</li>
  <li>1 ≤ nums[i] ≤ 10⁹</li>
  <li>1 ≤ k ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Hash Map):**  
- Use a hash map (dictionary) to track the counts of needed complements.  
- For each number, check if its complement (`k - num`) is already in the map. If so, a pair is formed — increment the answer and decrement the complement count. Otherwise, store the need for this number in the map. :contentReference[oaicite:1]{index=1}

**Complexity:**  
- Time: O(n) — traverse the array once  
- Space: O(n) — for the hash map  

---
