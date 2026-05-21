<h2><a href="https://leetcode.com/problems/longest-common-subsequence/">1143. Longest Common Subsequence</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />

<hr>

<h3>📌 Problem Summary</h3>

<p>
Given two strings <code>text1</code> and <code>text2</code>, return the length of their <b>Longest Common Subsequence</b>.
</p>

<p>
A subsequence is a sequence that can be derived from another string by deleting some characters without changing the order of the remaining characters.
</p>

<hr>

<h3>🧪 Examples</h3>

<pre>
<b>Input:</b>
text1 = "abcde"
text2 = "ace"

<b>Output:</b>
3

<b>Explanation:</b>
The longest common subsequence is "ace".
</pre>

<pre>
<b>Input:</b>
text1 = "abc"
text2 = "abc"

<b>Output:</b>
3
</pre>

<pre>
<b>Input:</b>
text1 = "abc"
text2 = "def"

<b>Output:</b>
0
</pre>

<hr>

<h3>📋 Constraints</h3>

<ul>
<li><code>1 ≤ text1.length, text2.length ≤ 1000</code></li>
<li><code>text1</code> and <code>text2</code> consist of lowercase English characters.</li>
</ul>

<hr>

<h3>💡 Approach (Dynamic Programming)</h3>

<p>
We use Dynamic Programming to solve this problem.
</p>

<p>
Let:
</p>

<pre>
dp(i, j)
</pre>

<p>
represent the length of the longest common subsequence between:
</p>

<ul>
<li><code>text1[i:]</code></li>
<li><code>text2[j:]</code></li>
</ul>

<hr>

<h3>🔄 Transition</h3>

<p>
If the characters are equal:
</p>

<pre>
text1[i] == text2[j]
</pre>

<p>
then we include that character:
</p>

<pre>
1 + dp(i + 1, j + 1)
</pre>

<p>
Otherwise, we try skipping one character from either string:
</p>

<pre>
max(dp(i + 1, j), dp(i, j + 1))
</pre>

<hr>

<h3>🪜 Steps</h3>

<ol>
<li>Create a memoization dictionary</li>
<li>Use recursion with DP</li>
<li>If characters match:
    <ul>
        <li>Move both pointers</li>
    </ul>
</li>
<li>Otherwise:
    <ul>
        <li>Skip one character from either string</li>
    </ul>
</li>
<li>Store computed results to avoid recomputation</li>
</ol>

<hr>

<h3>✅ Why This Works</h3>

<p>
At every position, we try all valid possibilities:
</p>

<ul>
<li>Take matching characters</li>
<li>Skip characters when they do not match</li>
</ul>

<p>
Memoization prevents repeated calculations, making the solution efficient.
</p>

<hr>

<h3>⏱️ Time Complexity</h3>

<p>
<code>O(n × m)</code>
</p>

<p>
Where:
</p>

<ul>
<li><code>n = len(text1)</code></li>
<li><code>m = len(text2)</code></li>
</ul>

<hr>

<h3>💾 Space Complexity</h3>

<p>
<code>O(n × m)</code>
</p>

<hr>

<h3>🏷️ Tags</h3>

<p>
Dynamic Programming, String, Memoization
</p>