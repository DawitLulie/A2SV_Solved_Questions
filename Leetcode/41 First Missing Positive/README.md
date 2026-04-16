<h2><a href="https://leetcode.com/problems/first-missing-positive">41. First Missing Positive</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
Given an unsorted integer array <code>nums</code>, return the smallest missing positive integer.
</p>

<p>
You must implement an algorithm that runs in <b>O(n)</b> time and uses <b>constant extra space</b>.
</p>

<hr>

<h3>🔹 Examples:</h3>

<pre>
<b>Input:</b> nums = [1,2,0]
<b>Output:</b> 3
</pre>

<pre>
<b>Input:</b> nums = [3,4,-1,1]
<b>Output:</b> 2
</pre>

<pre>
<b>Input:</b> nums = [7,8,9,11,12]
<b>Output:</b> 1
</pre>

<hr>

<h3>🔹 Constraints:</h3>
<ul>
<li><code>1 ≤ nums.length ≤ 10⁵</code></li>
<li><code>-2³¹ ≤ nums[i] ≤ 2³¹ - 1</code></li>
</ul>

<hr>

<h3> Approach (Cyclic Sort Idea):</h3>

<p>
We want to place each number in its correct position:
</p>

<ul>
<li>Number <code>1</code> → index <code>0</code></li>
<li>Number <code>2</code> → index <code>1</code></li>
<li>Number <code>n</code> → index <code>n-1</code></li>
</ul>

<p>
Steps:
</p>

<ol>
<li>Iterate through the array.</li>
<li>For each number, keep swapping it to its correct position:
    <ul>
        <li>Ignore numbers ≤ 0 or > n</li>
        <li>Swap only if it's not already in the correct place</li>
    </ul>
</li>
<li>After placement, scan the array:
    <ul>
        <li>First index where <code>nums[i] != i + 1</code> → answer is <code>i + 1</code></li>
    </ul>
</li>
<li>If all positions are correct → answer is <code>n + 1</code></li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
We rearrange the array so that each number is at its correct index.
</p>

<p>
After that:
</p>
<ul>
<li>If a number is missing, its position will be incorrect</li>
<li>The first mismatch gives the answer</li>
</ul>

<p>
This avoids extra space and keeps the solution O(n).
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n)</code> — each element is swapped at most once</p>

<h3> Space Complexity:</h3>
<p><code>O(1)</code> — in-place modification</p>

<hr>

<h3> Tags:</h3>
<p>Array, Hashing, Cyclic Sort</p>