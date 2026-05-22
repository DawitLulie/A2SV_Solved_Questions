<h2><a href="https://leetcode.com/problems/house-robber-ii/">213. House Robber II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
You are a professional robber planning to rob houses along a street.
</p>

<p>
All houses are arranged in a circle.
</p>

<p>
That means:
</p>

<ul>
<li>The first house is adjacent to the last house</li>
<li>You cannot rob two adjacent houses</li>
</ul>

<p>
Return the maximum amount of money you can rob without alerting the police.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> nums = [2,3,2]
<b>Output:</b> 3
</pre>

<pre>
<b>Input:</b> nums = [1,2,3,1]
<b>Output:</b> 4
</pre>

<pre>
<b>Input:</b> nums = [1,2,3]
<b>Output:</b> 3
</pre>

<hr>

<h3>Constraints:</h3>

<ul>
<li><code>1 <= nums.length <= 100</code></li>
<li><code>0 <= nums[i] <= 1000</code></li>
</ul>

<hr>

<h3>Approach (Dynamic Programming):</h3>

<p>
This problem is similar to House Robber I, but now the houses form a circle.
</p>

<p>
Because the first and last houses are adjacent, we cannot rob both.
</p>

<p>
So we split the problem into two cases:
</p>

<ul>
<li>Rob houses from index <code>0 → n-2</code></li>
<li>Rob houses from index <code>1 → n-1</code></li>
</ul>

<p>
Then take the maximum result from those two cases.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>If there is only one house, return its value</li>

<li>Create a helper function for normal House Robber logic</li>

<li>Run the helper on:
    <ul>
        <li><code>nums[:-1]</code></li>
        <li><code>nums[1:]</code></li>
    </ul>
</li>

<li>Return the maximum of the two results</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Since the first and last houses cannot both be robbed, every valid solution must exclude one of them.
</p>

<p>
By checking both possibilities separately, we guarantee the best possible answer.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>

<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>

<p><code>O(1)</code></p>

<hr>

<h3>🏷️ Tags:</h3>

<p>Dynamic Programming, Array</p>