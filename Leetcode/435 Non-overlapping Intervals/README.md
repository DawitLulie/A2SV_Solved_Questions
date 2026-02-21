<h2><a href="https://leetcode.com/problems/non-overlapping-intervals">435. Non-overlapping Intervals</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of <code>intervals</code> where <code>intervals[i] = [startᵢ, endᵢ]</code>, return <em>the minimum number of intervals you need to remove</em> to make the rest of the intervals non-overlapping.</p>

<p><strong>Note:</strong> Intervals that only touch at a point (e.g., [1,2] and [2,3]) are considered non-overlapping.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: Remove [1,3] and the rest are non-overlapping.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two intervals.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: They are already non-overlapping.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ intervals.length ≤ 10⁵</li>
  <li>intervals[i].length == 2</li>
  <li>-5 × 10⁴ ≤ startᵢ < endᵢ ≤ 5 × 10⁴</li>
</ul>

---

###  Solution

**Approach (Greedy):**

- Sort intervals by their **end time** in ascending order.
- Keep track of the end of the last non-overlapping interval.
- If the current interval overlaps (start < previous_end), increment removal count.
- Otherwise, update previous_end.

This works because choosing intervals with the earliest end time leaves maximum room for future intervals.

**Complexity:**

- Time: O(n log n) — sorting  
- Space: O(1) extra  

---