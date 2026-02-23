<h2><a href="https://leetcode.com/problems/container-with-most-water">11. Container With Most Water</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>height</code> of length <code>n</representing heights of vertical lines on the x-axis, find two lines that together with the x-axis form a container such that the container contains the most water. Return the maximum amount of water a container can store.</p>

<p><strong>Note:</strong> You may not slant the container.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The lines at index 1 and 8 form the container with area = min(8,7) * (8-1) = 49.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: height = [1,1]
Output: 1
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 ≤ height.length ≤ 10⁵</li>
  <li>0 ≤ height[i] ≤ 10⁴</li>
</ul>

---

###  Solution

**Approach (Two-pointer):**  
1. Initialize two pointers, `left` at 0 and `right` at n-1.  
2. Compute the area formed by `height[left]` and `height[right]`.  
3. Move the pointer pointing to the smaller height inward.  
4. Repeat until `left < right`, keeping track of the maximum area.

**Why this works:**  
The area is limited by the shorter line. Moving the taller line inward cannot increase area, so only move the smaller line.

**Complexity:**  
- Time: O(n) — each element visited at most once  
- Space: O(1)  

---