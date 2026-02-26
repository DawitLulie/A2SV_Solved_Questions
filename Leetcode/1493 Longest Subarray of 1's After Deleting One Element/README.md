<h2><a href="https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element">1493. Longest Subarray of 1's After Deleting One Element</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a binary array <code>nums</code>, you should delete one element from it.</p>

<p>Return the size of the longest non-empty subarray containing only <code>1</code>s in the resulting array.</p>

<p>Return <code>0</code> if there is no such subarray.</p>

---

### 🔹 Example 1

<pre>
Input: nums = [1,1,0,1]
Output: 3
Explanation:
After deleting the 0, the longest subarray of 1's is [1,1,1].
</pre>

---

### 🔹 Example 2

<pre>
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
</pre>

---

### 🔹 Example 3

<pre>
Input: nums = [1,1,1]
Output: 2
Explanation:
You must delete one element.
</pre>

---

### 🔹 Constraints

<ul>
<li>1 ≤ nums.length ≤ 10⁵</li>
<li>nums[i] is either 0 or 1.</li>
</ul>

---

###  Approach (Sliding Window)

We want the longest subarray containing at most **one zero**.

Steps:

1. Use two pointers (left, right).
2. Expand the right pointer.
3. Keep count of zeros inside the window.
4. If zero count becomes greater than 1:
   - Move left pointer until zero count ≤ 1.
5. Track maximum window length.
6. Since we must delete one element, answer is:
   - <code>window_length - 1</code>

---

###  Why This Works

- Deleting one element means we can tolerate at most one zero.
- The sliding window ensures we always maintain a valid window.
- Subtract 1 because one element must be removed.

---

### ⏱ Complexity

- Time: O(n)
- Space: O(1)

---