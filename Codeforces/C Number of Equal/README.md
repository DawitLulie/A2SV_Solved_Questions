<h2>C. Number of Equal</h2>
<img src='https://img.shields.io/badge/Difficulty-1200-orange' alt='Difficulty: 1200' />
<hr>

<p>You are given two arrays <code>a</code> and <code>b</code>, sorted in non-decreasing order.</p>

<p>Find the number of pairs <code>(i, j)</code> such that:</p>

<pre>
a[i] = b[j]
</pre>

---

### 🔹 Input

- First line: two integers <code>n</code> and <code>m</code>  
  (1 ≤ n, m ≤ 10⁵)
- Second line: <code>n</code> integers <code>a[i]</code>
- Third line: <code>m</code> integers <code>b[i]</code>

Values satisfy:

- −10⁹ ≤ a[i], b[i] ≤ 10⁹

---

### 🔹 Output

Print one integer — the number of valid pairs.

---

### 🔹 Example

<pre>
Input:
8 7
1 1 3 3 3 5 8 8
1 3 3 4 5 5 5

Output:
11
</pre>

---

###  Approach (Two Pointers)

Since both arrays are sorted:

1. Use two pointers `i` and `j`.
2. If `a[i] < b[j]` → move `i`.
3. If `a[i] > b[j]` → move `j`.
4. If equal:
   - Count how many equal elements appear consecutively in `a`.
   - Count how many equal elements appear consecutively in `b`.
   - Add `(countA × countB)` to answer.
   - Move both pointers forward.

This works because equal values are grouped together in sorted arrays.

---

###  Why This Works

- Sorting ensures duplicates are consecutive.
- We count all combinations at once instead of checking individually.
- Each element is processed once.

---

### ⏱ Complexity

- Time: O(n)
- Space: O(1)

---