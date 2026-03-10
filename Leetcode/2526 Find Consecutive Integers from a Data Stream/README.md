<h2><a href="https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream">2526. Find Consecutive Integers from a Data Stream</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>For a stream of integers, implement a data structure that checks if the last <code>k</code> integers are equal to a given value.</p>

<p>Implement the <code>DataStream</code> class:</p>

<ul>
<li><code>DataStream(int value, int k)</code> Initializes the object with an integer <code>value</code> and the integer <code>k</code>.</li>
<li><code>boolean consec(int num)</code> Adds the integer <code>num</code> to the stream and checks if the last <code>k</code> integers are equal to <code>value</code>. Returns <code>true</code> if true, otherwise <code>false</code>.</li>
</ul>

---

### Example

<pre>
Input
["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]

Output
[null, false, false, true, false]

Explanation
DataStream ds = new DataStream(4, 3);
ds.consec(4); // return false
ds.consec(4); // return false
ds.consec(4); // return true
ds.consec(3); // return false
</pre>

---

### Constraints

<ul>
<li>1 ≤ value, num ≤ 10⁹</li>
<li>1 ≤ k ≤ 10⁵</li>
<li>At most 10⁵ calls will be made to <code>consec</code>.</li>
</ul>

---

### Solution

**Approach (Counting Consecutive Values):**

Instead of storing the entire stream, we only track how many **consecutive values equal to `value`** appear at the end.

Steps:

1. Store `value` and `k`.
2. Maintain a counter `count`.
3. For each incoming number:
   - If `num == value`, increase `count`.
   - Otherwise, reset `count` to `0`.
4. Return `True` if `count >= k`, otherwise `False`.

This efficiently checks whether the last `k` values match the required number.

---

### Complexity

- **Time Complexity:** O(1) per operation  
- **Space Complexity:** O(1)

---

### Tags

design, data stream, queue, simulation