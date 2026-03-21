<h2><a href="https://leetcode.com/problems/count-elements-with-at-least-k-greater-values">3759. Count Elements With at Least K Greater Values</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>Return the number of elements in <code>nums</code> that have <strong>at least</strong> <code>k</code> elements strictly greater than them.</p>

---

### Example 1

<pre>
Input: nums = [3,1,4,2], k = 2
Output: 2
Explanation:
- 1 has 3 greater elements → valid
- 2 has 2 greater elements → valid
- 3 has 1 greater element → not valid
- 4 has 0 greater elements → not valid
</pre>

### Example 2

<pre>
Input: nums = [1,1,1], k = 1
Output: 0
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 1000</li>
<li>1 ≤ nums[i] ≤ 1000</li>
<li>0 ≤ k ≤ nums.length</li>
</ul>

---

# Solution

### Approach (Sorting)

Key idea:

If we sort the array, we can easily determine how many elements are greater than each element.

Steps:

1. Sort the array.
2. For each index <code>i</code>:
   - Number of elements greater = <code>n - i - 1</code>
3. Count how many elements satisfy:
   <code>n - i - 1 ≥ k</code>

---

### Complexity

- <strong>Time Complexity:</strong> O(n log n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

array, sorting