<h2><a href="https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/">1415. The k-th Lexicographical String of All Happy Strings of Length n</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
A <b>happy string</b> is a string that:
<ul>
  <li>consists only of letters <code>a</code>, <code>b</code>, <code>c</code></li>
  <li>no two adjacent characters are the same</li>
</ul>
</p>

<p>
Given integers <code>n</code> and <code>k</code>, return the k-th lexicographical happy string of length n.
If there are fewer than k happy strings, return an empty string.
</p>

<h3>Approach</h3>
<ul>
  <li>Use backtracking to generate all valid happy strings in lexicographical order.</li>
  <li>Stop early when we reach the k-th string.</li>
</ul>

<h3>Time Complexity</h3>
<p>O(3 * 2^(n-1)) in worst case</p>

<h3>Space Complexity</h3>
<p>O(n) recursion depth</p>