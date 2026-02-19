<h2><a href="https://leetcode.com/problems/merge-intervals">56. Merge Intervals</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of intervals where <code>intervals[i] = [start_i, end_i]</code>, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap, so merge them into [1,6].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= intervals.length &lt;= 10⁴</li>
  <li>intervals[i].length == 2</li>
  <li>0 &lt;= start_i &lt;= end_i &lt;= 10⁴</li>
</ul>

---

### Solution

**Approach:**  
- Sort intervals by starting time.  
- Iterate and merge intervals if the current interval overlaps with the previous one.  
- Otherwise, add it as a new interval in the result.

**Complexity:**  
- Time: O(n log n) — sorting intervals  
- Space: O(n) — for storing the merged intervals  

---
