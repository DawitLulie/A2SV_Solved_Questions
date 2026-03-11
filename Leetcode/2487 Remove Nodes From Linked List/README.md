<h2><a href="https://leetcode.com/problems/remove-nodes-from-linked-list">2487. Remove Nodes From Linked List</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given the head of a linked list, remove every node which has a node with a strictly greater value anywhere to the right side of it.</p>

<p>Return the head of the modified linked list.</p>

---

### Example 1

<pre>
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation:
- Node 5 is removed because 13 is to its right.
- Node 2 is removed because 13 is to its right.
- Node 13 is kept.
- Node 3 is removed because 8 is to its right.
- Node 8 is kept.
</pre>

### Example 2

<pre>
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation:
No node has a strictly greater value to its right.
</pre>

---

### Constraints

<ul>
<li>The number of nodes in the list is in the range [1, 10⁵]</li>
<li>1 ≤ Node.val ≤ 10⁵</li>
</ul>

---

### Solution

**Approach (Reverse Linked List + Max Tracking):**

1. Reverse the linked list to process nodes from right to left.
2. Maintain a `max_val` seen so far.
3. Traverse the reversed list:
   - Keep a node if its value ≥ `max_val`.
   - Update `max_val` accordingly.
4. Reverse the list back to restore the original order.

This ensures that for each node, we only keep it if there’s no greater node to its right.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

### Tags

linked list, greedy, two pointers