<h2><a href="https://atcoder.jp/contests/dp/tasks/dp_a">A - Frog 1</a></h2>
<img src='https://img.shields.io/badge/AtCoder-DP_A-blue' alt='AtCoder DP A' />
<hr>

<p>
There are <code>N</code> stones in a line.
</p>

<p>
For each stone <code>i</code>, the height is <code>h[i]</code>.
</p>

<p>
A frog starts from stone <code>1</code> and wants to reach stone <code>N</code>.
</p>

<p>
The frog can:
</p>

<ul>
<li>Jump from stone <code>i</code> to <code>i+1</code></li>
<li>Jump from stone <code>i</code> to <code>i+2</code></li>
</ul>

<p>
The cost of a jump is:
</p>

<p>
<code>|h[i] - h[j]|</code>
</p>

<p>
Find the minimum total cost to reach the last stone.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b>
4
10 30 40 20

<b>Output:</b>
30
</pre>

<pre>
<b>Input:</b>
2
10 10

<b>Output:</b>
0
</pre>

<hr>

<h3>Constraints:</h3>

<ul>
<li><code>2 ≤ N ≤ 100000</code></li>
<li><code>1 ≤ h[i] ≤ 10000</code></li>
</ul>

<hr>

<h3>Approach (Dynamic Programming):</h3>

<p>
For every stone, we calculate the minimum cost needed to reach it.
</p>

<p>
The frog can arrive at stone <code>i</code> from:
</p>

<ul>
<li>Stone <code>i-1</code></li>
<li>Stone <code>i-2</code></li>
</ul>

<p>
So:
</p>

<p>
<code>
dp[i] = min(
dp[i-1] + |h[i] - h[i-1]|,
dp[i-2] + |h[i] - h[i-2]|
)
</code>
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Create a DP array</li>

<li>Set:
    <ul>
        <li><code>dp[0] = 0</code></li>
    </ul>
</li>

<li>For each stone:
    <ul>
        <li>Try jumping from previous stone</li>
        <li>Try jumping from two stones back</li>
    </ul>
</li>

<li>Store the minimum cost</li>

<li>Return <code>dp[n-1]</code></li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
To reach any stone optimally, we only need the best answers for previous stones.
</p>

<p>
Dynamic Programming avoids recalculating the same states again and again.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>

<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>

<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>

<p>Dynamic Programming</p>