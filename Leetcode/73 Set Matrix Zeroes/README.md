<h2><a href="https://leetcode.com/problems/set-matrix-zeroes">73. Set Matrix Zeroes</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>. You must do it <strong>in-place</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>m == matrix.length</li>
  <li>n == matrix[0].length</li>
  <li>1 &lt;= m, n &lt;= 200</li>
  <li>-2³¹ &lt;= matrix[i][j] &lt;= 2³¹ - 1</li>
</ul>

<p><strong>Follow-up:</strong></p>
<ul>
  <li>A straightforward solution uses O(mn) space.</li>
  <li>Could you devise a constant space solution?</li>
</ul>

---

### Solution

**Approach:**  
- Use the first row and first column as markers to indicate which rows and columns should be zeroed.  
- First, check if the first row and first column themselves need to be zero.  
- Then, iterate through the rest of the matrix and mark zeros in first row/column.  
- Finally, zero the rows and columns based on the markers.  
- Handle the first row and first column at the end.

**Complexity:**  
- Time: O(m * n) — traverse all elements  
- Space: O(1) — in-place using matrix itself as marker  

---
