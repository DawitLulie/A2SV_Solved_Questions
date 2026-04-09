<h2><a href="https://leetcode.com/problems/search-a-2d-matrix">74. Search a 2D Matrix</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an <code>m x n</code> integer matrix <code>matrix</code> with the following properties:</p>

<ul>
<li>Each row is sorted in non-decreasing order.</li>
<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p>Given an integer <code>target</code>, return <strong>true</strong> if <code>target</code> is in the matrix or <strong>false</strong> otherwise.</p>

---

### Example 1

<pre>
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
</pre>

### Example 2

<pre>
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
</pre>

---

### Constraints

<ul>
<li>m == matrix.length</li>
<li>n == matrix[i].length</li>
<li>1 ≤ m, n ≤ 100</li>
<li>-10<sup>4</sup> ≤ matrix[i][j], target ≤ 10<sup>4</sup></li>
</ul>

---

# Solution

### Approach (Binary Search)

We can treat the matrix as a single sorted array.

If the matrix has <code>m</code> rows and <code>n</code> columns:
- Total elements = <code>m * n</code>
- Index mapping:
  - Row = <code>mid // n</code>
  - Column = <code>mid % n</code>

Steps:

1. Set <code>left = 0</code> and <code>right = m * n - 1</code>.
2. While <code>left ≤ right</code>:
   - Compute <code>mid</code>.
   - Convert to matrix index:
     - <code>row = mid // n</code>
     - <code>col = mid % n</code>
   - Compare <code>matrix[row][col]</code> with target:
     - If equal → return true
     - If smaller → search right
     - If larger → search left
3. Return false if not found.

**Why this works:**  
The matrix behaves like a sorted 1D array, so binary search can be applied directly.

---

### Complexity

- **Time Complexity:** O(log(m * n))  
- **Space Complexity:** O(1)

---

### Tags

binary search, matrix