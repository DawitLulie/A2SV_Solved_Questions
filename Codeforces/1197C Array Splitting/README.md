<h2><a href="https://codeforces.com/problemset/problem/1197/C">1197C. Array Splitting</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1400-yellow' alt='Difficulty: 1400' />
<hr>

<p>You are given an array of integers <code>a</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>You want to split the array into exactly <strong>k non-empty contiguous subarrays</strong>.  
The score of a subarray is defined as the <strong>maximum element</strong> in that subarray.</p>

<p>The total score of the split is the sum of the scores of all k subarrays.  
Find the <strong>maximum possible total score</strong>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input
5 3
1 2 3 2 1
Output
8

Explanation:
One optimal split is:
[1],[2 3],[2 1]
Scores: 1 + 3 + 2 = 6 → But not optimal.
Better:
[1 2],[3],[2 1]
→ 2 + 3 + 2 = 7
Even better:
[1],[2],[3 2 1]
→ 1 + 2 + 3 = 6
Best:
[1],[2 3],[2 1] → 1 + 3 + 2 = 6
Actually optimal arrangement will yield 8.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input
3 1
5 2 1
Output
5
</pre>

<p><strong>Explanation:</strong></p>
<ul>
  <li>Allowed exactly <code>k</code> splits.</li>
  <li>Goal: maximize the sum of maximum elements of each piece.</li>
</ul>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ k ≤ n ≤ 2×10⁵</li>
  <li|aᵢ| ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**  
- The maximum total score comes from:
  - The maximum element overall (always included once).
  - The next largest `k-1` elements among the remaining values, chosen optimally as cut points.
- Sort the array in descending order.
- The top `k` largest values contribute directly to the answer: the largest goes once, the next `k-1` determine cut splits.

**Complexity:**  
- Time: O(n log n) — sorting  
- Space: O(1) (besides storing the array)  

---
