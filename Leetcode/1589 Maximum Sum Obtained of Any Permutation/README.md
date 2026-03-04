<h2><a href="https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation">1589. Maximum Sum Obtained of Any Permutation</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an array <code>nums</code> of length <code>n</code>. You are also given a 2D array <code>requests</code> where <code>requests[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>.</p>

<p>Each <code>requests[i]</code> represents a range from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> (inclusive).</p>

<p>You may permute <code>nums</code> in any order. Return the maximum total sum of all requests.</p>

<p>Since the answer may be too large, return it modulo <code>10⁹ + 7</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation:
One optimal permutation is [3,5,4,2,1].
The total sum is:
(5+4+2) + (3+5) = 11 + 8 = 19.
</pre>

### Example 2

<pre>
Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
</pre>

---

### Constraints

<ul>
  <li>n == nums.length</li>
  <li>1 ≤ n ≤ 10⁵</li>
  <li>0 ≤ nums[i] ≤ 10⁵</li>
  <li>1 ≤ requests.length ≤ 10⁵</li>
  <li>0 ≤ start<sub>i</sub> ≤ end<sub>i</sub> &lt; n</li>
</ul>

---

### Solution

**Approach (Difference Array + Greedy Sorting):**

1. Create a frequency array of size <code>n</code> initialized with 0.
2. For each request <code>[l, r]</code>:
   - Increment <code>freq[l]</code> by 1.
   - Decrement <code>freq[r + 1]</code> by 1 (if valid).
3. Compute prefix sum of <code>freq</code> to get how many times each index is requested.
4. Sort:
   - Sort <code>nums</code> in ascending order.
   - Sort <code>freq</code> in ascending order.
5. Multiply corresponding elements and sum up the result.
6. Return result modulo <code>10⁹ + 7</code>.

**Why this works:**

To maximize the total sum:
- Assign the largest numbers to the indices that appear in the most requests.
- This is a greedy strategy based on matching largest frequency with largest value.

---

### Complexity

- **Time:** O(n log n) — sorting dominates  
- **Space:** O(n)

---

### Tags

array, greedy, prefix sum, sorting