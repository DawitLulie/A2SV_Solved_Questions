<h2><a href="https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent">1315. Sum of Nodes with Even-Valued Grandparent</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given the <code>root</code> of a binary tree, return the sum of values of nodes with an even-valued grandparent.</p>

<p>A grandparent of a node is the parent of its parent.</p>

---

### Example 1

<pre>
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
</pre>

---

### Constraints

<ul>
<li>The number of nodes in the tree is in the range [1, 10⁴]</li>
<li>1 ≤ Node.val ≤ 100</li>
</ul>

---

# Solution

### Approach (DFS Traversal)

We traverse the tree using DFS while keeping track of:

- Current node
- Parent value
- Grandparent value

At each node:
- If the grandparent exists and its value is even, add the current node’s value to the result.

Steps:

1. Perform DFS starting from root.
2. Pass along:
   - parent value
   - grandparent value
3. At each node:
   - Check if grandparent is even
   - Add node value if condition is satisfied
4. Recurse for left and right children.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(h), where h is tree height (recursion stack)

---

### Tags

tree, dfs, binary tree, recursion