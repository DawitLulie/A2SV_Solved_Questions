<h2><a href="https://leetcode.com/problems/last-stone-weight">1046. Last Stone Weight</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>
You are given an array of integers <code>stones</code> where each integer represents the weight of a stone.
</p>

<p>
We are playing a game where, at each turn, we pick the two heaviest stones and smash them together:
</p>

<ul>
<li>If the stones have equal weight, both are destroyed.</li>
<li>If they are different, the smaller one is destroyed and the larger one is reduced by the smaller weight.</li>
</ul>

<p>
Return the weight of the last remaining stone, or 0 if no stones remain.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> stones = [2,7,4,1,8,1]
<b>Output:</b> 1
<b>Explanation:</b>
7 + 8 → 1 remains → final answer is 1
</pre>

<pre>
<b>Input:</b> stones = [1]
<b>Output:</b> 1
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li>1 ≤ stones.length ≤ 30</li>
<li>1 ≤ stones[i] ≤ 1000</li>
</ul>

<hr>

<h3>Approach (Max Heap):</h3>

<p>
We always need the two largest stones efficiently, so we use a <b>max heap</b>.
Since Python has a min heap, we store negative values to simulate a max heap.
</p>

<h3>Steps:</h3>

<ol>
<li>Insert all stones into a heap (as negative values)</li>
<li>While heap has more than 1 stone:</li>
<ul>
<li>Pop two largest stones</li>
<li>If they are not equal, push their difference back</li>
</ul>
<li>Return last stone or 0</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Using a heap ensures we always pick the two heaviest stones in <code>O(log n)</code> time.
This matches the problem requirement efficiently.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n log n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Heap, Greedy, Priority Queue</p>