<h2><a href="https://leetcode.com/problems/pancake-sorting">969. Pancake Sorting</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of integers <code>arr</code>, sort the array using only the following operation:</p>

<p>Choose an integer <code>k</code> where <code>1 ≤ k ≤ arr.length</code>, then reverse the subarray <code>arr[0...k-1]</code>.</p>

<p>Return a sequence of <code>k</code> values corresponding to the pancake flips that sort the array.  
Any valid answer that sorts the array within <code>10 × n</code> flips will be accepted.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: arr = [3,2,4,1]
Output: [4,2,4,3]
Explanation:
Flip first 4 → [1,4,2,3]
Flip first 2 → [4,1,2,3]
Flip first 4 → [3,2,1,4]
Flip first 3 → [1,2,3,4]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: arr = [1,2,3]
Output: []
Explanation:
Array is already sorted.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ arr.length ≤ 100</li>
  <li>1 ≤ arr[i] ≤ n</li>
  <li>All integers in arr are unique.</li>
</ul>

---

###  Solution

**Approach (Greedy):**

We place the largest unsorted element at its correct position one by one.

Steps:
1. Start from the largest value `n` down to `1`.
2. Find the index of the current largest element.
3. If it is not already in correct position:
   - Flip it to the front (if needed).
   - Flip it to its correct position.
4. Repeat for the next largest.

Each number requires at most 2 flips, so total flips ≤ 2n.

**Why this works:**  
Reversing prefix segments allows us to move any element to any position using at most two operations.

**Complexity:**
- Time: O(n²) — searching + reversing  
- Space: O(1) extra (excluding output list)  

---