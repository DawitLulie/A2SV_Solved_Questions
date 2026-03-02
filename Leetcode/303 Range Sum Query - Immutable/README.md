<h2><a href="https://leetcode.com/problems/range-sum-query-immutable">303. Range Sum Query - Immutable</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code>, handle multiple queries of the following type:</p>

<p>Implement the <code>NumArray</code> class:</p>
<ul>
  <li><code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
  <li><code>int sumRange(int left, int right)</code> Returns the sum of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> inclusive (i.e., <code>nums[left] + nums[left + 1] + ... + nums[right]</code>).</li>
</ul>

<p><strong>Example 1:</strong></p>
<pre>
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 = (-2 + 0 + 3)
numArray.sumRange(2, 5); // return -1 = (3 + -5 + 2 + -1)
numArray.sumRange(0, 5); // return -3 = (-2 + 0 + 3 + -5 + 2 + -1)
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ nums.length ≤ 10⁴</li>
  <li>-10⁵ ≤ nums[i] ≤ 10⁵</li>
  <li>0 ≤ left ≤ right < nums.length</li>
  <li>At most 10⁴ calls will be made to <code>sumRange</code>.</li>
</ul>

---

### Solution

**Approach (Prefix Sum):**  
- Precompute a prefix sum array `prefix[i] = sum(nums[0]..nums[i-1])`.  
- For a query `sumRange(left, right)`, return `prefix[right + 1] - prefix[left]`.  
- This allows O(1) query time.  

**Complexity:**  
- Time: O(n) for preprocessing, O(1) per query  
- Space: O(1) for the prefix sum array  

---