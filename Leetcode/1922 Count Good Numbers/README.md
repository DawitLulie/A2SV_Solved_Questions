<h2><a href="https://leetcode.com/problems/count-good-numbers">1922. Count Good Numbers</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>A digit string is considered <strong>good</strong> if:</p>

<ul>
<li>Digits at <strong>even indices</strong> (0-based) are even digits: <code>0,2,4,6,8</code>.</li>
<li>Digits at <strong>odd indices</strong> are prime digits: <code>2,3,5,7</code>.</li>
</ul>

<p>Given an integer <code>n</code>, return the total number of good digit strings of length <code>n</code>. Since the answer may be very large, return it modulo <code>10^9 + 7</code>.</p>

---

### Example 1

<pre>
Input: n = 1
Output: 5
Explanation: Only even indices exist → choices = [0,2,4,6,8]
</pre>

### Example 2

<pre>
Input: n = 4
Output: 400
</pre>

---

### Constraints

<ul>
<li>1 ≤ n ≤ 10<sup>15</sup></li>
</ul>

---

# Solution

### Approach (Math + Fast Power)

Key idea:

- Even indices → 5 choices (0,2,4,6,8)
- Odd indices → 4 choices (2,3,5,7)

Let:
- even positions = ⌈n / 2⌉
- odd positions = ⌊n / 2⌋

Total good numbers:

<code>(5 ^ even_positions) * (4 ^ odd_positions)</code>

Since <code>n</code> is large, use fast exponentiation (binary exponentiation).

---

### Complexity

- <strong>Time Complexity:</strong> O(log n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

math, fast exponentiation, modular arithmetic