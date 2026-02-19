<h2><a href="https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values">2570. Merge Two 2D Arrays by Summing Values</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given two 2D integer arrays <code>nums1</code> and <code>nums2</code>.</p>

<p>Each element of the arrays is a pair <code>[id, value]</code>, where:</p>
<ul>
  <li><code>id</code> represents a unique identifier.</li>
  <li><code>value</code> represents the value associated with that <code>id</code>.</li>
</ul>

<p>Both input arrays are sorted in ascending order by <code>id</code>, and each <code>id</code> in a single array is unique.</p>

<p>Your task is to merge the two arrays into one array that:</p>
<ul>
  <li>Contains all unique <code>id</code>s from both arrays.</li>
  <li>Sums the values of matching <code>id</code>s from both arrays.</li>
  <li>Is sorted in ascending order by <code>id</code>.</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input:
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

Output:
[[1,6],[2,3],[3,2],[4,6]]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input:
nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]

Output:
[[1,3],[2,4],[3,6],[4,3],[5,5]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums1.length, nums2.length ≤ 200</li>
  <li>nums1[i].length == nums2[j].length == 2</li>
  <li>1 ≤ id, value ≤ 1000</li>
  <li>Each array contains unique ids.</li>
  <li>Both arrays are sorted in strictly ascending order by id.</li>
</ul>

---

### 🚀 Solution

**Approach:**  
- Use a hash map (or `Counter`) to sum values for each <code>id</code> across both arrays.  
- Iterate through both <code>nums1</code> and <code>nums2</code>, and accumulate the total for each <code>id</code>.  
- Sort the resulting pairs by <code>id</code> in ascending order and return.

**Complexity:**  
- Time: O(n + m + k log k), where n, m are input sizes and k is number of unique ids.  
- Space: O(k) additional for storing merged results.

---
