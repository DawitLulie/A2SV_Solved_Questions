<h2><a href="https://codeforces.com/problemset/problem/1154/A">1154A. Restoring Three Numbers</a></h2>
<img src='https://img.shields.io/badge/Difficulty-800-brightgreen' alt='Difficulty: 800' />
<hr>

<p>You are given four integers which are the results of the sums of three positive integers <code>a</code>, <code>b</code>, and <code>c</code>:</p>

<ul>
<li><code>a + b</code></li>
<li><code>a + c</code></li>
<li><code>b + c</code></li>
<li><code>a + b + c</code></li>
</ul>

<p>Your task is to restore the original three numbers <code>a</code>, <code>b</code>, and <code>c</code>.</p>

---

### Example

<pre>
Input:
2 3 4 9

Output:
7 6 5
</pre>

---

### Constraints

<ul>
<li>All given numbers are positive integers</li>
<li>There exists a valid solution</li>
</ul>

---

# Solution

### Approach (Math)

Key observation:

- The largest number among the four is always:
  <code>a + b + c</code> :contentReference[oaicite:0]{index=0}

Steps:

1. Sort the 4 numbers.
2. Let the largest number be <code>total = a + b + c</code>.
3. Then:
   - <code>a = total - (b + c)</code>
   - <code>b = total - (a + c)</code>
   - <code>c = total - (a + b)</code>
4. In practice:
   - Subtract each of the first three numbers from the largest.

---

### Complexity

- <strong>Time Complexity:</strong> O(1)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

math, implementation