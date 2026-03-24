<h2><a href="https://leetcode.com/problems/two-sum-iv-input-is-a-bst">653. Two Sum IV - Input is a BST</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given the root of a Binary Search Tree and an integer <code>k</code>, return <code>true</code> if there exist two elements in the BST such that their sum is equal to <code>k</code>, or <code>false</code> otherwise.</p>

---

### Example 1

<pre>
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Explanation: 5 + 4 = 9
</pre>

### Example 2

<pre>
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
</pre>

---

### Constraints

<ul>
<li>The number of nodes in the tree is in the range [1, 10⁴]</li>
<li>-10⁴ ≤ Node.val ≤ 10⁴</li>
<li>root is guaranteed to be a valid BST</li>
<li>-10⁵ ≤ k ≤ 10⁵</li>
</ul>

---

# Solution

### Approach (DFS + Hash Set)

We traverse the tree and store visited values in a set.

Steps:

1. Traverse the tree using DFS.
2. For each node with value <code>x</code>:
   - Check if <code>k - x</code> exists in the set.
   - If yes → return <code>True</code>.
3. Otherwise, add <code>x</code> to the set.
4. Continue traversal.

This is similar to the classic Two Sum problem.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(n)

---

### Tags

tree, dfs, hash table, binary search tree