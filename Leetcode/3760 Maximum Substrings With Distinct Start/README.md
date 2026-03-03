<h2><a href="https://leetcode.com/problems/maximum-substrings-with-distinct-start">3760. Maximum Substrings With Distinct Start</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>Return an integer denoting the maximum number of substrings you can split <code>s</code> into such that each substring starts with a distinct character (i.e., no two substrings start with the same character).</p>

---

### Example 1

<pre>
Input: s = "abab"
Output: 2
Explanation:
Split "abab" into "a" and "bab".
Each substring starts with a distinct character: 'a' and 'b'.
</pre>

### Example 2

<pre>
Input: s = "abcd"
Output: 4
Explanation:
Split "abcd" into "a", "b", "c", and "d".
Each substring starts with a distinct character.
</pre>

### Example 3

<pre>
Input: s = "aaaa"
Output: 1
Explanation:
All characters in "aaaa" are 'a'.
Only one substring can start with 'a'.
</pre>

---

### Constraints

<ul>
  <li>1 ≤ s.length ≤ 10⁵</li>
  <li><code>s</code> consists of lowercase English letters.</li>
</ul>

---

### Solution

**Approach (Count Distinct First Letters):**

- Each substring must start with a distinct character.
- To maximize the number of such substrings, count how many distinct letters appear in <code>s</code>.
- The result is simply the number of unique characters in the string.

**Reasoning:**  
Splitting can always be done so that each unique character begins one substring. Counting unique characters gives the maximum number of distinct starting substrings. :contentReference[oaicite:0]{index=0}

---

### Complexity

- **Time:** O(n) — iterate over the string once  
- **Space:** O(1) — only 26 possible lowercase letters

---

### Tags

string, hash table, counting