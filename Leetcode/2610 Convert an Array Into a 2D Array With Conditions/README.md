<h2><a href="https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions">2610. Convert an Array Into a 2D Array With Conditions</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an integer array <code>nums</code>. You need to create a <strong>2D array</strong> from <code>nums</code> satisfying the following conditions:</p>

<ul>
<li>The 2D array should contain only the elements of the array <code>nums</code>.</li>
<li>Each row in the 2D array should contain <strong>distinct integers</strong>.</li>
<li>The number of rows in the 2D array should be <strong>minimal</strong>.</li>
</ul>

<p>Return the resulting array. If there are multiple answers, return any of them.</p>

---

### Example 1

<pre>
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation:
Each row contains distinct integers.
The number 1 appears three times, so we need at least three rows.
</pre>

### Example 2

<pre>
Input: nums = [1,2,3,4]
Output: [[1,2,3,4]]
Explanation:
All numbers are distinct, so only one row is needed.
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 200</li>
<li>1 ≤ nums[i] ≤ nums.length</li>
</ul>

---

# Solution

### Approach (Greedy + Frequency Count)

The key observation:

- If a number appears <code>k</code> times, we need at least <code>k</code> rows because each row must contain distinct elements.

Steps:

1. Count the frequency of each number.
2. The maximum frequency determines the number of rows.
3. Create rows gradually.
4. For each number and its frequency, place the number in the first <code>freq</code> rows.

This ensures:
- Each row has distinct numbers.
- The number of rows is minimal.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)
- <strong>Space Complexity:</strong> O(n)

---

### Tags

greedy, hash table, array, simulation