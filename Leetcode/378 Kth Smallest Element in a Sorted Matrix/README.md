<h2><a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/">378. Kth Smallest Element in a Sorted Matrix</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />

<hr>

<h3>Problem Statement</h3>

<p>
You are given an <code>n x n</code> matrix where each row and each column is sorted in ascending order.
</p>

<p>
Return the <code>kth</code> smallest element in the matrix.
</p>

<p>
Note that it is the <b>kth smallest</b> element in sorted order, not the kth distinct element.
</p>

<hr>

<h3>Example 1:</h3>

<pre>
<b>Input:</b>
matrix = [
 [1,5,9],
 [10,11,13],
 [12,13,15]
]
k = 8

<b>Output:</b>
13
</pre>

<h3>Example 2:</h3>

<pre>
<b>Input:</b>
matrix = [[-5]]
k = 1

<b>Output:</b>
-5
</pre>

<hr>

<h3>Constraints:</h3>

<ul>
<li><code>n == matrix.length == matrix[i].length</code></li>
<li><code>1 ≤ n ≤ 300</code></li>
<li><code>-10⁹ ≤ matrix[i][j] ≤ 10⁹</code></li>
<li>Each row and column is sorted in non-decreasing order</li>
<li><code>1 ≤ k ≤ n²</code></li>
</ul>

<hr>

<h3>Approach (Max Heap)</h3>

<p>
We use a max heap of size <code>k</code>.
</p>

<p>
Traverse every element in the matrix:
</p>

<ul>
<li>Push the negative value into the heap</li>
<li>If heap size becomes larger than <code>k</code>, remove the largest element</li>
</ul>

<p>
At the end, the top of the heap will contain the kth smallest element.
</p>

<hr>

<h3>Step-by-Step</h3>

<ol>
<li>Create an empty heap</li>
<li>Loop through all matrix elements</li>
<li>Push negative values into heap</li>
<li>If heap size exceeds <code>k</code>, pop one element</li>
<li>Return the negative of the heap top</li>
</ol>

<hr>

<h3>Why Negative Values?</h3>

<p>
Python only provides a min heap.
</p>

<p>
To simulate a max heap,
we store negative values.
</p>

<hr>

<h3>Why This Works</h3>

<p>
The heap always stores the smallest <code>k</code> elements seen so far.
</p>

<p>
The largest among them is the kth smallest overall.
</p>

<hr>

<h3>⏱️ Time Complexity</h3>

<p>
<code>O(n² log k)</code>
</p>

<hr>

<h3>💾 Space Complexity</h3>

<p>
<code>O(k)</code>
</p>

<hr>

<h3>🏷️ Tags</h3>

<p>
Heap, Matrix
</p>