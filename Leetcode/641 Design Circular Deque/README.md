<h2><a href="https://leetcode.com/problems/design-circular-deque">641. Design Circular Deque</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Design your implementation of a <strong>circular double-ended queue (deque)</strong>.</p>

<p>Implement the <code>MyCircularDeque</code> class:</p>

<ul>
<li><code>MyCircularDeque(int k)</code> Initializes the deque with maximum size <code>k</code>.</li>
<li><code>boolean insertFront()</code> Adds an item at the front of the deque. Returns <code>true</code> if the operation is successful.</li>
<li><code>boolean insertLast()</code> Adds an item at the rear of the deque. Returns <code>true</code> if the operation is successful.</li>
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

**Approach (Circular Array):**

We implement the deque using a fixed-size array and two pointers:

- `front` → points to the front element  
- `rear` → points to the rear element  

Key ideas:

1. Use **modulo arithmetic** to wrap around the array.
2. Track the number of elements using `size`.
3. For insertion:
   - Update the pointer first, then insert the value.
4. For deletion:
   - Move the pointer appropriately.

This allows constant-time operations for all deque methods.

---

### Complexity

- **Time Complexity:** O(1) for all operations  
- **Space Complexity:** O(k)

---

### Tags

design, queue, deque, circular queue, data structure