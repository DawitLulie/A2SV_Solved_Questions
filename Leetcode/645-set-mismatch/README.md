<h2><a href="https://leetcode.com/problems/set-mismatch/">645. Set Mismatch</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<h3> Problem Statement</h3>
<p>
You are given an integer array <code>nums</code> containing numbers from <code>1</code> to <code>n</code>.
Exactly one number is <b>duplicated</b> and one number is <b>missing</b>.
</p>

<p>
Return the duplicated number and the missing number as an array <code>[duplicate, missing]</code>.
</p>

<hr>

<h3> Intuition</h3>
<p>
Since the numbers should be from 1 to n, we can track how many times each number appears.
</p>

<p>
- The number appearing twice is the <b>duplicate</b>  
- The number not appearing at all is the <b>missing</b>
</p>

<hr>

<h3> Approach</h3>

<ol>
  <li>Create a frequency array of size n+1</li>
  <li>Count occurrences of each number</li>
  <li>Scan from 1 to n:
    <ul>
      <li>If freq[i] == 2 → duplicate</li>
      <li>If freq[i] == 0 → missing</li>
    </ul>
  </li>
</ol>

<hr>

<h3>⏱ Complexity Analysis</h3>

<ul>
  <li><b>Time Complexity:</b> O(n)</li>
  <li><b>Space Complexity:</b> O(n)</li>
</ul>

<hr>

<h3> Summary</h3>
<p>
We use a simple counting method to detect both the repeated and missing numbers efficiently in linear time.
</p>