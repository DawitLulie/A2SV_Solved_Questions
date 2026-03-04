<h2><a href="https://leetcode.com/problems/range-sum-query-2d-immutable">304. Range Sum Query 2D - Immutable</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type:</p>

<p>Calculate the sum of the elements inside the rectangle defined by its upper left corner 
<code>(row1, col1)</code> and lower right corner <code>(row2, col2)</code>.</p>

<p>Implement the <code>NumMatrix</code> class:</p>

<ul>
  <li><code>NumMatrix(int[][] matrix)</code> initializes the object with the integer matrix <code>matrix</code>.</li>
  <li><code>int sumRegion(int row1, int col1, int row2, int col2)</code> returns the sum of the elements of <code>matrix</code> inside the rectangle defined by <code>(row1, col1)</code> and <code>(row2, col2)</code>.</li>
</ul>

---

### Example

<pre>
Input:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],
   [5,6,3,2,1],
   [1,2,0,1,5],
   [4,1,0,1,7],
   [1,0,3,0,5]]],
 [2,1,4,3],
 [1,1,2,2],
 [1,2,2,4]]

Output:
[null, 8, 11, 12]
</pre>

---

### Constraints

<ul>
  <li>m == matrix.length</li>
  <li>n == matrix[i].length</li>
  <li>1 ≤ m, n ≤ 200</li>
  <li>-10⁵ ≤ matrix[i][j] ≤ 10⁵</li>
  <li>0 ≤ row1 ≤ row2 &lt; m</li>
  <li>0 ≤ col1 ≤ col2 &lt; n</li>
  <li>At most 10⁴ calls will be made to <code>sumRegion</code>.</li>
</ul>

---

### Solution

**Approach (2D Prefix Sum):**

We precompute a 2D prefix sum matrix where:

<pre>
prefix[r][c] = sum of all elements from (0,0) to (r-1,c-1)
</pre>

To avoid edge cases, we create a prefix matrix of size (m+1) × (n+1).

Formula to build prefix:

<pre>
prefix[r][c] =
matrix[r-1][c-1]
+ prefix[r-1][c]
+ prefix[r][c-1]
- prefix[r-1][c-1]
</pre>

To answer a query:

<pre>
sumRegion(row1, col1, row2, col2) =
prefix[row2+1][col2+1]
- prefix[row1][col2+1]
- prefix[row2+1][col1]
+ prefix[row1][col1]
</pre>

**Why this works:**

The prefix matrix allows us to compute any submatrix sum in O(1) time after O(m × n) preprocessing.

---

### Complexity

- **Time:**
  - Initialization: O(m × n)
  - Each query: O(1)

- **Space:** O(m × n)

---

### Tags

array, prefix sum, matrix, design