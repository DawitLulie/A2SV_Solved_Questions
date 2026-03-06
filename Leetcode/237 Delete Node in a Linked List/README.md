<h2><a href="https://leetcode.com/problems/delete-node-in-a-linked-list">237. Delete Node in a Linked List</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.</p>

<p>You are not given access to the head of the list. The node to be deleted is guaranteed not to be the tail.</p>

---

### Example 1

<pre>
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: Node with value 5 is deleted.
</pre>

### Example 2

<pre>
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
</pre>

---

### Constraints

<ul>
  <li>The number of nodes in the list is in the range <code>[2, 1000]</code></li>
  <li>-1000 ≤ Node.val ≤ 1000</li>
  <li>All the values of the linked list are unique</li>
  <li>The given node is not the tail and exists in the list</li>
</ul>

---

### Solution

**Approach (In-place Node Replacement):**

Since we do not have access to the previous node:

1. Copy the value of the next node into the current node:
   <pre>node.val = node.next.val</pre>
2. Bypass the next node:
   <pre>node.next = node.next.next</pre>

This effectively deletes the target node in O(1) time.

---

### Complexity

- **Time:** O(1)  
- **Space:** O(1)

---

### Tags

linked list, in-place, two pointers