<h2><a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array">153. Find Minimum in Rotated Sorted Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Suppose an array of length <code>n</code> sorted in ascending order is rotated between 1 and n times. For example, the array <code>nums = [0,1,2,4,5,6,7]</code> might become:</p>

<ul>
<li>[4,5,6,7,0,1,2]</li>
<li>[0,1,2,4,5,6,7]</li>
<li>[1,2,4,5,6,7,0]</li>
</ul>

<p>Given the rotated sorted array <code>nums</code> of unique elements, return <strong>the minimum element</strong> of this array.</p>

---

### Example 1

<pre>
Input: nums = [3,4,5,1,2]
Output: 1
</pre>

### Example 2

<pre>
Input: nums = [4,5,6,7,0,1,2]
Output: 0
</pre>

### Example 3

<pre>
Input: nums = [11,13,15,17]
Output: 11
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 5000</li>
<li>-5000 ≤ nums[i] ≤ 5000</li>
<li>All elements are unique.</li>
</ul>

---

# Solution

### Approach (Binary Search)

We can find the minimum using binary search:

1. Set <code>left = 0</code> and <code>right = len(nums) - 1</code>.
2. While <code>left < right</code>:
   - Compute <code>mid = (left + right) // 2</code>.
   - If <code>nums[mid] > nums[right]</code>, the minimum is in the right half: <code>left = mid + 1</code>.
   - Else, the minimum is in the left half (including mid): <code>right = mid</code>.
3. When <code>left == right</code>, <code>nums[left]</code> is the minimum.

**Why this works:**  
The rotated array is partially sorted. By comparing mid with right, we can determine which half contains the minimum.

---

### Complexity

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(1)

---

### Tags

binary search, array, rotated