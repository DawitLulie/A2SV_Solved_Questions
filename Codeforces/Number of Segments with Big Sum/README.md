<h2>D. Number of Segments with Big Sum</h2>
<img src='https://img.shields.io/badge/Difficulty-1400-orange' alt='Difficulty: 1400' />
<hr>

<p>Given an array of <code>n</code> integers <code>a[i]</code>. A segment <code>a[l..r]</code> (1 ≤ l ≤ r ≤ n) is called <strong>good</strong> if the sum of its elements is at least <code>s</code>.</p>

<p>Find the total number of good segments.</p>

---

### Input

- First line: integers <code>n</code> and <code>s</code> (1 ≤ n ≤ 10⁵, 1 ≤ s ≤ 10¹⁸)  
- Second line: <code>n</code> integers <code>a[i]</code> (1 ≤ a[i] ≤ 10⁹)

---

### Output

- Print one integer — the number of good segments.

---

### Example

<pre>
Input:
7 20
2 6 4 3 6 8 9

Output:
9
</pre>

---

### Approach (Two Pointers / Sliding Window)

Since all <code>a[i] ≥ 1</code>, we can use a sliding window.

1. Maintain two pointers <code>left</code> and <code>right</code>.
2. Expand <code>right</code> and maintain current sum.
3. Whenever the sum becomes ≥ s:
   - All segments starting at <code>left</code> and ending at any index ≥ right are valid.
   - Add <code>(n - right)</code> to the answer.
   - Move <code>left</code> forward and reduce sum.
4. Continue until all segments are processed.

This works because the array contains only positive integers, so expanding increases sum and shrinking decreases it.

---

### Complexity

- Time: O(n) — each pointer moves at most n times  
- Space: O(1)