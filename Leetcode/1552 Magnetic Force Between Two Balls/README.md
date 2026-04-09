<h2><a href="https://leetcode.com/problems/magnetic-force-between-two-balls">1552. Magnetic Force Between Two Balls</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>In a basket, there are <code>n</code> positions where you can place balls. You are given an integer array <code>position</code> where <code>position[i]</code> is the location of the i-th basket.</p>

<p>You are also given an integer <code>m</code>, the number of balls you need to place.</p>

<p>You want to place the balls such that the <strong>minimum magnetic force</strong> between any two balls is maximized.</p>

<p>Return the <strong>largest minimum distance</strong> possible.</p>

---

### Example 1

<pre>
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation:
Place balls at positions 1, 4, and 7.
Minimum distance = 3
</pre>

### Example 2

<pre>
Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
</pre>

---

### Constraints

<ul>
<li>2 ≤ position.length ≤ 10<sup>5</sup></li>
<li>1 ≤ position[i] ≤ 10<sup>9</sup></li>
<li>All integers in <code>position</code> are distinct.</li>
<li>2 ≤ m ≤ position.length</li>
</ul>

---

# Solution

### Approach (Binary Search on Answer)

We want to maximize the minimum distance between any two balls.

1. Sort the positions.

2. Define search range:
   - <code>left = 1</code> (minimum possible distance)
   - <code>right = max(position) - min(position)</code>

3. Check if a distance <code>mid</code> is possible:
   - Place the first ball at the first position.
   - Greedily place the next ball at the next position where distance ≥ mid.
   - Count how many balls can be placed.
   - If count ≥ m → valid.

4. Binary search:
   - If valid → try larger distance
   - Else → try smaller distance

5. Track the maximum valid distance.

**Why this works:**  
If a distance works, smaller distances also work. If it fails, larger distances will also fail. This monotonic behavior allows binary search.

---

### Complexity

- **Time Complexity:** O(n log n + n log D)  
- **Space Complexity:** O(1)

Where D = max(position) - min(position)

---

### Tags

binary search, greedy, sorting