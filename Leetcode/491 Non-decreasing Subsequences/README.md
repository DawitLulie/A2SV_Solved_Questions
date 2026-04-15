<h2><a href="https://leetcode.com/problems/non-decreasing-subsequences">491. Non-decreasing Subsequences</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, return all the different possible <strong>non-decreasing subsequences</strong> of the given array with at least two elements. You may return the answer in any order.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>A subsequence is <strong>non-decreasing</strong> if each element is greater than or equal to the previous one.</p>

---

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [4,6,7,7]
Output: [
 [4,6],
 [4,6,7],
 [4,6,7,7],
 [4,7],
 [4,7,7],
 [6,7],
 [6,7,7],
 [7,7]
]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
</pre>

---

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 15</li>
  <li>-100 &lt;= nums[i] &lt;= 100</li>
</ul>

---

<h3> Intuition</h3>

<p>
We need to find all subsequences (not necessarily contiguous) where the numbers are in non-decreasing order.
Also, each subsequence must have at least 2 elements.
</p>

<p>
The challenge is:
</p>
<ul>
  <li>Generating all possible subsequences</li>
  <li>Avoiding duplicates</li>
</ul>

<p>
This makes it a perfect problem for <strong>backtracking</strong>.
</p>

---

<h3> Approach (Backtracking + Set for Duplicates)</h3>

<p><strong>Step-by-step:</strong></p>

<ol>
  <li>Create a result set to automatically avoid duplicates.</li>
  <li>Use a recursive function <code>backtrack(start, path)</code>.</li>
  <li>If <code>path.length >= 2</code>, add it to result.</li>
  <li>Loop from <code>start</code> to end:
    <ul>
      <li>If <code>path</code> is empty OR current number ≥ last element in path:
        <ul>
          <li>Add the number to path.</li>
          <li>Call recursion with next index.</li>
          <li>Backtrack (remove last element).</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>

---

<h3> Handling Duplicates</h3>

<p>
Since the array may contain duplicate numbers, we may generate the same subsequence multiple times.
</p>

<p>
To fix this:
</p>
<ul>
  <li>Use a <strong>set</strong> to store results as tuples.</li>
  <li>This ensures only unique subsequences are kept.</li>
</ul>

---

<h3> Why Backtracking Works</h3>

<p>
Backtracking explores all possible subsequences.
At each step, we decide whether to include a number or not.
</p>

<p>
By checking the non-decreasing condition, we ensure only valid sequences are built.
</p>

---

<h3>⏱️ Complexity Analysis</h3>

<ul>
  <li><strong>Time Complexity:</strong> O(2<sup>n</sup>)  
    <br>Each element can either be included or excluded.</li>

  <li><strong>Space Complexity:</strong> O(2<sup>n</sup>)  
    <br>To store all possible subsequences.</li>
</ul>

---

<h3> Tags</h3>

<p>Backtracking, Recursion, DFS, Set</p>

---