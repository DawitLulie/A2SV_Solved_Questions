<h2><a href="https://codeforces.com/problemset/problem/2112/C">2112C. Coloring Game</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1300-yellow' alt='Difficulty: 1300' />
<hr>

<p>You are given a sorted array <code>a</code> of size <code>n</code>.</p>

<p>Alice chooses <code>3</code> elements and colors them red. Then Bob chooses one element and colors it blue (possibly recoloring a red one).</p>

<p>Alice wins if the sum of the red elements is strictly greater than the value of the blue element.</p>

<p>Your task is to count the number of ways Alice can choose <code>3</code> elements such that she wins regardless of Bob’s move.</p>

---

### Example

<pre>
Input:
5
7 7 7 7 7

Output:
10
</pre>

---

### Constraints

<ul>
<li>3 ≤ n ≤ 5000</li>
<li>Array is sorted</li>
<li>Sum of n over all test cases ≤ 5000</li>
</ul>

---

# Solution

### Approach (Greedy + Two Pointers)

Key observation:

Bob will choose the **maximum possible value** to try to beat Alice.

So for Alice to **always win**, we must ensure: