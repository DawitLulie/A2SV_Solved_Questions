<h2><a href="https://leetcode.com/problems/zero-array-transformation-i">3355. Zero Array Transformation I</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an integer array <code>nums</code> of length <code>n</code> and a 2D array <code>queries</code>, where 
<code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code>.</p>

<p>For each query, you can decrease every element in the subarray 
<code>nums[l<sub>i</sub>...r<sub>i</sub>]</code> by <strong>1</strong>.</p>

<p>Return <code>true</code> if it is possible to transform <code>nums</code> into an array consisting of only zeros after applying all queries in order. Otherwise, return <code>false</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,0,1], queries = [[0,2]]
Output: true
Explanation:
Apply the query once:
[1,0,1] → [0,-1,0]
All elements that needed to reach zero were covered.
</pre>

### Example 2

<pre>
Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]
Output: false
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁵</li>
<li>0 ≤ nums[i] ≤ 10⁵</li>
<li>1 ≤ queries.length ≤ 10⁵</li>
<li>0 ≤ l<sub>i</sub> ≤ r<sub>i</sub> &lt; nums.length</li>
</ul>

---

### Solution

**Approach (Difference Array + Prefix Sum):**

Each query decreases a whole range by <code>1</code>.  
Instead of applying every query directly, we use a **difference array** to track how many times each index is affected.

Steps:

1. Create a difference array <code>diff</code> of size <code>n + 1</code>.
2. For each query <code>[l, r]</code>:
   <pre>
diff[l] += 1
diff[r + 1] -= 1
</pre>
3. Compute the prefix sum to determine how many total decrements each index receives.
4. If the total decrements at index <code>i</code> are **less than <code>nums[i]</code>**, we cannot reduce it to zero → return <code>false</code>.
5. If all indices have enough operations to reach zero, return <code>true</code>.

---

### Complexity

- **Time:** O(n + q)  
- **Space:** O(n)

Where:
- <code>n</code> = length of the array  
- <code>q</code> = number of queries

---

### Tags

array, prefix sum, difference array