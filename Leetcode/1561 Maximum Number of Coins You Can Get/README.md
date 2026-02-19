<h2><a href="https://leetcode.com/problems/maximum-number-of-coins-you-can-get">1561. Maximum Number of Coins You Can Get</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>There are <code>3n</code> piles of coins of varying size, you and your friends will take piles of coins as follows:</p>

<ul>
  <li>In each step, you will choose any <strong>3 piles</strong> of coins (not necessarily consecutive).</li>
  <li>Of your choice, Alice will pick the pile with the <strong>maximum</strong> number of coins.</li>
  <li>You will pick the next pile with the <strong>maximum</strong> number of coins.</li>
  <li>Your friend Bob will pick the last pile.</li>
</ul>

<p>Repeat until there are no more piles of coins.</p>

<p>Given an integer array <code>piles</code> of size <code>3n</code>, return the <strong>maximum number of coins</strong> that you can have.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose piles (2,7,8) → Alice: 8, You: 7, Bob: 2  
Choose piles (1,2,4) → Alice: 4, You: 2, Bob: 1  
Total = 7 + 2 = 9
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: piles = [2,4,5]
Output: 4
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>3 &lt;= piles.length &lt;= 10⁵</li>
  <li>piles.length % 3 == 0</li>
  <li>1 &lt;= piles[i] &lt;= 10⁴</li>
</ul>

---

### Solution

**Approach:**  
- Sort the array in ascending order.  
- Since Alice always takes the largest, and Bob takes the smallest among the three,  
  we simulate optimal play by:
  - Ignoring the smallest third (Bob’s picks).
  - From the remaining largest elements, take every second element starting from the second largest.
- Accumulate the values for your picks.

**Complexity:**  
- Time: O(n log n) — due to sorting  
- Space: O(1) — ignoring sorting space (or O(n) depending on implementation)

---
