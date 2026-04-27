<h2><a href="https://leetcode.com/problems/employee-importance">690. Employee Importance</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>
You are given a list of employees, where each employee has:
</p>

<ul>
<li><code>id</code>: unique ID</li>
<li><code>importance</code>: their value</li>
<li><code>subordinates</code>: list of IDs of direct subordinates</li>
</ul>

<p>
Return the total importance of an employee and all of their subordinates (direct + indirect).
</p>

<hr>

<h3>Example:</h3>

<pre>
<b>Input:</b>
employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]]
id = 1

<b>Output:</b> 11
</pre>

<hr>

<h3>Approach (DFS + Array Mapping):</h3>

<p>
Instead of using a hashmap, we use arrays to store:
</p>

<ul>
<li><code>val[i]</code> → importance of employee <code>i</code></li>
<li><code>graph[i]</code> → list of subordinates of employee <code>i</code></li>
</ul>

<p>
Since employee IDs may not be continuous, we first find the maximum ID and create arrays of size <code>n + 1</code>.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Find the maximum employee ID</li>
<li>Create:
    <ul>
        <li><code>val</code> array to store importance</li>
        <li><code>graph</code> adjacency list for subordinates</li>
    </ul>
</li>

<li>Fill both arrays using the input</li>

<li>Run DFS starting from the given <code>id</code>:
    <ul>
        <li>Add current employee importance</li>
        <li>Visit all subordinates recursively</li>
    </ul>
</li>

<li>Store result in a global variable</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
We convert the input into a graph-like structure using arrays.
DFS ensures we visit every subordinate exactly once and accumulate the total importance.
</p>

<p>
Using arrays instead of hashmap can be faster due to constant-time indexing.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>DFS, Graph, Array</p>