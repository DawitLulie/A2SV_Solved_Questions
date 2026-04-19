<h2><a href="https://leetcode.com/problems/sort-colors">75. Sort Colors</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
</p>

<p>
We use integers <code>0, 1, 2</code> to represent red, white, and blue respectively.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> nums = [2,0,2,1,1,0]
<b>Output:</b> [0,0,1,1,2,2]
</pre>

<pre>
<b>Input:</b> nums = [2,0,1]
<b>Output:</b> [0,1,2]
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>n == nums.length</code></li>
<li><code>1 ≤ n ≤ 300</code></li>
<li><code>nums[i] ∈ {0,1,2}</code></li>
</ul>

<hr>

<h3>Approach (Dutch National Flag Algorithm):</h3>

<p>
We use three pointers to sort the array in one pass.
</p>

<ul>
<li><b>low</b> → position for 0</li>
<li><b>mid</b> → current index</li>
<li><b>high</b> → position for 2</li>
</ul>

<hr>

<h3>Steps:</h3>

<ol>
<li>Initialize <code>low = 0</code>, <code>mid = 0</code>, <code>high = n - 1</code></li>
<li>While <code>mid ≤ high</code>:
    <ul>
        <li>If <code>nums[mid] == 0</code> → swap with low, move both forward</li>
        <li>If <code>nums[mid] == 1</code> → move mid</li>
        <li>If <code>nums[mid] == 2</code> → swap with high, move high backward</li>
    </ul>
</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
We separate the array into three regions in a single traversal.
</p>

<p>
Each element is processed at most once → optimal sorting.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(1)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Array, Two Pointers, Sorting</p>