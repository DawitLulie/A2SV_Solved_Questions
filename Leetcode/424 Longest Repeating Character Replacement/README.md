<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement">424. Longest Repeating Character Replacement</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>s</code> consisting of uppercase English letters, you can perform at most <code>k</code> operations. In one operation, you can choose any character of the string and change it to any other uppercase English character.</p>

<p>Return the length of the longest substring containing the same letter you can get after performing the above operations.</p>

---

### Example 1

<pre>
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace two 'A's with 'B's or two 'B's with 'A's.
</pre>

---

### Example 2

<pre>
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'A' with 'B' to get "AABBBBA", the longest repeating substring is "BBBB".
</pre>

---

### Constraints

<ul>
<li>1 ≤ s.length ≤ 10⁵</li>
<li>0 ≤ k ≤ s.length</li>
<li>s consists of only uppercase English letters.</li>
</ul>

---

### Approach (Sliding Window)

- Maintain a sliding window [left, right] representing the current substring.
- Track the count of the most frequent character in the window.
- While window size minus max frequency > k, shrink the window from the left.
- Update the maximum window size seen so far.

---

### Complexity

- Time: O(n)  
- Space: O(26) ≈ O(1)