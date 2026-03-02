<h2><a href="https://leetcode.com/problems/product-of-array-except-self">238. Product of Array Except Self</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code>, return an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is guaranteed to fit in a 32-bit integer.</p>

<p>You must write an algorithm that runs in <strong>O(n)</strong> time and without using the division operation.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 ≤ nums.length ≤ 10⁵</li>
  <li>-30 ≤ nums[i] ≤ 30</li>
  <li>The product of any prefix or suffix fits in 32-bit integer.</li>
</ul>

---

### Solution

**Approach (Prefix & Suffix Products):**

- First pass: store prefix products.
- Second pass: multiply with suffix products.
- Do not use division.
- Reuse the output array to achieve O(1) extra space.

For each index:
answer[i] = (product before i) * (product after i)

---

### Complexity

- Time: O(n)
- Space: O(1) extra space (excluding output array)