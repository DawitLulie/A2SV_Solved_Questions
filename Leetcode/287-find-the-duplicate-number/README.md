<h2><a href="https://leetcode.com/problems/find-the-duplicate-number/">287. Find the Duplicate Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3> Problem Statement</h3>
<p>
Given an array of integers <code>nums</code> containing <code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.
</p>

<p>
There is only <b>one repeated number</b> in <code>nums</code>, return this repeated number.
</p>

<p>
You must solve the problem <b>without modifying the array</b> and using only <b>constant extra space</b>.
</p>

<hr>

<h3> Intuition</h3>
<p>
We cannot sort or use extra space, so we think differently.
</p>

<p>
We use <b>binary search on the value range</b> (not indices).
</p>

<p>
If we count how many numbers are ≤ mid:
</p>

<ul>
  <li>If count > mid → duplicate is in left half</li>
  <li>Else → duplicate is in right half</li>
</ul>

<p>
This works because of the <b>Pigeonhole Principle</b>.
</p>

<hr>

<h3> Approach</h3>

<ol>
  <li>Set low = 1 and high = n</li>
  <li>While low &lt; high:
    <ul>
      <li>Find mid</li>
      <li>Count numbers ≤ mid</li>
      <li>If count &gt; mid → move left</li>
      <li>Else → move right</li>
    </ul>
  </li>
  <li>Return low (duplicate number)</li>
</ol>

<hr>

<h3>⏱ Complexity Analysis</h3>

<ul>
  <li><b>Time Complexity:</b> O(n log n)</li>
  <li><b>Space Complexity:</b> O(1)</li>
</ul>

<hr>

<h3> Key Insight</h3>
<p>
Instead of searching indices, we search values using counting.
This allows us to find the duplicate without modifying the array.
</p>