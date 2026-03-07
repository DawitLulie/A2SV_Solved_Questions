<h2><a href="https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks">2379. Minimum Recolors to Get K Consecutive Black Blocks</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given a string <code>blocks</code> consisting of characters <code>'B'</code> (black) and <code>'W'</code> (white), and an integer <code>k</code>.</p>

<p>Return the minimum number of white blocks you need to recolor to black so that there is at least one substring of length <code>k</code> consisting entirely of black blocks.</p>

---

### Example 1

<pre>
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
</pre>

### Example 2

<pre>
Input: blocks = "WBWBBBW", k = 2
Output: 0
</pre>

---

### Constraints

<ul>
  <li>1 ≤ k ≤ blocks.length ≤ 100</li>
  <li>blocks[i] is either 'W' or 'B'</li>
</ul>

---

### Solution

**Approach (Sliding Window):**

We can use a sliding window of size <code>k</code> to count white blocks in each substring:

1. Initialize a counter for white blocks in the first window of size <code>k</code>.
2. Slide the window to the right by one character each time:
   - Decrease count if the leaving character is white.
   - Increase count if the entering character is white.
3. Keep track of the minimum number of white blocks across all windows.

This minimum is the answer.

---

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

---

### Tags

string, sliding window