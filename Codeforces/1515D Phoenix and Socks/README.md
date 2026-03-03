<h2><a href="https://codeforces.com/problemset/problem/1515/D">1515D. Phoenix and Socks</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1500-yellow' alt='Difficulty: 1500' />
<hr>

<p>Phoenix has brought his <strong>n socks</strong> (n is even). Each sock has a color and is either a left or right sock. He wants to make exactly <strong>n/2 matching pairs</strong>, where a matching pair consists of one left sock and one right sock of the same color.</p>

<p>He can pay <strong>1 coin</strong> to:</p>
<ul>
  <li>Recolor a sock to any color.</li>
  <li>Change a left sock into a right sock.</li>
  <li>Change a right sock into a left sock.</li>
</ul>

<p>Each sock must belong to exactly one pair. Determine the <strong>minimum cost</strong> required to form n/2 valid matching pairs.</p>

---

### Input

- First line contains integer <code>t</code> — number of test cases.
- For each test case:
  - Integers <code>n</code>, <code>l</code>, <code>r</code> where <code>l + r = n</code>.
  - Array of <code>n</code> integers representing colors.
  - First <code>l</code> are left socks.
  - Next <code>r</code> are right socks.

---

### Output

For each test case, print the minimum cost.

---

### Example

<pre>
Input
4
6 3 3
1 2 3 2 2 2
6 2 4
1 1 2 2 2 2
6 5 1
6 5 4 3 2 1
4 0 4
4 4 4 3

Output
2
3
5
3
</pre>

---

### Solution

**Greedy Strategy:**

1. First, match as many same-color left and right socks as possible for free.
2. If one side has more socks:
   - Use pairs of same-color socks on that side to flip efficiently.
   - Each flip reduces imbalance and helps form matches.
3. Finally, handle remaining unmatched socks:
   - Each remaining pair requires one recolor or flip.

The idea is to:
- Eliminate free matches first.
- Reduce imbalance efficiently.
- Minimize operations on leftover unmatched socks.

---

### Complexity

- Time: O(n) per test case
- Space: O(n) for counting colors

---

### Tags

greedy, implementation, counting