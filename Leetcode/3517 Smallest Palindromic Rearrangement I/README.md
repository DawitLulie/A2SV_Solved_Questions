<h2><a href="https://leetcode.com/problems/smallest-palindromic-rearrangement-i">3517. Smallest Palindromic Rearrangement I</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given a <strong>palindromic</strong> string <code>s</code>.</p>

<p>Return the <strong>lexicographically smallest palindromic permutation</strong> of <code>s</code>.</p>

<p>A string is <strong>palindromic</strong> if it reads the same forward and backward.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: s = "z"
Output: "z"
Explanation:
A string of only one character is already the lexicographically smallest palindrome.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: s = "babab"
Output: "abbba"
Explanation:
Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: s = "daccad"
Output: "acddca"
Explanation:
Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= s.length &lt;= 10⁵</li>
  <li>s consists of lowercase English letters.</li>
  <li>s is guaranteed to be palindromic.</li>
</ul>

---

### Solution

**Approach:**  
- Since the string is already palindromic, we only need to rearrange it to get the lexicographically smallest palindrome.
- Take the first half of the string.
- Sort it.
- Mirror it to form the full palindrome.
- If the length is odd, keep the middle character unchanged.

**Complexity:**  
- Time: O(n log n) — sorting half of the string  
- Space: O(n) — building the result  

---
