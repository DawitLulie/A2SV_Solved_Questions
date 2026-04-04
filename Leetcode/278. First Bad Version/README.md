<h2><a href="https://leetcode.com/problems/first-bad-version">278. First Bad Version</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Given <code>n</code> versions [1, 2, ..., n] and an API <code>isBadVersion(version)</code> which returns whether version is bad, find the first bad version. You should minimize the number of calls to the API.</p>

---

### Example 1

<pre>
Input: n = 5, bad = 4
Output: 4
Explanation:
Call isBadVersion(3) -> false
Call isBadVersion(4) -> true
Call isBadVersion(5) -> true
First bad version is 4
</pre>

### Example 2

<pre>
Input: n = 1, bad = 1
Output: 1
</pre>

---

### Constraints

<ul>
<li>1 ≤ n ≤ 2³¹ - 1</li>
<li>1 ≤ bad ≤ n</li>
</ul>

---

# Solution

### Approach (Binary Search)

Key idea:

Use binary search to efficiently find the first bad version while minimizing API calls.

Steps:

1. Initialize <code>left = 1</code>, <code>right = n</code>.
2. While <code>left < right</code>:
   - <code>mid = left + (right - left) // 2</code>
   - If <code>isBadVersion(mid)</code> is True:
     - The first bad version is ≤ mid → <code>right = mid</code>
   - Else:
     - The first bad version is > mid → <code>left = mid + 1</code>
3. Return <code>left</code>.

---

### Complexity

- <strong>Time Complexity:</strong> O(log n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

binary search, interactive