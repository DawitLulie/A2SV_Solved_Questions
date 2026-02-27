<h2><a href="https://codeforces.com/problemset/problem/1690/D">1690D. Black and White Stripe</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1400-orange' alt='Difficulty: 1400' />
<hr>

<p>You are given a binary string <code>s</code> consisting of characters <code>'B'</code> and <code>'W'</code>.  
You want to make the string **alternating** (i.e., no two adjacent characters are the same).</p>

<p>In one move, you can choose an index <code>i</code> (1 ≤ i ≤ n) and flip <code>s[i]</code> ('B' → 'W' or 'W' → 'B').</p>

<p>Find the minimum number of moves required to make the string alternating.</p>

---

### Input

- First line contains a single integer <code>t</code> — number of test cases.  
- Each test case contains:
  - <code>n</code> — length of the string.
  - Binary string <code>s</code> of length <code>n</code>.

Constraints:
<ul>
<li>1 ≤ t ≤ 1000</li>
<li>1 ≤ n ≤ 10⁵</li>
<li>The total length of all strings does not exceed 10⁵</li>
</ul>

---

### Output

- For each test case, print the **minimum number of flips** needed to make <code>s</code> alternating.

---

### Example

```
Input
3
5
BBWBW
3
WWW
4
BWBB

Output
1
1
1
```

---

### Approach (Two Patterns)

An alternating string must follow one of two patterns:

1. `B W B W B W ...`  
2. `W B W B W B ...`

For each test case:

1. Compute mismatches if we force the string to follow pattern 1:
   - At even indices, expect `'B'`.  
   - At odd indices, expect `'W'`.  
   - Count how many positions differ.
2. Compute mismatches for pattern 2:
   - Even indices → `'W'`, odd → `'B'`.
3. The answer is `min(mismatches_pattern1, mismatches_pattern2)`.

---

### Complexity

- **Time:** O(n) — one pass per test case  
- **Space:** O(1) extra
