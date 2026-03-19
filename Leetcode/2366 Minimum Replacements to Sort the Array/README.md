<h2><a href="https://leetcode.com/problems/minimum-replacements-to-sort-the-array">2366. Minimum Replacements to Sort the Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. In one operation you can replace any element of the array with <strong>any two elements that sum to it</strong>.</p>

<p>Return the <strong>minimum number of operations</strong> to make the array <strong>non-decreasing</strong>.</p>

---

### Example 1

<pre>
Input: nums = [3,9,3]
Output: 2
Explanation:
Split 9 → [3,3,3]
Now array becomes [3,3,3,3]
Total operations = 2
</pre>

### Example 2

<pre>
Input: nums = [1,2,3,4,5]
Output: 0
Explanation:
Already non-decreasing.
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁵</li>
<li>1 ≤ nums[i] ≤ 10⁹</li>
</ul>

---

# Solution

### Approach (Greedy from Right to Left)

Key idea:

We process from right to left and ensure that each element is ≤ the next element.

Let:
- <code>prev</code> = the maximum allowed value for current position

Steps:

1. Start from the last element:
   - Set <code>prev = nums[n-1]</code>
2. Traverse from right to left:
   - If <code>nums[i] ≤ prev</code>:
     - No operation needed
     - Update <code>prev = nums[i]</code>
   - Else:
     - We need to split <code>nums[i]</code>
     - Divide it into <code>k</code> parts such that each part ≤ <code>prev</code>
     - Minimum <code>k = ceil(nums[i] / prev)</code>
     - Add <code>k - 1</code> to operations
     - Update <code>prev = nums[i] // k</code>

This greedy approach ensures minimal splits.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

### Tags

greedy, math, array