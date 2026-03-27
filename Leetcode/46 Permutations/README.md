<h2><a href="https://leetcode.com/problems/permutations">46. Permutations</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>

<p>Given an array <code>nums</code> of distinct integers, return <strong>all the possible permutations</strong>. You can return the answer in any order.</p>

<p>A <strong>permutation</strong> is a rearrangement of elements in a particular order.</p>

---

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [1,2,3]
Output: [
 [1,2,3],
 [1,3,2],
 [2,1,3],
 [2,3,1],
 [3,1,2],
 [3,2,1]
]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [0,1]
Output: [[0,1],[1,0]]
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [1]
Output: [[1]]
</pre>

---

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 &lt;= nums.length &lt;= 6</li>
  <li>-10 &lt;= nums[i] &lt;= 10</li>
  <li>All integers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

---

<h3> Intuition</h3>

<p>
To solve this problem, we need to generate <strong>all possible arrangements</strong> of the given numbers.
This is a classic problem where <strong>backtracking</strong> is the best approach.
</p>

<p>
Think of it like this:
At each step, we choose one number and fix it at the current position.
Then we recursively arrange the remaining numbers.
</p>

---

<h3> Approach (Backtracking)</h3>

<p><strong>Step-by-step idea:</strong></p>

<ol>
  <li>Create a result list to store all permutations.</li>
  <li>Use a recursive function to build permutations.</li>
  <li>At each step:
    <ul>
      <li>Loop through all numbers.</li>
      <li>If a number is not already used:
        <ul>
          <li>Add it to the current path.</li>
          <li>Mark it as used.</li>
          <li>Recursively continue building.</li>
          <li>Backtrack (remove it and mark unused).</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>When the current path length equals <code>n</code>, add it to the result.</li>
</ol>

---

<h3>🔁 Why Backtracking Works</h3>

<p>
Backtracking explores all possible choices step by step.
If a path is not complete, it continues exploring.
If a path is complete, it is added to the result.
Then it "goes back" (undoes the last choice) and tries other possibilities.
</p>

<p>
This ensures we generate <strong>all permutations without missing any</strong>.
</p>

---

<h3>⏱️ Complexity Analysis</h3>

<ul>
  <li><strong>Time Complexity:</strong> O(n!)  
    <br>Because there are n! permutations for n numbers.</li>

  <li><strong>Space Complexity:</strong> O(n)  
    <br>For recursion stack and tracking used elements.</li>
</ul>

---

<h3>🏷️ Tags</h3>

<p>Backtracking, Recursion, DFS</p>

---