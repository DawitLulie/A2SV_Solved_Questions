<h2><a href="https://leetcode.com/problems/capacity-to-ship-packages-within-d-days">1011. Capacity To Ship Packages Within D Days</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an array <code>weights</code> where <code>weights[i]</code> is the weight of the <code>i-th</code> package. You are also given an integer <code>days</code>.</p>

<p>Each day, you load the ship with packages in the given order. The ship cannot carry more than its capacity.</p>

<p>Return the <strong>least weight capacity</strong> of the ship that will result in all packages being shipped within <code>days</code>.</p>

---

### Example 1

<pre>
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation:
A ship capacity of 15 allows shipping in 5 days:
[1,2,3,4,5]
[6,7]
[8]
[9]
[10]
</pre>

### Example 2

<pre>
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
</pre>

### Example 3

<pre>
Input: weights = [1,2,3,1,1], days = 4
Output: 3
</pre>

---

### Constraints

<ul>
<li>1 ≤ weights.length ≤ 5 * 10⁴</li>
<li>1 ≤ weights[i] ≤ 500</li>
<li>1 ≤ days ≤ weights.length</li>
</ul>

---

# Solution

### Approach (Binary Search on Answer)

Key idea:

We search for the minimum capacity using binary search.

- Minimum capacity = max(weights)
- Maximum capacity = sum(weights)

For a given capacity, we can check how many days are needed.

Steps:

1. Set:
   - <code>left = max(weights)</code>
   - <code>right = sum(weights)</code>
2. While <code>left < right</code>:
   - Compute <code>mid</code>
   - Simulate shipping:
     - Count how many days needed with capacity = mid
   - If days needed ≤ given days:
     - Try smaller capacity → <code>right = mid</code>
   - Else:
     - Increase capacity → <code>left = mid + 1</code>
3. Return <code>left</code>

---

### Complexity

- <strong>Time Complexity:</strong> O(n log sum(weights))  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

binary search, array, greedy