<h2><a href="https://codeforces.com/problemset/problem/611/C">611C. New Year and Domino</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1500-yellow' alt='Difficulty: 1500' />
<hr>

<p>You are given a grid of size <code>h × w</code> consisting of empty cells <code>'.'</code> and blocked cells <code>'#'</code>.</p>

<p>A domino occupies exactly two adjacent cells (either horizontally or vertically), and both must be empty.</p>

<p>You are given <code>q</code> queries. Each query specifies a rectangle in the grid. For each query, determine the number of ways to place a domino completely inside the rectangle.</p>

---

### Example

<pre>
Input:
5 8
....#..#
.#......
##.#....
##..#.##
........
4
1 1 2 3
4 1 4 1
1 2 4 5
2 5 5 8

Output:
4
0
10
15
</pre>

---

### Constraints

<ul>
<li>1 ≤ h, w ≤ 500</li>
<li>1 ≤ q ≤ 100000</li>
<li>Grid contains only '.' and '#'</li>
</ul>

---

# Solution

### Approach (2D Prefix Sum)

Brute force per query is too slow because <code>q</code> is large. :contentReference[oaicite:0]{index=0}  

We preprocess the grid.

Key idea:
- Count all valid **horizontal pairs** and **vertical pairs**.

Steps:

1. Create two grids:
   - <code>hor[i][j]</code> = 1 if <code>(i,j)</code> and <code>(i,j+1)</code> are both '.'
   - <code>ver[i][j]</code> = 1 if <code>(i,j)</code> and <code>(i+1,j)</code> are both '.'

2. Build 2D prefix sums for both grids.

3. For each query rectangle:
   - Count horizontal dominoes inside it
   - Count vertical dominoes inside it
   - Add both

Important:
- Horizontal pairs must stay inside rectangle → adjust right boundary
- Vertical pairs must stay inside rectangle → adjust bottom boundary

---

### Complexity

- <strong>Preprocessing:</strong> O(h × w)  
- <strong>Each Query:</strong> O(1)  
- <strong>Total:</strong> O(h × w + q)

---

### Tags

prefix sum, 2d prefix sum, dp, implementation