<h2><a href="https://leetcode.com/problems/merge-adjacent-equal-elements">3834. Merge Adjacent Equal Elements</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given an integer array <code>nums</code>. You can perform the following operation any number of times:</p>

<ul>
<li>If two <strong>adjacent elements</strong> are equal, merge them into one element with value <code>2 × value</code>.</li>
</ul>

<p>Return the final array after applying all possible operations.</p>

<p><strong>Note:</strong> Always process from left to right.</p>

---

### Example 1

<pre>
Input: nums = [2,2,4,4]
Output: [4,8]
Explanation:
- Merge first two 2's → [4,4,4]
- Merge next two 4's → [4,8]
</pre>

### Example 2

<pre>
Input: nums = [2,2,2,2]
Output: [4,4]
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 2000</li>
<li>1 ≤ nums[i] ≤ 10⁹</li>
</ul>

---

# Solution

### Approach (Simulation)

We simulate the merging process from left to right.

Key idea:
- If two adjacent elements are equal, merge them into double and skip the next element.

Steps:

1. Initialize an empty result array.
2. Traverse the array with index <code>i</code>.
3. If <code>nums[i] == nums[i + 1]</code>:
   - Append <code>2 * nums[i]</code>
   - Skip the next element (<code>i += 2</code>)
4. Otherwise:
   - Append <code>nums[i]</code>
   - Move one step (<code>i += 1</code>)
5. Continue until the end.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(n)

---

### Tags

simulation, array