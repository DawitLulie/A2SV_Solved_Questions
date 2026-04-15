<h2><a href="https://leetcode.com/problems/find-all-duplicates-in-an-array/">442. Find All Duplicates in an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3> Problem Statement</h3>
<p>
Given an integer array <code>nums</code> of length <code>n</code> where all the integers are in the range <code>[1, n]</code>,
each integer appears once or twice.
</p>

<p>
Return an array of all the integers that appear <b>twice</b>.
</p>

<p>
You must solve the problem <b>without using extra space</b> and in <b>O(n)</b> time.
</p>

<hr>

<h3> Intuition</h3>
<p>
Since values are in the range <code>[1, n]</code>, we can use the array itself to track visited numbers.
</p>

<p>
For each number <code>x</code>, we mark index <code>abs(x) - 1</code> as negative.
</p>

<ul>
  <li>If it's already negative → we have seen it before → it's a duplicate</li>
</ul>

<hr>

<h3> Approach</h3>

<ol>
  <li>Initialize an empty result list</li>
  <li>Iterate through the array</li>
  <li>For each number:
    <ul>
      <li>Find index = abs(num) - 1</li>
      <li>If nums[index] is negative → add to result</li>
      <li>Else → mark nums[index] as negative</li>
    </ul>
  </li>
  <li>Return result</li>
</ol>

<hr>

<h3>⏱ Complexity Analysis</h3>

<ul>
  <li><b>Time Complexity:</b> O(n)</li>
  <li><b>Space Complexity:</b> O(1) (excluding output)</li>
</ul>

<hr>

<h3> Key Insight</h3>
<p>
We use the input array itself as a hash map by marking visited indices negative.
This avoids extra space usage.
</p>