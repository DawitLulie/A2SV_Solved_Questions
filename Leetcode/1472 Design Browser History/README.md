<h2><a href="https://leetcode.com/problems/design-browser-history">1472. Design Browser History</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You have a browser of one tab where you start on the <code>homepage</code> and you can visit another <code>url</code>, get back in the history, or move forward in the history.</p>

<p>Implement the <code>BrowserHistory</code> class:</p>

<ul>
<li><code>BrowserHistory(string homepage)</code> Initializes the object with the <code>homepage</code>.</li>
<li><code>void visit(string url)</code> Visits <code>url</code> from the current page. It clears up all the forward history.</li>
<li><code>string back(int steps)</code> Move <code>steps</code> steps back in history. If you can only return <code>x</code> steps in the history and <code>x &lt; steps</code>, you will return only <code>x</code> steps. Return the current <code>url</code> after moving back.</li>
<li><code>string forward(int steps)</code> Move <code>steps</code> steps forward in history. If you can only move <code>x</code> steps forward and <code>x &lt; steps</code>, you will move only <code>x</code> steps. Return the current <code>url</code> after moving forward.</li>
</ul>

---

### Example

<pre>
Input
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]
</pre>

---

### Constraints

<ul>
<li>1 ≤ homepage.length ≤ 20</li>
<li>1 ≤ url.length ≤ 20</li>
<li>1 ≤ steps ≤ 100</li>
<li>homepage and url consist of '.' or lowercase English letters.</li>
<li>At most 5000 calls will be made to visit, back, and forward.</li>
</ul>

---

### Solution

**Approach (Doubly Linked List):**

We implement the browser history as a **doubly linked list**:

- Each node stores a URL and has pointers to the **previous** and **next** nodes.
- `cur` pointer keeps track of the current page.

Operations:

1. **visit(url)**  
   - Create a new node for `url`.
   - Set its `prev` pointer to the current node.
   - Update the `next` of the current node to the new node.
   - Move the `cur` pointer to the new node.
   - Forward history beyond `cur` is automatically discarded since we overwrite `next`.

2. **back(steps)**  
   - Move `cur` to `cur.prev` up to `steps` times or until `prev` is `None`.

3. **forward(steps)**  
   - Move `cur` to `cur.next` up to `steps` times or until `next` is `None`.

This method simulates the browser history efficiently and naturally handles forward/back navigation.

---

### Complexity

- **Time Complexity:** O(steps) per `back`/`forward` call, O(1) per `visit`  
- **Space Complexity:** O(n) — one node per visited page

---

### Tags

design, linked list, simulation, doubly linked list