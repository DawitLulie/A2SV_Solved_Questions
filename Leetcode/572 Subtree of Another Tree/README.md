<h2><a href="https://leetcode.com/problems/subtree-of-another-tree">572. Subtree of Another Tree</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values of <code>subRoot</code>, and <code>false</code> otherwise.</p>

<p>A subtree of a binary tree is a tree that consists of a node in <code>root</code> and all of this node's descendants.</p>

---

### Example 1

<pre>
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
</pre>

### Example 2

<pre>
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
</pre>

---

### Constraints

<ul>
<li>The number of nodes in the <code>root</code> tree is in the range [1, 2000]</li>
<li>The number of nodes in the <code>subRoot</code> tree is in the range [1, 1000]</li>
<li>-10⁴ ≤ Node.val ≤ 10⁴</li>
</ul>

---

# Solution

### Approach (DFS + Tree Comparison)

We check every node in <code>root</code> and try to match it with <code>subRoot</code>.

Steps:

1. Define a helper function <code>isSame(a, b)</code>:
   - If both are <code>None</code>, return <code>True</code>
   - If one is <code>None</code>, return <code>False</code>
   - If values differ, return <code>False</code>
   - Recursively check left and right

2. Traverse the main tree:
   - For each node, check if it matches <code>subRoot</code> using <code>isSame</code>
   - If yes → return <code>True</code>
   - Else continue searching left and right

---

### Complexity

- <strong>Time Complexity:</strong> O(n * m)  
- <strong>Space Complexity:</strong> O(h)

---

### Tags

tree, dfs, recursion, binary tree