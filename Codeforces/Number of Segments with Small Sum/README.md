<h2>C. Number of Segments with Small Sum</h2>
<img src='https://img.shields.io/badge/Difficulty-1400-orange' alt='Difficulty: 1400' />
<hr>

<p>Given an array of <code>n</code> integers <code>a[i]</code>. A segment <code>a[l..r]</code> (1 ≤ l ≤ r ≤ n) is called <strong>good</strong> if the sum of its elements is at most <code>s</code>.</p>

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
19
</pre>

---

### Approach (Two Pointers / Sliding Window)

1. Maintain a sliding window [left, right] representing the current segment.
2. Keep track of the sum of the window.
3. Expand the window to the right while sum ≤ s.
4. When sum exceeds s, move left pointer to reduce sum.
5. For each right index, the number of new good segments ending at right is (right - left + 1).
6. Accumulate this count for the answer.

---

### Complexity

- Time: O(n) — each element is processed at most twice  
- Space: O(1)