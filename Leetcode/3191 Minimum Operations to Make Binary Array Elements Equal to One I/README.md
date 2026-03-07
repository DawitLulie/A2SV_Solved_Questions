<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i">3191. Minimum Operations to Make Binary Array Elements Equal to One I</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a binary array <code>nums</code>.</p>

<p>You can perform the following operation any number of times:</p>

<ul>
<li>Choose an index <code>i</code> such that <code>i + 2 &lt; nums.length</code>.</li>
<li>Flip the values of <code>nums[i]</code>, <code>nums[i + 1]</code>, and <code>nums[i + 2]</code>.</li>
</ul>

<p>Flipping means:</p>

<ul>
<li><code>0</code> becomes <code>1</code></li>
<li><code>1</code> becomes <code>0</code></li>
</ul>

<p>Return the <strong>minimum number of operations</strong> required to make all elements of <code>nums</code> equal to <code>1</code>.  
If it is not possible, return <code>-1</code>.</p>

---

### Example 1

<pre>
Input: nums = [0,1,1,1,0,0]
Output: 3
</pre>

### Example 2

<pre>
Input: nums = [0,1,1,1]
Output: -1
</pre>

---

### Constraints

<ul>
<li>3 ≤ nums.length ≤ 10⁵</li>
<li><code>nums[i]</code> is either <code>0</code> or <code>1</code></li>
</ul>

---

### Solution

**Approach (Greedy Traversal):**

We process the array from left to right.

Key idea:

If we encounter a <code>0</code> at index <code>i</code>, the only way to fix it is to flip the subarray starting at <code>i</code>:

<pre>
flip(nums[i], nums[i+1], nums[i+2])
</pre>

Steps:

1. Traverse the array from <code>0</code> to <code>n - 3</code>.
2. If <code>nums[i] == 0</code>, perform a flip operation on the next three elements.
3. Increment the operation counter.
4. After processing, check the last two elements.
5. If any of them is <code>0</code>, return <code>-1</code>.

This greedy strategy works because once we move past an index, we can no longer change it.

---

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

---

### Tags

array, greedy, simulation