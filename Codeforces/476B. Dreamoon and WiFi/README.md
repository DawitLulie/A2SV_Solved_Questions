<h2><a href="https://codeforces.com/problemset/problem/476/B">476B. Dreamoon and WiFi</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1300-blue' alt='Difficulty: 1300' />
<hr>

<p>Dreamoon is standing at position 0 on a number line. He wants to reach a position given by string <code>s1</code>.</p>

<p>Each character in <code>s1</code> is either <code>'+'</code> (move +1) or <code>'-'</code> (move -1).</p>

<p>However, Dreamoon receives another string <code>s2</code> where some characters are unknown and represented by <code>'?'</code>.</p>

<p>Each <code>'?'</code> can independently be either <code>'+'</code> or <code>'-'</code> with equal probability.</p>

<p>Your task is to compute the probability that after replacing all <code>'?'</code> in <code>s2</code>, Dreamoon ends up at the same position as defined by <code>s1</code>.</p>

---

### Example

<pre>
Input:
++
+?

Output:
0.5
</pre>

---

# Solution

### Approach

1. Compute target position from <code>s1</code>.
2. Compute current position from <code>s2</code> ignoring <code>'?'</code>.
3. Count number of <code>'?'</code>.
4. Try all combinations of <code>'+'</code> and <code>'-'</code>.
5. Count valid ways that match target.
6. Probability = valid / total.

---

### Complexity

- <strong>Time Complexity:</strong> O(2^k)
- <strong>Space Complexity:</strong> O(1)

---

### Tags

math, brute force, probability