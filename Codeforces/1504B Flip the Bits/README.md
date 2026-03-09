<h2><a href="https://codeforces.com/problemset/problem/1504/B">1504B. Flip the Bits</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1200-yellow' alt='Difficulty: 1200' />
<hr>

<p>You are given a binary string <code>a</code> of length <code>n</code>. In one operation, you can select any prefix of <code>a</code> with an equal number of <code>0</code> and <code>1</code> symbols. Then all symbols in the prefix are inverted: each <code>0</code> becomes <code>1</code> and each <code>1</code> becomes <code>0</code>.</p>

<p>For example, suppose <code>a = 0111010000</code>.</p>

<ul>
<li>Select the prefix of length 8 (four 0s and four 1s):  
<pre>[01110100]00 → [10001011]00</pre></li>

<li>Select the prefix of length 2:  
<pre>[10]00101100 → [01]00101100</pre></li>
</ul>

<p>It is illegal to select a prefix where the number of <code>0</code>s and <code>1</code>s are not equal.</p>

<p>Given another binary string <code>b</code> of the same length, determine whether it is possible to transform <code>a</code> into <code>b</code> using some number of operations. :contentReference[oaicite:0]{index=0}</p>

---

### Input

<ul>
<li>The first line contains an integer <code>t</code> — number of test cases.</li>
<li>For each test case:</li>
<ul>
<li>An integer <code>n</code> — length of the strings.</li>
<li>A binary string <code>a</code>.</li>
<li>A binary string <code>b</code>.</li>
</ul>
</ul>

---

### Output

<p>For each test case, print <code>YES</code> if it is possible to transform <code>a</code> into <code>b</code>, otherwise print <code>NO</code>.</p>

---

### Example

<pre>
Input
5
10
0111010000
0100101100
4
0000
0000
3
001
000
12
010101010101
100110011010
6
000111
110100

Output
YES
YES
NO
YES
NO
</pre>

---

### Constraints

<ul>
<li>1 ≤ t ≤ 10⁴</li>
<li>1 ≤ n ≤ 3 × 10⁵</li>
<li>The sum of n over all test cases ≤ 3 × 10⁵</li>
</ul>

---

### Solution

**Approach (Prefix Balance + Greedy):**

Key observation:

A prefix can be flipped only if the number of <code>0</code>s equals the number of <code>1</code>s.  
So we track such prefixes first.

Steps:

1. Traverse string <code>a</code> and count zeros and ones.
2. Whenever <code>zeros == ones</code>, mark that prefix as valid for flipping.
3. Process the strings from **right to left**.
4. Maintain a flag indicating whether the prefix has been flipped.
5. If current characters don't match the target:
   - We must flip the prefix ending at that index.
   - This is only possible if the prefix is balanced.
6. If not balanced → transformation is impossible.

---

### Complexity

- **Time:** O(n) per test case  
- **Space:** O(1)

---

### Tags

greedy, constructive algorithms, implementation, math
