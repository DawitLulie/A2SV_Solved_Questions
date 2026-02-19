<h2><a href="https://leetcode.com/problems/insert-interval">57. Insert Interval</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a set of non-overlapping intervals <code>intervals</code> sorted by their start times, insert a new interval <code>newInterval</code> into <code>intervals</code> such that the intervals remain non-overlapping (merge overlapping intervals if necessary).</p>

<p>Return <em>the updated list of intervals</em>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: The new interval [4,8] overlaps with [3,5],[6,7],[8,10].
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>0 &lt;= intervals.length &lt;= 10⁴</li>
  <li>intervals[i].length == 2</li>
  <li>0 &lt;= start_i &lt;= end_i &lt;= 10⁵</li>
  <li>intervals is sorted by <code>start_i</code></li>
  <li>newInterval.length == 2</li>
  <li>0 &lt;= start &lt;= end &lt;= 10⁵</li>
</ul>

---

### Solution

**Approach:**  
- Iterate through intervals.  
- Add all intervals that end before the new interval starts.  
- Merge all overlapping intervals with the new interval.  
- Add remaining intervals after the new interval.

**Complexity:**  
- Time: O(n) — single pass through intervals  
- Space: O(n) — for the output list  

---
