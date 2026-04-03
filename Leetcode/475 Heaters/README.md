<h2><a href="https://leetcode.com/problems/heaters">475. Heaters</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Winter is coming! Your task is to find the minimum radius of heaters so that all houses are covered.</p>

<p>You are given positions of <code>houses</code> and <code>heaters</code> on a horizontal line.</p>

<p>Each heater warms an area within a fixed radius. A house is covered if it lies within the radius of at least one heater.</p>

<p>Return the <strong>minimum radius</strong> needed so that all houses are covered.</p>

---

### Example 1

<pre>
Input: houses = [1,2,3], heaters = [2]
Output: 1
</pre>

### Example 2

<pre>
Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
</pre>

---

### Constraints

<ul>
<li>1 ≤ houses.length, heaters.length ≤ 3 * 10⁴</li>
<li>1 ≤ houses[i], heaters[i] ≤ 10⁹</li>
</ul>

---

# Solution

### Approach (Binary Search / Two Pointers)

Key idea:

For each house, find the **closest heater**, and take the maximum of these minimum distances.

Steps:

1. Sort both <code>houses</code> and <code>heaters</code>.
2. For each house:
   - Use binary search to find the nearest heater.
   - Compute distance to closest heater.
3. Track the maximum distance across all houses.

That maximum distance is the answer.

---

### Complexity

- <strong>Time Complexity:</strong> O(n log m)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

binary search, two pointers, sorting