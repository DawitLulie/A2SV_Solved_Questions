<h2><a href="https://leetcode.com/problems/partition-labels">763. Partition Labels</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a string <code>s</code>. We want to partition the string into as many parts as possible so that each letter appears in <strong>at most one part</strong>.</p>

<p>Note that the partition is done so that after concatenating all the parts in order, the resulting string should be <code>s</code>.</p>

<p>Return a list of integers representing the size of these parts.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect,
because it splits the string into less parts.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "eccbbbbdec"
Output: [10]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 500</li>
  <li><code>s</code> consists of lowercase English letters.</li>
</ul>

---

### Solution

**Approach:**  
Use a greedy strategy.

1. First, record the last occurrence index of every character.
2. Iterate through the string and keep track of the farthest last occurrence seen so far.
3. When the current index equals that farthest position, we form a partition.
4. Start a new partition after that.

This ensures each letter appears in only one part.

**Complexity:**  
- Time: O(n)  
- Space: O(1) (since only 26 lowercase letters)  

---
