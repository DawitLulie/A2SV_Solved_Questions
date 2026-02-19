<h2><a href="https://leetcode.com/problems/rotate-image">48. Rotate Image</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an <code>n x n</code> 2D matrix representing an image, rotate the image by 90 degrees (clockwise) in-place.</p>

<p>You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **Do not** allocate another 2D matrix.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>n == matrix.length == matrix[i].length</li>
  <li>1 &lt;= n &lt;= 20</li>
  <li>-1000 &lt;= matrix[i][j] &lt;= 1000</li>
</ul>

---

### Solution

**Approach:**  
- First, transpose the matrix (swap rows with columns).  
- Then, reverse each row to rotate 90 degrees clockwise.

**Complexity:**  
- Time: O(n²)  
- Space: O(1) — in-place rotation  

---
