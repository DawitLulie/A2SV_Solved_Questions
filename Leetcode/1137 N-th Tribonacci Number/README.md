<h2><a href="https://leetcode.com/problems/n-th-tribonacci-number/">1137. N-th Tribonacci Number</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>
The Tribonacci sequence T<sub>n</sub> is defined as:
</p>

<ul>
<li><code>T0 = 0</code></li>
<li><code>T1 = 1</code></li>
<li><code>T2 = 1</code></li>
</ul>

<p>
For <code>n >= 0</code>:
</p>

<p>
<code>Tn+3 = Tn + Tn+1 + Tn+2</code>
</p>

<p>
Return the value of <code>Tn</code>.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> n = 4
<b>Output:</b> 4

<b>Explanation:</b>
T3 = 0 + 1 + 1 = 2
T4 = 1 + 1 + 2 = 4
</pre>

<pre>
<b>Input:</b> n = 25
<b>Output:</b> 1389537
</pre>

<hr>

<h3>Constraints:</h3>

<ul>
<li><code>0 <= n <= 37</code></li>
<li>The answer is guaranteed to fit within a 32-bit integer.</li>
</ul>

<hr>

<h3>Approach (Dynamic Programming):</h3>

<p>
Each Tribonacci number depends on the previous three numbers.
</p>

<p>
Instead of recalculating values again and again, we store the last three numbers and build the sequence step by step.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Handle the base cases:
    <ul>
        <li>If <code>n = 0</code>, return <code>0</code></li>
        <li>If <code>n = 1</code> or <code>n = 2</code>, return <code>1</code></li>
    </ul>
</li>

<li>Initialize:
    <ul>
        <li><code>a = 0</code></li>
        <li><code>b = 1</code></li>
        <li><code>c = 1</code></li>
    </ul>
</li>

<li>Loop from <code>3</code> to <code>n</code></li>

<li>Compute:
    <br>
    <code>next = a + b + c</code>
</li>

<li>Shift values forward:
    <ul>
        <li><code>a = b</code></li>
        <li><code>b = c</code></li>
        <li><code>c = next</code></li>
    </ul>
</li>

<li>Return <code>c</code></li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Every Tribonacci number only needs the previous three numbers.
</p>

<p>
By updating the values step by step, we generate the sequence efficiently without using extra memory.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>

<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>

<p><code>O(1)</code></p>

<hr>

<h3>🏷️ Tags:</h3>

<p>Dynamic Programming, Math</p>