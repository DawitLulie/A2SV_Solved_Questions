<h2><a href="https://codeforces.com/problemset/problem/2056/B">2056B. Permutation Construction</a></h2>
<img src='https://img.shields.io/badge/Codeforces-1200-blue' alt='Rating: 1200' />
<hr>

<p>
You are given an integer <code>n</code> and an <code>n × n</code> matrix of characters.
Each row represents constraints for building a permutation.
</p>

<p>
Your task is to construct a permutation of numbers from <code>1</code> to <code>n</code> based on these rules.
</p>

<hr>

<h3>Approach (Greedy + Insertion):</h3>

<p>
We build the permutation step by step using a greedy idea.
</p>

<p>
For each row <code>i</code>, we determine where to insert number <code>i + 1</code> in the current permutation.
</p>

<hr>

<h3>Key Idea:</h3>

<p>
For row <code>i</code>, we look at all previous columns <code>j &lt; i</code>.
</p>

<ul>
<li>If <code>matrix[i][j] == '0'</code>, it means the current number should come <b>before</b> that position</li>
<li>So we shift the insertion index to the left</li>
</ul>

<hr>

<h3>Steps:</h3>

<ol>
<li>Initialize an empty list <code>p</code></li>

<li>For each <code>i</code> from <code>0</code> to <code>n-1</code>:
    <ul>
        <li>Start with <code>index = i</code></li>
        <li>Check all previous positions <code>j &lt; i</code></li>
        <li>If <code>nums[j] == '0'</code>, decrement index</li>
    </ul>
</li>

<li>Insert <code>i + 1</code> into position <code>index</code> in list <code>p</code></li>

<li>Print the final permutation</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Each row gives relative ordering between current element and previous ones.
</p>

<p>
By adjusting the insertion index based on '0's, we ensure:
</p>

<ul>
<li>Correct ordering with already placed elements</li>
<li>Valid permutation construction</li>
</ul>

<p>
This is similar to building a permutation using relative position constraints.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n²)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Greedy, Constructive Algorithms, Implementation</p>