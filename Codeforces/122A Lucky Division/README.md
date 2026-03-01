<h2><a href="https://codeforces.com/problemset/problem/122/A">122A. Lucky Division</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1000-yellow' alt='Difficulty: 1000' />
<hr>

<p>Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits <strong>4</strong> and <strong>7</strong>.  
Petya calls a number <strong>almost lucky</strong> if it can be evenly divided by some lucky number. Given an integer <code>n</code>, determine whether it is almost lucky.</p>

<p><strong>Input:</strong></p>
<pre>
The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.
</pre>

<p><strong>Output:</strong></p>
<pre>
Print <code>YES</code> if number n is almost lucky. Otherwise, print <code>NO</code>.
</pre>

<p><strong>Example 1:</strong></p>
<pre>
Input: 47
Output: YES
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: 16
Output: YES
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: 78
Output: NO
</pre>

<p><strong>Explanation:</strong></p>
<ul>
  <li><code>47</code> is itself a lucky number, so it’s almost lucky.</li>
  <li><code>16</code> is divisible by <code>4</code>, which is a lucky number.</li>
  <li><code>78</code> is not divisible by any lucky number → not almost lucky.</li>
</ul>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ n ≤ 1000</li>
</ul>

---

### Solution

**Approach:**  
- Precompute all lucky numbers up to 1000.  
- Check if the given number is divisible by any lucky number.  
- If yes, print “YES”, otherwise “NO”.  

**Why it works:**  
Lucky numbers are rare within 1…1000, so checking divisibility is fast and simple.  

**Complexity:**  
- Time: O(L) where L is number of lucky numbers (very small)  
- Space: O(1)

---