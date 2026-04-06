<h2><a href="https://leetcode.com/problems/h-index-ii">275. H-Index II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an array of integers <code>citations</code> where <code>citations[i]</code> is the number of citations a researcher received for their <code>i-th</code> paper and <code>citations</code> is sorted in ascending order, return the researcher's <strong>h-index</strong>.</p>

<p>The <strong>h-index</strong> is defined as the maximum value <code>h</code> such that the researcher has at least <code>h</code> papers with at least <code>h</code> citations each.</p>

<p>You must write an algorithm that runs in <strong>O(log n)</strong> time.</p>

---

### Example 1

<pre>
Input: citations = [0,1,3,5,6]
Output: 3
Explanation:
There are 3 papers with at least 3 citations.
</pre>

### Example 2

<pre>
Input: citations = [1,2,100]
Output: 2
</pre>

---

### Constraints

<ul>
<li>n == citations.length</li>
<li>1 ≤ n ≤ 10⁵</li>
<li>0 ≤ citations[i] ≤ 1000</li>
<li>citations is sorted in ascending order</li>
</ul>

---

# Solution

### Approach (Binary Search)

Key idea:

If we pick an index <code>mid</code>, then:
- Number of papers with ≥ citations[mid] is <code>n - mid</code>

We check:
citations[mid] >= n - mid


Steps:

1. Initialize <code>left = 0</code>, <code>right = n - 1</code>.
2. While <code>left ≤ right</code>:
   - Compute <code>mid</code>
   - If <code>citations[mid] ≥ n - mid</code>:
     - Try smaller index → <code>right = mid - 1</code>
   - Else:
     - Move right → <code>left = mid + 1</code>
3. Answer is <code>n - left</code>

---

### Complexity

- <strong>Time Complexity:</strong> O(log n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

binary search, array