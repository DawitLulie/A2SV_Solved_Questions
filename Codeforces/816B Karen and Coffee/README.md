<h2><a href="https://codeforces.com/contest/816/problem/B">816B. Karen and Coffee</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1400-orange' alt='Difficulty: 1400' />
<hr>

<p>Karen loves coffee and wants to drink it every day.</p>

<p>There are <code>n</code> recipes, and each recipe is active during an interval 
<code>[l<sub>i</sub>, r<sub>i</sub>]</code> (inclusive).</p>

<p>A day is considered <strong>good</strong> if at least <code>k</code> recipes are active on that day.</p>

<p>You are given <code>q</code> queries. Each query consists of two integers 
<code>a</code> and <code>b</code>. For each query, determine how many good days are in the interval <code>[a, b]</code>.</p>

---

### Example

<pre>
Input:
3 1 3
1 3
2 4
5 6
1 4
2 5
3 6

Output:
4
3
2
</pre>

---

### Constraints

<ul>
  <li>1 ≤ n, q ≤ 2 × 10⁵</li>
  <li>1 ≤ k ≤ n</li>
  <li>1 ≤ l<sub>i</sub> ≤ r<sub>i</sub> ≤ 2 × 10⁵</li>
  <li>1 ≤ a ≤ b ≤ 2 × 10⁵</li>
</ul>

---

### Solution

**Approach (Difference Array + Prefix Sum):**

1. Initialize a difference array <code>prefix</code> of size slightly larger than the maximum day.
2. For each recipe interval <code>[l<sub>i</sub>, r<sub>i</sub>]</code>:
   - Increment <code>prefix[l<sub>i</sub>]</code> by 1.
   - Decrement <code>prefix[r<sub>i</sub> + 1]</code> by 1.
3. Compute the prefix sum of <code>prefix</code> to get the number of active recipes for each day.
4. Build a cumulative array <code>valid</code> counting days where active recipes ≥ k.
5. For each query <code>[a, b]</code>, answer in O(1) using:
   <pre>
   valid[b] - valid[a - 1]
   </pre>

**Why this works:**  
- Difference array efficiently handles range updates for intervals.  
- Prefix sum converts it to actual counts per day.  
- Cumulative <code>valid</code> array allows constant-time range queries.

---

### Complexity

- **Time:** O(n + q + max_day) — iterate recipes and compute prefix sums  
- **Space:** O(max_day) — arrays to store prefix counts and cumulative valid days

---

### Tags

data structures, implementation, prefix sum