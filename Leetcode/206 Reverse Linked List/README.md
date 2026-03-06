<h2><a href="https://leetcode.com/problems/reverse-linked-list">206. Reverse Linked List</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given the <code>head</code> of a singly linked list, reverse the list, and return the reversed list.</p>

---

### Example 1

<pre>
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
</pre>

### Example 2

<pre>
Input: head = [1,2]
Output: [2,1]
</pre>

### Example 3

<pre>
Input: head = []
Output: []
</pre>

---

### Constraints

<ul>
  <li>The number of nodes in the list is in the range <code>[0, 5000]</code></li>
  <li>-5000 ≤ Node.val ≤ 5000</li>
</ul>

---

### Solution

**Approach (Iterative / Two Pointers):**

We reverse the linked list using two pointers:

1. Initialize:
   - <code>prev = None</code>
   - <code>current = head</code>
2. Iterate while <code>current</code> is not None:
   - Save next node: <code>next_node = current.next</code>
   - Reverse pointer: <code>current.next = prev</code>
   - Move pointers forward:
     - <code>prev = current</code>
     - <code>current = next_node</code>
3. After the loop, <code>prev</code> points to the new head of the reversed list.

---

### Complexity

- **Time:** O(n) — traverse the list once  
- **Space:** O(1) — in-place reversal

---

### Tags

linked list, two pointers, iterative