<h2>E. Segments with Small Set</h2>
<img src='https://img.shields.io/badge/Difficulty-1400-orange' alt='Difficulty: 1400' />
<hr>

<p>Given an array of <code>n</code> integers <code>a[i]</code>. A segment <code>a[l..r]</code> (1 ≤ l ≤ r ≤ n) is called <strong>good</strong> if it contains at most <code>k</code> unique elements.</p>

<p>Find the number of different good segments.</p>

---

### Input

- First line: integers <code>n</code> and <code>k</code> (1 ≤ n ≤ 10⁵, 0 ≤ k ≤ n)  
- Second line: <code>n</code> integers <code>a[i]</code> (1 ≤ a[i] ≤ 10⁵)

---

### Output

- Print one integer — the number of good segments.

---

### Example

<pre>
Input:
7 3
2 6 4 3 6 8 3

Output:
20
</pre>

---

### Approach (Two Pointers / Sliding Window)

1. Maintain a sliding window [left, right].
2. Keep a count of unique elements in the current window using a dictionary.
3. Expand the window to the right:
   - Add the element at right to the dictionary.
   - If the number of unique elements exceeds k:
     - Move left forward until unique count ≤ k.
4. For each right, the number of new good segments ending at right is (right - left + 1).
5. Accumulate this count for the answer.

This approach works because expanding the window adds new segments, and shrinking ensures the unique element constraint.

---

### Complexity

- Time: O(n) — each element is processed at most twice  
- Space: O(n) — to store counts of elements