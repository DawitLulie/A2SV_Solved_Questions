<h2><a href="https://leetcode.com/problems/custom-sort-string">791. Custom Sort String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given two strings <code>order</code> and <code>s</code>.  
All the characters of <code>order</code> are unique, and you want to sort the characters of <code>s</code> so that they match the order defined in <code>order</code>.  
Characters in <code>s</code> that do not appear in <code>order</code> can be placed anywhere at the end of the result.</p>

<p>Return <em>any permutation of <code>s</code> that satisfies this property</em>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
The characters 'a', 'b', 'c' appear in order "cba". 'd' can be anywhere.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: order = "kqep", s = "pekeq"
Output: "kqeep"
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ order.length ≤ 26</li>
  <li>1 ≤ s.length ≤ 200</li>
  <li>order and s consist of lowercase English letters.</li>
  <li>All characters in order are unique.</li>
</ul>

---

###  Solution

**Approach:**  
- Count the frequency of each character in `s`.  
- Iterate over characters in `order`, append them in order using their counts.  
- Append remaining characters not in `order` at the end.  
- Return the resulting string.

**Complexity:**  
- Time: O(n + m) — n = length of `s`, m = length of `order`  
- Space: O(26) = O(1) — for counting letters  

---