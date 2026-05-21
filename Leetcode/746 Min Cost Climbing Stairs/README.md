<h2><a href="https://leetcode.com/problems/min-cost-climbing-stairs/">746. Min Cost Climbing Stairs</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Easy-green" alt="Difficulty: Easy" />

<hr>

<h3>📌 Problem Summary</h3>

<p>
You are given an integer array <code>cost</code> where:
</p>

<ul>
<li><code>cost[i]</code> is the cost of stepping on the <code>i-th</code> stair.</li>
</ul>

<p>
After paying the cost, you can either:
</p>

<ul>
<li>climb one stair</li>
<li>or climb two stairs</li>
</ul>

<p>
You can start from step <code>0</code> or step <code>1</code>.
</p>

<p>
Return the minimum cost to reach the top of the floor.
</p>

<hr>

<h3>🧪 Examples</h3>

<pre>
<b>Input:</b>
cost = [10,15,20]

<b>Output:</b>
15

<b>Explanation:</b>
Start at index 1 and pay 15.
</pre>

<pre>
<b>Input:</b>
cost = [1,100,1,1,1,100,1,1,100,1]

<b>Output:</b>
6
</pre>

<hr>

<h3>📋 Constraints</h3>

<ul>
<li><code>2 ≤ cost.length ≤ 1000</code></li>
<li><code>0 ≤ cost[i] ≤ 999</code></li>
</ul>

<hr>

<h3>💡 Approach (Dynamic Programming)</h3>

<p>
We use Dynamic Programming because the same subproblems appear many times.
</p>

<p>
Let:
</p>

<pre>
dp(i)
</pre>

<p>
represent the minimum cost needed to reach the top starting from index <code>i</code>.
</p>

<hr>

<h3>🔄 Transition</h3>

<p>
From any stair, we can:
</p>

<ul>
<li>move 1 step</li>
<li>or move 2 steps</li>
</ul>

<p>
So:
</p>

<pre>
cost[i] + min(dp(i + 1), dp(i + 2))
</pre>

<hr>

<h3>🪜 Steps</h3>

<ol>
<li>Create a memoization dictionary</li>
<li>Use recursion to calculate minimum cost</li>
<li>If we go beyond the array:
    <ul>
        <li>return 0</li>
    </ul>
</li>
<li>Store computed states in memo</li>
<li>Return the minimum of:
    <ul>
        <li>starting from index 0</li>
        <li>starting from index 1</li>
    </ul>
</li>
</ol>

<hr>

<h3>✅ Why This Works</h3>

<p>
At every stair, we choose the cheaper path between:
</p>

<ul>
<li>taking one step</li>
<li>taking two steps</li>
</ul>

<p>
Memoization avoids recalculating the same states repeatedly.
</p>

<hr>

<h3>⏱️ Time Complexity</h3>

<p>
<code>O(n)</code>
</p>

<hr>

<h3>💾 Space Complexity</h3>

<p>
<code>O(n)</code>
</p>

<hr>

<h3>🏷️ Tags</h3>

<p>
Dynamic Programming, Recursion, Memoization
</p>