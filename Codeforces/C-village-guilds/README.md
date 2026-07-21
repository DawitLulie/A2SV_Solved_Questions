<h2><a href="https://codeforces.com/problemset/problem/1920/C">C. Village Guilds</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
You are given a rooted tree with <code>n</code> vertices, rooted at vertex <code>1</code>.
</p>

<p>
For every vertex <code>v</code> and every non-negative integer <code>h</code>, consider the set of vertices that:
</p>

<ul>
<li>belong to the subtree of <code>v</code></li>
<li>have distance exactly <code>h</code> from <code>v</code></li>
</ul>

<p>
This set is called a <b>guild</b>.
</p>

<p>
Two guilds are considered different if they contain different sets of vertices.
</p>

<p>
Find the number of different non-empty guilds in the tree.
</p>

---

### Example 1

<pre>
Input:
5
5
1 2 3 4

Output:
5
</pre>

<p>
For a chain tree, every guild contains only one vertex, so there are exactly 5 different guilds.
</p>

---

### Example 2

<pre>
Input:
3
3
1 1

Output:
4
</pre>

<p>
The tree:

1
├── 2
└── 3

Guilds:
<ul>
<li>{1}</li>
<li>{2}</li>
<li>{3}</li>
<li>{2,3}</li>
</ul>
</p>

---

### Constraints

<ul>
<li>1 ≤ t ≤ 10<sup>4</sup></li>
<li>2 ≤ n ≤ 2 · 10<sup>5</sup></li>
<li>1 ≤ p<sub>i</sub> &lt; i</li>
<li>The sum of n over all test cases does not exceed 2 · 10<sup>5</sup></li>
</ul>

---

### Solution

**Approach (Tree DFS + Hashing):**

A guild is determined by:

<ul>
<li>a starting vertex <code>v</code></li>
<li>a distance <code>h</code></li>
<li>the set of descendants of <code>v</code> at that distance</li>
</ul>

<p>
We need to count unique sets of vertices, not just the number of pairs <code>(v,h)</code>.
</p>

<p>
During DFS, we calculate information about every subtree.
For every vertex, we store the groups of descendants by their depth relative to that vertex.
</p>

<p>
The main idea is to represent every guild using a unique hash value.
If two guilds contain exactly the same vertices, their hashes will be equal.
</p>

Steps:

<ol>
<li>Build the rooted tree using the given parent array.</li>

<li>Run DFS from the root.</li>

<li>For every vertex, collect descendants according to their distance from that vertex.</li>

<li>Create a hash for each non-empty distance group.</li>

<li>Insert hashes into a global set to count only distinct guilds.</li>
</ol>

---

### Complexity

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

Where <code>n</code> is the number of vertices in the tree.

---

### Tags

tree, dfs, hashing, depth, sets