<h2><a href="https://leetcode.com/problems/maximum-candies-allocated-to-k-children">2226. Maximum Candies Allocated to K Children</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an integer array <code>candies</code>, where each element represents a pile of candies, and an integer <code>k</code> representing the number of children.</p>

<p>You can divide each pile into smaller piles, but you <strong>cannot combine</strong> piles.</p>

<p>Each child must receive the <strong>same number of candies</strong>. Return the <strong>maximum number of candies</strong> each child can get.</p>

---

### Example 1

<pre>
Input: candies = [5,8,6], k = 3
Output: 5
Explanation:
We can split piles to give each child 5 candies.
</pre>

### Example 2

<pre>
Input: candies = [2,5], k = 11
Output: 0
Explanation:
Not enough candies to give at least 1 candy to each child.
</pre>

---

### Constraints

<ul>
<li>1 ≤ candies.length ≤ 10<sup>5</sup></li>
<li>1 ≤ candies[i] ≤ 10<sup>7</sup></li>
<li>1 ≤ k ≤ 10<sup>12</sup></li>
</ul>

---

# Solution

### Approach (Binary Search on Answer)

We want to maximize the number of candies each child gets.

Instead of trying all possibilities, we use binary search on the answer.

1. Set the search range:
   - <code>left = 1</code>
   - <code>right = max(candies)</code>

2. For a given value <code>mid</code>, check if it is possible:
   - Count how many children can be served:
     <code>total = sum(candy // mid for candy in candies)</code>
   - If <code>total ≥ k</code>, then <code>mid</code> is valid.

3. Adjust search:
   - If valid → try larger value
   - Else → try smaller value

4. Track the maximum valid value.

**Why this works:**  
The answer is monotonic. If a value works, smaller values also work. If it fails, larger values will also fail. This allows binary search.

---

### Complexity

- **Time Complexity:** O(n log M)  
- **Space Complexity:** O(1)

---

### Tags

binary search, greedy