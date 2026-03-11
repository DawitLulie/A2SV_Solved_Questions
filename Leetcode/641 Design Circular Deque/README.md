<h2><a href="https://leetcode.com/problems/design-circular-deque">641. Design Circular Deque</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Design your implementation of a <strong>circular double-ended queue (deque)</strong>.</p>

<p>Implement the <code>MyCircularDeque</code> class:</p>

<ul>
<li><code>MyCircularDeque(int k)</code> Initializes the deque with maximum size <code>k</code>.</li>
<li><code>boolean insertFront(int value)</code> Adds an item at the front of the deque. Returns <code>true</code> if the operation is successful.</li>
<li><code>boolean insertLast(int value)</code> Adds an item at the rear of the deque. Returns <code>true</code> if the operation is successful.</li>
<li><code>boolean deleteFront()</code> Deletes an item from the front of the deque. Returns <code>true</code> if the operation is successful.</li>
<li><code>boolean deleteLast()</code> Deletes an item from the rear of the deque. Returns <code>true</code> if the operation is successful.</li>
<li><code>int getFront()</code> Gets the front item from the deque. If the deque is empty, return <code>-1</code>.</li>
<li><code>int getRear()</code> Gets the last item from the deque. If the deque is empty, return <code>-1</code>.</li>
<li><code>boolean isEmpty()</code> Checks whether the circular deque is empty.</li>
<li><code>boolean isFull()</code> Checks whether the circular deque is full.</li>
</ul>

---

### Example

<pre>
Input
["MyCircularDeque","insertLast","insertLast","insertFront","insertFront",
 "getRear","isFull","deleteLast","insertFront","getFront"]

[[3],[1],[2],[3],[4],[],[],[],[4],[]]

Output
[null,true,true,true,false,2,true,true,true,4]
</pre>

---

### Constraints

<ul>
<li>1 ≤ k ≤ 1000</li>
<li>0 ≤ value ≤ 1000</li>
<li>At most 2000 calls will be made to the methods.</li>
</ul>

---

### Solution

**Approach (Doubly Linked List):**

In this implementation, the deque is built using a **doubly linked list**.

Each node stores:
- `val`
- `prev` pointer
- `next` pointer

We maintain two pointers:

- `head` → front of the deque  
- `tail` → rear of the deque  

And two counters:

- `k` → maximum capacity  
- `capacity` → current number of elements

Operations:

1. **insertFront**
   - Create a new node.
   - Attach it before the current `head`.
   - Update `head`.

2. **insertLast**
   - Create a new node.
   - Attach it after the current `tail`.
   - Update `tail`.

3. **deleteFront**
   - Move `head` to `head.next`.
   - Update `prev` pointer.

4. **deleteLast**
   - Move `tail` to `tail.prev`.
   - Update `next` pointer.

5. **getFront / getRear**
   - Return values from `head` or `tail`.

6. **isEmpty / isFull**
   - Check using the `capacity` variable.

This structure allows efficient **O(1)** operations for insertion and deletion at both ends.

---

### Complexity

- **Time Complexity:** O(1) for all operations  
- **Space Complexity:** O(k)

---

### Tags

design, linked list, deque, data structure