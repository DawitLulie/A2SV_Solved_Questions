<h2><a href="https://leetcode.com/problems/odd-even-linked-list">328. Odd Even Linked List</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given the <code>head</code> of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.</p>

<p>The first node is considered <strong>odd</strong>, and the second node is <strong>even</strong>, and so on.</p>

<p>Note that the relative order inside both the even and odd groups should remain the same as it was in the input.</p>

<p>You must solve the problem in <strong>O(1)</strong> extra space complexity and <strong>O(n)</strong> time complexity.</p>

---

### Example 1

<pre>
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
</pre>

### Example 2

<pre>
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
</pre>

---

### Constraints

<ul>
  <li>The number of nodes in the linked list is in the range <code>[0, 10⁴]</code></li>
  <li>-10⁶ ≤ Node.val ≤ 10⁶</li>
</ul>

---

### Solution

**Approach (Two Pointers on Linked List):**

We separate the list into two parts:
- Odd indexed nodes
- Even indexed nodes

Steps:

1. Keep two pointers:
   - <code>odd</code> starting at the first node
   - <code>even</code> starting at the second node
2. Save the start of the even list (<code>even_head</code>) so we can attach it later.
3. Iterate through the list:
   - Connect the next odd node: <code>odd.next = even.next</code>
   - Move <code>odd</code> forward
   - Connect the next even node: <code>even.next = odd.next</code>
   - Move <code>even</code> forward
4. After the loop, attach the even list after the odd list:
   <pre>
   odd.next = even_head
   </pre>

This keeps the relative order of nodes while grouping odds first and evens second.

---

### Complexity

- **Time:** O(n) — we traverse the list once  
- **Space:** O(1) — no extra data structures used

---

### Tags

linked list, two pointers