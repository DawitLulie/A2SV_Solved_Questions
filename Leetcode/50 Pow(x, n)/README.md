<h2><a href="https://leetcode.com/problems/powx-n">50. Pow(x, n)</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Implement <code>pow(x, n)</code>, which calculates <code>x</code> raised to the power <code>n</code> (i.e., <code>x^n</code>).</p>

---

### Example 1

<pre>
Input: x = 2.00000, n = 10
Output: 1024.00000
</pre>

### Example 2

<pre>
Input: x = 2.10000, n = 3
Output: 9.26100
</pre>

### Example 3

<pre>
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/(2^2) = 1/4 = 0.25
</pre>

---

### Constraints

<ul>
<li>-100.0 < x < 100.0</li>
<li>-2^31 <= n <= 2^31 - 1</li>
<li>-10^4 <= x^n <= 10^4</li>
</ul>

---

# Solution

### Approach (Fast Exponentiation / Recursion)

Key idea: Compute powers efficiently using recursion by splitting the exponent.

1. If <code>n == 0</code>, return 1.
2. For positive <code>n</code>:
   - Recursively compute <code>half = myPow(x, n // 2)</code>
   - If <code>n</code> is even, result = <code>half * half</code>
   - If <code>n</code> is odd, result = <code>half * half * x</code>
3. For negative <code>n</code>, return <code>1 / myPow(x, -n)</code>

This reduces the time complexity from O(n) to O(log n).

---

### Complexity

- **Time Complexity:** O(log n)  
- **Space Complexity:** O(log n) due to recursion stack

---

### Tags

math, recursion, divide and conquer
