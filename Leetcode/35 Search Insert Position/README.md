<h2><a href="https://leetcode.com/problems/search-insert-position">35. Search Insert Position</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a sorted array of distinct integers and a target value, return the <strong>index</strong> if the target is found.</p>

<p>If not, return the index where it would be if it were inserted in order.</p>

<p>You must write an algorithm with <strong>O(log n)</strong> runtime complexity.</p>

---

### Example 1

<pre>
Input: nums = [1,3,5,6], target = 5
Output: 2
</pre>

### Example 2

<pre>
Input: nums = [1,3,5,6], target = 2
Output: 1
</pre>

### Example 3

<pre>
Input: nums = [1,3,5,6], target = 7
Output: 4
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁴</li>
<li>-10⁴ ≤ nums[i] ≤ 10⁴</li>
<li>nums contains <strong>distinct</strong> values sorted in ascending order</li>
<li>-10⁴ ≤ target ≤ 10⁴</li>
</ul>

---

# Solution

### Approach (Binary Search)

Key idea:

Since the array is sorted, we use binary search to find the correct position.

Steps:

1. Initialize <code>left = 0</code>, <code>right = n - 1</code>.
2. While <code>left ≤ right</code>:
   - Find <code>mid</code>.
   - If <code>nums[mid] == target</code>, return <code>mid</code>.
   - If <code>nums[mid] < target</code>, move <code>left = mid + 1</code>.
   - Else move <code>right = mid - 1</code>.
3. If not found, <code>left</code> will be the correct insert position.

---

### Complexity

- <strong>Time Complexity:</strong> O(log n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

binary search, array