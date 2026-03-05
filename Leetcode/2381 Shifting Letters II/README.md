<h2><a href="https://leetcode.com/problems/shifting-letters-ii">2381. Shifting Letters II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a string <code>s</code> of lowercase English letters and a 2D integer array <code>shifts</code> where <code>shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]</code>.</p>

<p>For every <code>i</code>:</p>

<ul>
  <li>If <code>direction<sub>i</sub> = 1</code>, shift the characters in the range <code>[start<sub>i</sub>, end<sub>i</sub>]</code> forward by one letter.</li>
  <li>If <code>direction<sub>i</sub> = 0</code>, shift the characters in the range <code>[start<sub>i</sub>, end<sub>i</sub>]</code> backward by one letter.</li>
</ul>

<p>Shifting forward means <code>'z'</code> becomes <code>'a'</code>.  
Shifting backward means <code>'a'</code> becomes <code>'z'</code>.</p>

<p>Return the final string after all operations are applied.</p>

---

### Example 1

<pre>
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
</pre>

### Example 2

<pre>
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
</pre>

---

### Constraints

<ul>
  <li>1 ≤ s.length ≤ 5 * 10⁴</li>
  <li>1 ≤ shifts.length ≤ 5 * 10⁴</li>
  <li>0 ≤ start<sub>i</sub> ≤ end<sub>i</sub> &lt; s.length</li>
  <li>direction<sub>i</sub> is either 0 or 1</li>
</ul>

---

### Solution

**Approach (Prefix Sum / Difference Array):**

Applying each shift directly to every character would be too slow.  
Instead, we use a **difference array** to track how shifts affect ranges.

Steps:

1. Create a difference array <code>diff</code> of size <code>n + 1</code>.
2. For each shift:
   - If direction = 1 → add <code>+1</code>
   - If direction = 0 → add <code>-1</code>
3. Update the range using difference array:
   <pre>
   diff[l] += val
   diff[r + 1] -= val
   </pre>
4. Build prefix sum to compute total shift for each index.
5. Apply the shift to each character using modulo 26.

---

### Why this works

The difference array allows us to apply **range updates in O(1)** instead of modifying every element in the range.

After computing prefix sums, we know the **total shift applied to each character**.

---

### Complexity

- **Time:** O(n + m)  
- **Space:** O(n)

Where:
- <code>n</code> = length of string  
- <code>m</code> = number of shift operations

---

### Tags

array, prefix sum, string