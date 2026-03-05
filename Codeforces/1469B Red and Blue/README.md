<h2><a href="https://codeforces.com/contest/1469/problem/B">1469B. Red and Blue</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1200-yellow' alt='Difficulty: 1200' />
<hr>

<p>You are given an array of <strong>n colored balls</strong> — each is either <strong>red</strong> or <strong>blue</strong>. The red balls are represented by <code>R</code>, and the blue balls by <code>B</code>.</p>

<p>You can rearrange the balls by swapping adjacent pairs any number of times.</p>

<p>The <strong>badness</strong> of a sequence is defined as the number of positions <code>i</code> such that a blue ball comes before a red ball (<code>B before R</code>).</p>

<p>Your task: determine the <strong>minimum badness</strong> you can achieve after rearranging the balls optimally.</p>

---

### Example

<pre>
Input
1
5
BRBRB

Output
3
</pre>

---

### Constraints

<ul>
  <li>1 ≤ t ≤ 10⁴</li>
  <li>1 ≤ n ≤ 2 × 10⁵</li>
  <li>Total sum of all n across test cases ≤ 2 × 10⁵</li>
</ul>

---

### Solution

**Approach (Two Pointers / Greedy):**

To minimize badness (i.e., minimize the number of times a ‘B’ appears before an ‘R’), we should:

1. Pair each blue ball with a red ball from the opposite end so that as many Bs as possible are shifted to the right side.
2. Use two pointers:
   - One pointer <code>l</code> starting from the beginning to find B’s that need to move.
   - Another pointer <code>r</code> starting from the end to find R’s that can be swapped with those B’s.
3. For each valid pair (B at <code>l</code> and R at <code>r</code>), we can “swap” them in the final arrangement, reducing badness by 1.

Repeat until pointers cross.

This effectively pushes as many R’s as possible to the left and B’s to the right.

---

### Complexity

- **Time:** O(n) per test case  
- **Space:** O(1) extra

---

### Tags

two pointers, greedy, implementation