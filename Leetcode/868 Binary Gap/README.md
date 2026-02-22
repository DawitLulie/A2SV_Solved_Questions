<h2><a href="https://leetcode.com/problems/binary-gap">868. Binary Gap</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given a positive integer <code>n</code>, find and return the longest distance between two consecutive <code>1</code>'s in the binary representation of <code>n</code>.  
If there are no two consecutive <code>1</code>'s, return <code>0</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: n = 22
Output: 2
Explanation:
22 in binary is 10110.
The consecutive 1's have distances:
index 0 → index 2 → distance = 2
index 2 → index 3 → distance = 1
Maximum distance = 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: n = 8
Output: 0
Explanation:
8 in binary is 1000.
There is only one '1'.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: n = 5
Output: 2
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ n ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**

1. Convert the number to its binary representation.
2. Traverse the binary string.
3. Track the index of the previous `1`.
4. Compute the distance between consecutive `1`s and keep the maximum.

**Alternative (bit manipulation):**
- Use bit shifting (`n >> 1`) and check last bit (`n & 1`) without converting to string.

**Complexity:**

- Time: O(log n) — number of bits in n  
- Space: O(1) extra  

---