<h2><a href="https://leetcode.com/problems/bulls-and-cows">299. Bulls and Cows</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are playing the game "Bulls and Cows" with your friend.</p>

<p>You write a secret number and your friend tries to guess it. Each time your friend makes a guess, you provide a hint:</p>
<ul>
  <li>The number of <strong>bulls</strong>: digits in the guess that are in the correct position.</li>
  <li>The number of <strong>cows</strong>: digits in the guess that are in your secret number but in the wrong position.</li>
</ul>

<p>Given two strings <code>secret</code> and <code>guess</code>, return the hint for your friend's guess.</p>

<p>The hint should be formatted as <code>"xAyB"</code>, where <code>x</code> is the number of bulls and <code>y</code> is the number of cows.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: 1 bull (8), 3 cows (1,0,7).
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: 1 bull (1), 1 cow (1).
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= secret.length, guess.length &lt;= 1000</li>
  <li>secret.length == guess.length</li>
  <li>secret and guess consist of digits only.</li>
</ul>

---

### Solution

**Approach:**  
- Iterate over both strings to count bulls (matching positions).  
- Use a counter or array to count remaining digits for cows.  
- Sum the minimum of counts from secret and guess for each digit to get cows.  
- Format the answer as `"xAyB"`.

**Complexity:**  
- Time: O(n) — n = length of secret  
- Space: O(1) — digits are 0-9, fixed size array  

---
