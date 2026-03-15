<h2><a href="https://leetcode.com/problems/two-out-of-three">2032. Two Out of Three</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given three integer arrays <code>nums1</code>, <code>nums2</code>, and <code>nums3</code>, return a <strong>distinct array</strong> containing all the values that appear in <strong>at least two</strong> out of the three arrays.</p>

<p>You may return the values in <strong>any order</strong>.</p>

---

### Example 1

<pre>
Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation:
- 3 appears in all three arrays.
- 2 appears in nums1 and nums2.
</pre>

### Example 2

<pre>
Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation:
Each number appears in at least two arrays.
</pre>

### Example 3

<pre>
Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation:
No number appears in at least two arrays.
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums1.length, nums2.length, nums3.length ≤ 100</li>
<li>1 ≤ nums1[i], nums2[i], nums3[i] ≤ 100</li>
</ul>

---

# Solution

### Approach (Set Intersection)

We use sets to remove duplicates from each array.

Key idea:
- Convert each array to a set.
- Find intersections between pairs of sets.
- Combine all results using set union.

Steps:

1. Convert <code>nums1</code>, <code>nums2</code>, and <code>nums3</code> to sets.
2. Find common elements:
   - <code>set1 ∩ set2</code>
   - <code>set1 ∩ set3</code>
   - <code>set2 ∩ set3</code>
3. Union all results to get elements appearing in at least two arrays.
4. Convert to list and return.

---

### Complexity

- <strong>Time Complexity:</strong> O(n + m + k)  
- <strong>Space Complexity:</strong> O(n + m + k)

---

### Tags

set, hash table, array