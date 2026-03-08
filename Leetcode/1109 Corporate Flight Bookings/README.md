<h2><a href="https://leetcode.com/problems/corporate-flight-bookings">1109. Corporate Flight Bookings</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>There are <code>n</code> flights that are labeled from <code>1</code> to <code>n</code>.</p>

<p>You are given an array of flight bookings <code>bookings</code>, where 
<code>bookings[i] = [first<sub>i</sub>, last<sub>i</sub>, seats<sub>i</sub>]</code> represents a booking for 
<code>seats<sub>i</sub></code> seats on every flight from <code>first<sub>i</sub></code> to 
<code>last<sub>i</sub></code> (inclusive).</p>

<p>Return an array <code>answer</code> of length <code>n</code>, where 
<code>answer[i]</code> is the total number of seats booked on flight <code>i + 1</code>.</p>

---

### Example 1

<pre>
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
</pre>

### Example 2

<pre>
Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
</pre>

---

### Constraints

<ul>
<li>1 ≤ n ≤ 2 * 10⁴</li>
<li>1 ≤ bookings.length ≤ 2 * 10⁴</li>
<li>bookings[i].length == 3</li>
<li>1 ≤ first<sub>i</sub> ≤ last<sub>i</sub> ≤ n</li>
<li>1 ≤ seats<sub>i</sub> ≤ 10⁴</li>
</ul>

---

### Solution

**Approach (Difference Array + Prefix Sum):**

Each booking adds seats to a range of flights.

Instead of updating every flight in the range directly, we use a **difference array**:

1. Create an array <code>diff</code> of size <code>n</code> initialized with 0.
2. For each booking <code>[l, r, seats]</code>:
   <pre>
diff[l - 1] += seats
if r < n:
    diff[r] -= seats
</pre>
3. Compute the prefix sum of <code>diff</code> to get the final seat count for each flight.

This allows range updates in constant time.

---

### Complexity

- **Time:** O(n + m)  
- **Space:** O(n)

Where:
- <code>n</code> = number of flights  
- <code>m</code> = number of bookings

---

### Tags

array, prefix sum