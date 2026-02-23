<h2><a href="https://codeforces.com/problemset/problem/2121/D">2121D. 1709</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1300-yellow' alt='Difficulty: 1300' />
<hr>

<p>You are given two arrays of integers <code>a</code> and <code>b</code> of length <code>n</code>. Each integer from <code>1</code> to <code>2·n</code> appears exactly once in either array.</p>

<p>Your task is to perform a sequence of operations (possibly zero) so that both of the following conditions are satisfied:</p>
<ul>
  <li>For each <code>1 ≤ i &lt; n</code>, <code>a[i] &lt; a[i+1]</code> and <code>b[i] &lt; b[i+1]</code>.</li>
  <li>For each <code>1 ≤ i ≤ n</code>, <code>a[i] &lt; b[i]</code>.</li>
</ul>

<p>During each operation, you can perform exactly one of the following:</p>
<ol>
  <li>Swap <code>a[i]</code> and <code>a[i+1]</code> for <code>1 ≤ i &lt; n</code>.</li>
  <li>Swap <code>b[i]</code> and <code>b[i+1]</code> for <code>1 ≤ i &lt; n</code>.</li>
  <li>Swap <code>a[i]</code> and <code>b[i]</code> for <code>1 ≤ i ≤ n</code>.</li>
</ol>

<p>You do not need to minimize operations, but the total number must not exceed 1709. A solution always exists.</p>

<p><strong>Input:</strong></p>
<ul>
  <li>First line: integer <code>t</code> — number of test cases.</li>
  <li>For each test case:
    <ul>
      <li>Line 1: integer <code>n</code>.</li>
      <li>Line 2: n integers <code>a[1..n]</code>.</li>
      <li>Line 3: n integers <code>b[1..n]</code>.</li>
    </ul>
  </li>
</ul>

<p><strong>Output:</strong></p>
<ul>
  <li>For each test case, first line: number of operations <code>k</code> (0 ≤ k ≤ 1709).</li>
  <li>Next <code>k</code> lines: operations
    <ul>
      <li><code>1 i</code> — swap <code>a[i]</code> and <code>a[i+1]</code></li>
      <li><code>2 i</code> — swap <code>b[i]</code> and <code>b[i+1]</code></li>
      <li><code>3 i</code> — swap <code>a[i]</code> and <code>b[i]</code></li>
    </ul>
  </li>
</ul>

<p><strong>Example:</strong></p>
<pre>
Input:
6
1
1
2
1
2
1
2
1 3
4 2
2
1 4
3 2
3
6 5 4
3 2 1
3
5 3 4
2 6 1

Output:
0
1
3 1
1
2 1
1
3 2
9
3 1
3 2
3 3
1 1
2 1
2 2
1 2
1 1
2 1
6
2 2
1 1
1 2
2 1
3 1
3 2
</pre>

---

###  Solution

**Approach:**
- Iterate through arrays to ensure <code>a[i] &lt; b[i]</code> by swapping positions if needed.
- Use adjacent swaps within <code>a</code> and <code>b</code> to make arrays strictly increasing.
- Since <code>n ≤ 40</code>, a bubble-sort–style constructive solution works.
- Total operations ≤ 1709.

**Complexity:**
- Time: O(n²) per test case  
- Space: O(n)  

---