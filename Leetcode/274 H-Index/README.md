<h2><a href="https://leetcode.com/problems/h-index">274. H-Index</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of integers <code>citations</code> where <code>citations[i]</code> is the number of citations a researcher received for their <code>i<sup>th</sup></code> paper, return <em>the researcher's h-index</em>.</p>

<p>A scientist has an <strong>h-index</strong> of <code>h</code> if <code>h</code> of their <code>n</code> papers have at least <code>h</code> citations each, and the other <code>n - h</code> papers have ≤ <code>h</code> citations each.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: 3 papers have at least 3 citations each.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: citations = [1,3,1]
Output: 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ citations.length ≤ 5000</li>
  <li>0 ≤ citations[i] ≤ 1000</li>
</ul>

<p><strong>Follow-up:</strong> Could you solve it in <code>O(n)</code> time?</p>

---

###  Solution

**Approach:**  
- Sort the `citations` array in descending order.  
- Iterate through the sorted array, find the largest `h` such that at least `h` papers have ≥ `h` citations.  
- Return `h`.

**Complexity:**  
- Time: O(n log n) — sorting  
- Space: O(1) extra  

---