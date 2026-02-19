<h2><a href="https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons">452. Minimum Number of Arrows to Burst Balloons</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code>points</code> where <code>points[i] = [x_start, x_end]</code> denotes a balloon whose horizontal diameter stretches between <code>x_start</code> and <code>x_end</code>.</p>

<p>You do not know the exact y-coordinates of the balloons.</p>

<p>An arrow can be shot up exactly vertically (along the y-axis) from different points along the x-axis. A balloon with <code>x_start</code> and <code>x_end</code> is burst by an arrow shot at <code>x</code> if <code>x_start &lt;= x &lt;= x_end</code>.</p>

<p>Return <em>the minimum number of arrows</em> that must be shot to burst all balloons.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One arrow at x = 6 bursts [2,8] and [1,6].
Another arrow at x = 11 bursts [10,16] and [7,12].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= points.length &lt;= 10⁵</li>
  <li>points[i].length == 2</li>
  <li>-2³¹ &lt;= x_start &lt; x_end &lt;= 2³¹ - 1</li>
</ul>

---

### Solution

**Approach:**  
- Sort the balloons by their ending coordinate.  
- Initialize the first arrow at the end of the first balloon.  
- Iterate through the balloons:
  - If the current balloon starts after the arrow position, shoot a new arrow.
  - Otherwise, the current balloon is already burst.
- Count the number of arrows used.

This is a classic greedy interval problem.

**Complexity:**  
- Time: O(n log n) — sorting the intervals  
- Space: O(1) — ignoring sorting space  

---
