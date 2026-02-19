<h2><a href="https://leetcode.com/problems/spiral-matrix">54. Spiral Matrix</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an <code>m x n</code> matrix, return all elements of the matrix in spiral order.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>m == matrix.length</li>
  <li>n == matrix[i].length</li>
  <li>1 &lt;= m, n &lt;= 10</li>
  <li>-100 &lt;= matrix[i][j] &lt;= 100</li>
</ul>

---

### Solution

**Approach:**  
- Use four boundaries: top, bottom, left, right.  
- Traverse in the order: top row → right column → bottom row → left column.  
- Shrink the boundaries after completing each side.  
- Repeat until all elements are traversed.

**Complexity:**  
- Time: O(m * n) — each element is visited once  
- Space: O(1) — only storing output array  

---
