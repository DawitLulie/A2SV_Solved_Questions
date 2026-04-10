<h2>
<a href="https://leetcode.com/problems/fair-distribution-of-cookies">
2305. Fair Distribution of Cookies
</a>
</h2>

<p>
Solved on <b>:contentReference[oaicite:0]{index=0}</b>
</p>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium"/>

<hr>

<h2> Problem Statement</h2>

<p>
You are given an integer array <code>cookies</code>, where <code>cookies[i]</code> represents the number of cookies in the ith bag.
You are also given an integer <code>k</code> representing the number of children.
</p>

<p>
You need to distribute all cookies among <code>k</code> children such that the unfairness is minimized.
</p>

<h3>🔴 Unfairness Definition:</h3>
<p>
Unfairness is the <b>maximum total cookies any child receives</b>.
</p>

<hr>

<h2>📌 Example 1</h2>

<pre>
Input: cookies = [8, 15, 10, 20, 8], k = 2
Output: 31
</pre>

<p><b>Explanation:</b></p>
<ul>
<li>Child 1 → [8, 15, 8] = 31</li>
<li>Child 2 → [10, 20] = 30</li>
</ul>

<p><b>Answer = 31 (minimum possible unfairness)</b></p>

<hr>

<h2>📌 Example 2</h2>

<pre>
Input: cookies = [6, 1, 3, 2, 2, 4, 1, 2], k = 3
Output: 7
</pre>

<hr>

<h2>💡 Approach (Backtracking + Pruning)</h2>

<p>
We try all possible ways to assign each cookie bag to one of the k children.
</p>

<h3>Key Idea:</h3>
<ul>
<li>Maintain an array <code>distribution[i]</code> = cookies given to child i</li>
<li>Try assigning each cookie recursively</li>
</ul>

<h3>Steps:</h3>
<ol>
<li>Sort cookies in descending order (important optimization)</li>
<li>Assign each cookie to any child</li>
<li>Recurse to next cookie</li>
<li>Track maximum load per distribution</li>
<li>Minimize the result</li>
</ol>

<h3>🔥 Pruning:</h3>
<p>
If current maximum already exceeds best answer, stop exploring that path.
</p>

<hr>

<h2>⚙️ Complexity Analysis</h2>

<ul>
<li><b>Time Complexity:</b> O(k^n)</li>
<li><b>Space Complexity:</b> O(k + n)</li>
</ul>

<p>
Where n = number of cookie bags, k = number of children.
</p>

<hr>

<h2>🚀 Intuition</h2>

<p>
We explore all possible distributions but cut invalid paths early using pruning.
Because constraints are small, backtracking is efficient.
</p>

<hr>

<h2>✅ Tags</h2>
<p>Backtracking, Recursion, Pruning, Brute Force</p>