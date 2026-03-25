<h2><a href="https://codeforces.com/problemset/problem/913/B">913B. Christmas Spruce</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1000-brightgreen' alt='Difficulty: 1000' />
<hr>

<p>You are given a rooted tree with <code>n</code> vertices. The root is vertex <code>1</code>.</p>

<p>Each vertex except the root has exactly one parent.</p>

<p>A vertex is called <strong>internal</strong> if it has at least one child.</p>

<p>A tree is called a <strong>spruce</strong> if every internal vertex has at least <strong>three leaf children</strong>.</p>

<p>Determine whether the given tree is a spruce.</p>

---

### Example

<pre>
Input:
4
1 1 1

Output:
Yes
</pre>

---

### Constraints

<ul>
<li>3 ≤ n ≤ 1000</li>
<li>Each node (except root) has exactly one parent</li>
</ul>

---

# Solution

### Approach (Tree + Counting Leaves)

Key idea:

For every internal node, count how many of its children are leaves.

A leaf is a node with no children.

Steps:

1. Build the tree using adjacency list.
2. Identify leaf nodes (nodes with no children).
3. For each node:
   - If it has children (internal node):
     - Count how many of its children are leaves.
     - If fewer than 3 → answer is "No".
4. If all internal nodes satisfy the condition → "Yes".

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(n)

---

### Tags

tree, implementation, dfs