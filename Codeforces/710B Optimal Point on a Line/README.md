<h2><a href="https://codeforces.com/contest/710/problem/B">710B. Optimal Point on a Line</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1400-yellow' alt='Difficulty: 1400' />
<hr>

<p>You are given an integer <code>n</code> and <code>n</code> integers representing points on a number line.</p>

<p>Your task is to find a point <code>x</code> such that the sum of distances to all given points is minimized:</p>

<pre>
|x - a₁| + |x - a₂| + ... + |x - aₙ|
</pre>

<p>Print any such optimal <code>x</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input:
4
1 2 4 8

Output:
2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input:
3
-1 0 2

Output:
0
</pre>

<p><strong>Explanation:</strong></p>
<p>
The sum of absolute deviations is minimized when <code>x</code> is the <strong>median</strong> of the array.
</p>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ n ≤ 3 × 10⁵</li>
  <li>−10⁹ ≤ aᵢ ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**  
- Sort the array.  
- The optimal value that minimizes the sum of absolute differences is the <strong>median</strong>.  
- If <code>n</code> is odd → pick the middle element.  
- If <code>n</code> is even → any value between the two middle elements works (usually pick one of them).

This is a well-known mathematical property of absolute deviation.

**Complexity:**  
- Time: O(n log n) — sorting  
- Space: O(1) extra (ignoring input storage)

---
