<!-- README.md -->

<h2><a href="https://leetcode.com/problems/predict-the-winner">486. Predict the Winner</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />

<hr/>

<h3> Problem Description</h3>
<p>
Two players take turns picking numbers from either the <b>start</b> or <b>end</b> of the array.
</p>

<ul>
<li>Player 1 starts first.</li>
<li>Both players play optimally.</li>
<li>Each tries to maximize their score.</li>
</ul>

<p>
Return <b>true</b> if Player 1 can win or tie.
</p>

<hr/>

<h3> Examples</h3>

<pre>
Input: nums = [1,5,2]
Output: false
</pre>

<pre>
Input: nums = [1,5,233,7]
Output: true
</pre>

<hr/>

<h3> Intuition</h3>

<p>
This solution directly simulates the game using recursion.
</p>

<ul>
<li><b>Player 1</b> tries to maximize score.</li>
<li><b>Player 2</b> tries to minimize Player 1’s score.</li>
</ul>

<p>
So we alternate between <b>max</b> and <b>min</b>.
</p>

<hr/>

<h3> Approach (Minimax Recursion)</h3>

<ol>
<li>Create a function <b>dp(left, right, turn)</b>:
    <ul>
        <li><b>left, right</b> → current range</li>
        <li><b>turn</b> → whose turn (1 = Player 1, 2 = Player 2)</li>
    </ul>
</li>

<li><b>Base case:</b>
<pre>if left > right → return 0</pre>
</li>

<li><b>If Player 1 (turn == 1):</b>
<ul>
<li>Pick left → nums[left] + dp(...)</li>
<li>Pick right → nums[right] + dp(...)</li>
<li>Take <b>max</b></li>
</ul>
</li>

<li><b>If Player 2 (turn == 2):</b>
<ul>
<li>Player 2 does NOT add score</li>
<li>They minimize Player 1’s result</li>
<li>Take <b>min</b></li>
</ul>
</li>

<li>Store result in memo (<b>visited</b>)</li>

<li>Final check:
<pre>Player 1 score >= Player 2 score</pre>
</li>
</ol>

<hr/>

<h3> Why It Works</h3>

<p>
This is a classic <b>minimax</b> problem.
</p>

<ul>
<li>Player 1 tries to maximize score.</li>
<li>Player 2 tries to reduce Player 1’s score.</li>
</ul>

<p>
By switching between <b>max</b> and <b>min</b>, we simulate optimal play.
</p>

<hr/>

<h3>⏱️ Complexity</h3>

<ul>
<li><b>Time:</b> O(n²)</li>
<li><b>Space:</b> O(n²)</li>
</ul>

<hr/>

<h3> Tags</h3>

<p>Recursion, Minimax, Dynamic Programming</p>