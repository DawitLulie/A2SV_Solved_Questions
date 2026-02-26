<h2>B. Most Socially-Distanced Subsequence</h2>
<img src='https://img.shields.io/badge/Difficulty-1100-green' alt='Difficulty: 1100' />
<hr>

<p>Given a permutation <code>p</code> of length <code>n</code>, find a subsequence of length at least 2 such that:</p>

<p><code>|s1 − s2| + |s2 − s3| + ... + |sk−1 − sk|</code> is maximized.</p>

<p>Among all such subsequences, choose one with the minimum possible length.</p>

---

### Key Observation

To maximize the total absolute difference between consecutive elements:

- We should keep only the “turning points” of the permutation.
- That means:
  - Always include the first element.
  - Always include the last element.
  - Include an element if it is a **local maximum or local minimum**.

Why?

Because if three consecutive elements are strictly increasing or strictly decreasing, the middle one does not increase the total absolute difference and can be removed.

So we:
- Traverse the permutation.
- Keep elements where the direction changes.

This guarantees:
- Maximum possible sum.
- Minimum possible subsequence length.

---

### Algorithm

For each test case:

1. Start result list with first element.
2. For each middle element:
   - If it is a local maxima or minima, keep it.
3. Always keep the last element.
4. Output the result.

---

### Complexity

- Time: O(n) per test case
- Space: O(n)