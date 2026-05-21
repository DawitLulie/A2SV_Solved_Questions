<h2><a href="https://leetcode.com/problems/house-robber/">198. House Robber</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium" />

<hr>

<h3>📌 Problem Summary</h3>

<p>
You are a robber planning to rob houses along a street.
</p>

<p>
Each house has some amount of money stored.
</p>

<p>
The only constraint is:
</p>

<ul>
<li>You cannot rob two adjacent houses.</li>
</ul>

<p>
Return the maximum amount of money you can rob without alerting the police.
</p>

<hr>

<h3>🧪 Examples</h3>

<pre>
<b>Input:</b>
nums = [1,2,3,1]

<b>Output:</b>
4

<b>Explanation:</b>
Rob house 1 and house 3.
1 + 3 = 4
</pre>

<pre>
<b>Input:</b>
nums = [2,7,9,3,1]

<b>Output:</b>
12

<b>Explanation:</b>
Rob houses 1, 3, and 5.
2 + 9 + 1 = 12
</pre>

<hr>

<h3>📋 Constraints</h3>

<ul>
<li><code>1 ≤ nums.length ≤ 100</code></li>
<li><code>0 ≤ nums[i] ≤ 400</code></li>
</ul>

<hr>

<h3>💡 Approach (Dynamic Programming)</h3>

<p>
This is a classic Dynamic Programming problem.
</p>

<p>
At every house, we have two choices:
</p>

<ul>
<li>Rob the current house</li>
<li>Skip the current house</li>
</ul>

<p>
Let:
</p>

<pre>
dp(i)
</pre>

<p>
represent the maximum money we can rob starting from index <code>i</code>.
</p>

<hr>

<h3>🔄 Transition</h3>

<p>
If we rob the current house:
</p>

<pre>
nums[i] + dp(i + 2)
</pre>

<p>
If we skip the current house:
</p>

<pre>
dp(i + 1)
</pre>

<p>
Take the maximum:
</p>

<pre>
max(nums[i] + dp(i + 2), dp(i + 1))
</pre>

<hr>

<h3>🪜 Steps</h3>

<ol>
<li>Create a memoization dictionary</li>
<li>Use recursion with DP</li>
<li>If index goes out of bounds:
    <ul>
        <li>return 0</li>
    </ul>
</li>
<li>At each house:
    <ul>
        <li>choose rob or skip</li>
    </ul>
</li>
<li>Store computed results in memo</li>
</ol>

<hr>

<h3>✅ Why This Works</h3>

<p>
For every house, we explore all valid choices:
</p>

<ul>
<li>Rob it and skip the next house</li>
<li>Skip it and move to the next house</li>
</ul>

<p>
Memoization prevents repeated calculations and makes the solution efficient.
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