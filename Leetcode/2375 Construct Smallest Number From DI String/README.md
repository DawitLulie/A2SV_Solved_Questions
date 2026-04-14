<h2><a href="https://leetcode.com/problems/construct-smallest-number-from-di-string">2375. Construct Smallest Number From DI String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />

<hr/>

<h3>🧩 Problem Description</h3>
<p>
You are given a string <b>pattern</b> consisting of <b>'I'</b> (increasing) and <b>'D'</b> (decreasing).
</p>

<p>
Construct the <b>smallest number</b> using digits from <b>1 to 9</b> (without repetition) such that:
</p>

<ul>
<li>'I' → next digit is greater</li>
<li>'D' → next digit is smaller</li>
</ul>

<hr/>

<h3>📌 Examples</h3>

<pre>
Input: pattern = "IIIDIDDD"
Output: "123549876"
</pre>

<pre>
Input: pattern = "DDD"
Output: "4321"
</pre>

<hr/>

<h3>📊 Constraints</h3>
<ul>
<li>1 ≤ pattern.length ≤ 8</li>
<li>pattern consists only of 'I' and 'D'</li>
</ul>

<hr/>

<h3>💡 Intuition (Backtracking)</h3>

<p>
We try <b>all possible permutations</b> of digits from <b>1 to n+1</b>, and pick the smallest valid one.
</p>

<p>
At each step:
</p>
<ul>
<li>Choose a digit that is not used</li>
<li>Check if it satisfies the pattern ('I' or 'D')</li>
<li>Continue building the number</li>
</ul>

<p>
👉 This guarantees we find the <b>smallest valid number</b>.
</p>

<hr/>

<h3>🚀 Approach (Step-by-Step)</h3>

<ol>
<li>Create list of digits from 1 to n+1</li>
<li>Use a <b>used[]</b> array to track visited digits</li>
<li>Use backtracking to build the number</li>
<li>At each step:
  <ul>
    <li>If digit already used → skip</li>
    <li>If pattern condition fails → skip</li>
  </ul>
</li>
<li>When length becomes n+1:
  <ul>
    <li>Compare with current result</li>
    <li>Store the smallest one</li>
  </ul>
</li>
</ol>

<hr/>

<h3> Why This Works</h3>

<ul>
<li>We explore all valid permutations</li>
<li>We only keep the smallest answer</li>
<li>Constraints are small (n ≤ 8), so this is efficient</li>
</ul>

<hr/>

<h3>⏱ Complexity</h3>

<ul>
<li><b>Time Complexity:</b> O((n+1)!)</li>
<li><b>Space Complexity:</b> O(n)</li>
</ul>

<hr/>

