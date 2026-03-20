<h2><a href="https://leetcode.com/problems/same-tree">100. Same Tree</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given the roots of two binary trees <code>p</code> and <code>q</code>, write a function to check if they are the same or not.</p>

<p>Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.</p>

---

### Example 1

<pre>
Input: p = [1,2,3], q = [1,2,3]
Output: true
</pre>

### Example 2

<pre>
Input: p = [1,2], q = [1,null,2]
Output: false
</pre>

### Example 3

<pre>
Input: p = [1,2,1], q = [1,1,2]
Output: false
</pre>

---

### Constraints

<ul>
<li>The number of nodes in both trees is in the range [0, 100]</li>
<li>-10⁴ ≤ Node.val ≤ 10⁴</li>
</ul>

---

# Solution

### Approach (DFS / Recursion)

We compare both trees node by node.

Steps:

1. If both nodes are <code>None</code>, return <code>True</code>.
2. If one is <code>None</code> and the other is not, return <code>False</code>.
3. If values of nodes are different, return <code>False</code>.
4. Recursively check:
   - left subtree
   - right subtree

If all checks pass, the trees are identical.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(h)

---

### Tags

tree, dfs, recursion, binary tree