<h2><a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/">17. Letter Combinations of a Phone Number</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />
<hr>

<p>
Given a string containing digits from <code>2-9</code>, return all possible letter combinations that the number could represent.
Return the answer in <b>any order</b>.
</p>

<p>
The mapping of digits to letters is just like on a telephone keypad.
</p>

<hr>

<h3>📌 Example 1:</h3>

<pre>
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
</pre>

<h3>📌 Example 2:</h3>

<pre>
Input: digits = ""
Output: []
</pre>

<hr>

<h3>⚡ Constraints:</h3>

<ul>
<li>0 ≤ digits.length ≤ 4</li>
<li>digits[i] is a digit in the range ['2', '9']</li>
</ul>

<hr>

<h3>💡 Approach (Backtracking):</h3>

<p>
We use <b>backtracking</b> to generate all possible combinations.
</p>

<h4>Step-by-step:</h4>

<ol>
<li>Create a mapping of digits to letters</li>
<li>Start from the first digit</li>
<li>For each digit:
  <ul>
    <li>Try all possible letters</li>
  </ul>
</li>
<li>Build the string step by step</li>
<li>When the length of the string equals digits length → save it</li>
</ol>

<hr>

<h3>🧠 Why This Works:</h3>

<p>
Each digit has multiple choices. Backtracking explores all paths by:
</p>

<ul>
<li>Picking one letter</li>
<li>Going deeper</li>
<li>Undoing (backtracking) and trying another</li>
</ul>

<hr>

<h3>⏱️ Time Complexity:</h3>

<p>
O(4<sup>n</sup>) → each digit can have up to 4 letters
</p>

<h3>💾 Space Complexity:</h3>

<p>
O(n) → recursion stack
</p>

<hr>

<h3>🏷️ Tags:</h3>

<p>Backtracking, Recursion, String</p>