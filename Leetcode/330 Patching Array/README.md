<h2><a href="https://leetcode.com/problems/patching-array/">330. Patching Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
Given a sorted integer array <code>nums</code> and an integer <code>n</code>, add the minimum number of patches such that any number in the range <code>[1, n]</code> can be formed as the sum of elements in the array.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> nums = [1,3], n = 6
<b>Output:</b> 1
<b>Explanation:</b> Add 2 → now we can form [1..6]
</pre>

<pre>
<b>Input:</b> nums = [1,5,10], n = 20
<b>Output:</b> 2
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>1 ≤ nums.length ≤ 1000</code></li>
<li><code>1 ≤ nums[i] ≤ 10⁴</code></li>
<li><code>nums</code> is sorted in ascending order</li>
<li><code>1 ≤ n ≤ 2³¹ - 1</code></li>
</ul>

<hr>

<h3>💡 Key Idea (Greedy):</h3>

<p>
We track the smallest number <b>miss</b> that we <b>cannot</b> form yet.
</p>

<ul>
<li>If we can form all values in <code>[1, miss-1]</code></li>
<li>Then:
  <ul>
    <li>If next number ≤ miss → we extend range</li>
    <li>Else → we must patch with <code>miss</code></li>
  </ul>
</li>
</ul>

<hr>

<h3>🔍 Why Patch with <code>miss</code>?</h3>

<p>
Because:
</p>

<ul>
<li>Current coverage: <code>[1, miss-1]</code></li>
<li>Adding <code>miss</code> gives coverage:</li>
</ul>

<pre>
[1, miss-1] + miss → [1, 2*miss - 1]
</pre>

<p>
This is the <b>maximum extension</b> possible with one number.
</p>

<hr>

<h3>🚶 Step-by-Step:</h3>

<ol>
<li>Initialize:
  <ul>
    <li><code>miss = 1</code></li>
    <li><code>i = 0</code></li>
  </ul>
</li>

<li>While <code>miss ≤ n</code>:
  <ul>
    <li>If <code>i &lt; len(nums)</code> and <code>nums[i] ≤ miss</code>:
      <ul>
        <li>Use it → <code>miss += nums[i]</code></li>
        <li><code>i++</code></li>
      </ul>
    </li>
    <li>Else:
      <ul>
        <li>Patch with <code>miss</code></li>
        <li><code>miss += miss</code></li>
      </ul>
    </li>
  </ul>
</li>

</ol>

<hr>

<h3>🧠 Why This Works:</h3>

<p>
We always cover the largest possible range with the minimum patches.
</p>

<p>
This greedy choice is optimal because any smaller patch gives less coverage.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(len(nums))</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(1)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Greedy, Array</p>