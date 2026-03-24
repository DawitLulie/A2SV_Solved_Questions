<h2><a href="https://leetcode.com/problems/minimum-depth-of-binary-tree">111. Minimum Depth of Binary Tree</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a binary tree, find its <strong>minimum depth</strong>.</p>

<p>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong> A leaf is a node with no children.</p>

---

### Example 1

<pre>
Input: root = [3,9,20,null,null,15,7]
Output: 2
</pre>

### Example 2

<pre>
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
</pre>

---

### Constraints

<ul>
<li>The number of nodes in the tree is in the range [0, 10⁵]</li>
<li>-1000 ≤ Node.val ≤ 1000</li>
</ul>

---

# Solution

### Approach (BFS - Level Order Traversal)

Key idea:

The first time we reach a <strong>leaf node</strong> in BFS, we have found the minimum depth.

Steps:

1. Use a queue and start from the root with depth = 1.
2. Perform level-order traversal.
3. For each node:
   - If it is a leaf → return current depth.
   - Otherwise push its children with depth + 1.
4. BFS guarantees the shortest path.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(n)

---

### Tags

tree, bfs, binary tree