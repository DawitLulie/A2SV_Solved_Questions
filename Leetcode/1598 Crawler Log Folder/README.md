<h2><a href="https://leetcode.com/problems/crawler-log-folder">1598. Crawler Log Folder</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given a list of strings <code>logs</code> representing operations performed by a file system crawler. Initially, the crawler starts in the main folder <code>"/"</code>.</p>

<p>The operations are as follows:</p>

<ul>
<li><code>"../"</code> : Move to the parent folder. If already in the main folder, stay in "/".</li>
<li><code>"./"</code> : Stay in the current folder.</li>
<li><code>"x/"</code> : Move into a child folder named <code>x</code>.</li>
</ul>

<p>Return the <strong>minimum number of steps</strong> required to go back to the main folder after performing all operations in <code>logs</code>.</p>

---

### Example 1

<pre>
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation:
- Move to "d1/"
- Move to "d2/"
- "../" → back to "d1/"
- Move to "d21/"
- "./" → stay
Steps to return to main folder: 2 ("../" twice)
</pre>

### Example 2

<pre>
Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3
</pre>

### Example 3

<pre>
Input: logs = ["d1/","../","../","../"]
Output: 0
</pre>

---

### Constraints

<ul>
<li>1 ≤ logs.length ≤ 10³</li>
<li>2 ≤ logs[i].length ≤ 10</li>
<li><code>logs[i]</code> contains lowercase English letters, digits, '.', and '/'</li>
<li>logs[i] follows one of the described formats</li>
</ul>

---

### Solution

**Approach (Counter / Stack Simulation):**

We can simulate the crawler using a simple counter:

1. Initialize `depth = 0`.
2. Iterate through each log:
   - If `log == "../"`: decrement `depth` if `depth > 0`.
   - If `log == "./"`: do nothing.
   - Else: increment `depth` (moving into a child folder).
3. After processing all logs, `depth` is the number of steps to return to the main folder.

This avoids the need for a stack and works in O(n) time.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

Where `n` is the number of logs.

---

### Tags

simulation, string, stack