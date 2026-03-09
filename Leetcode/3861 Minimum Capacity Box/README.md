<h2><a href="https://leetcode.com/problems/minimum-capacity-box">3861. Minimum Capacity Box</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>You are given an integer array <code>capacity</code>, where <code>capacity[i]</code> represents the capacity of the <code>i<sup>th</sup></code> box, and an integer <code>itemSize</code> representing the size of an item.</p>

<p>The <code>i<sup>th</sup></code> box can store the item if:</p>

<pre>
capacity[i] >= itemSize
</pre>

<p>Return the <strong>index of the box</strong> with the <strong>minimum capacity</strong> that can store the item.</p>

<p>If multiple boxes have the same minimum valid capacity, return the <strong>smallest index</strong>.</p>

<p>If no box can store the item, return <code>-1</code>.</p>

---

### Example 1

<pre>
Input: capacity = [3,5,2,6], itemSize = 4
Output: 1

Explanation:
Boxes with enough capacity are:
index 1 → 5
index 3 → 6

The minimum valid capacity is 5 at index 1.
</pre>

### Example 2

<pre>
Input: capacity = [1,2,3], itemSize = 5
Output: -1

Explanation:
No box has capacity ≥ 5.
</pre>

---

### Constraints

<ul>
<li>1 ≤ capacity.length ≤ 10⁵</li>
<li>1 ≤ capacity[i], itemSize ≤ 10⁹</li>
</ul>

---

### Solution

**Approach (Single Pass / Linear Scan):**

We iterate through the array once while tracking the best valid box.

Steps:

1. Initialize `ans = -1`.
2. Traverse the array:
   - If `capacity[i] >= itemSize`, the box can hold the item.
   - Update `ans` if:
     - `ans == -1`, or
     - `capacity[i] < capacity[ans]`.
3. Return `ans`.

This ensures we always keep the index of the **smallest capacity box that fits the item**. :contentReference[oaicite:0]{index=0}

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

Where `n` is the number of boxes.

---

### Tags

array, simulation