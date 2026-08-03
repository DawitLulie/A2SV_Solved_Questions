<h2><a href="https://leetcode.com/problems/stone-game-iii/">1406. Stone Game III</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Hard-red" alt="Difficulty: Hard" />
<hr>

<p>
Alice and Bob are playing a game with a row of stones. Each stone has a value stored in the array <code>stoneValue</code>.
</p>

<p>
Alice always starts first. On each turn, a player can take the first <b>1, 2, or 3</b> remaining stones.
The player's score increases by the sum of the values of the stones they take.
</p>

<p>
Both players play optimally. Return:
</p>

<ul>
<li><code>"Alice"</code> if Alice gets a higher score.</li>
<li><code>"Bob"</code> if Bob gets a higher score.</li>
<li><code>"Tie"</code> if both scores are equal.</li>
</ul>

<hr>

<h3>Example 1</h3>

<pre>
<b>Input:</b> stoneValue = [1,2,3,7]
<b>Output:</b> "Bob"
</pre>

<h3>Example 2</h3>

<pre>
<b>Input:</b> stoneValue = [1,2,3,-9]
<b>Output:</b> "Alice"
</pre>

<h3>Example 3</h3>

<pre>
<b>Input:</b> stoneValue = [1,2,3,6]
<b>Output:</b> "Tie"
</pre>

<hr>

<h3>Constraints</h3>

<ul>
<li><code>1 ≤ stoneValue.length ≤ 5 × 10<sup>4</sup></code></li>
<li><code>-1000 ≤ stoneValue[i] ≤ 1000</code></li>
</ul>

<hr>

<h3>Intuition</h3>

<p>
At first, it may seem that we should calculate Alice's score and Bob's score separately.
However, that becomes difficult because every decision affects the opponent's future choices.
</p>

<p>
Instead, Dynamic Programming focuses on something much simpler:
</p>

<p>
<b>How much better can the current player do compared to the opponent?</b>
</p>

<p>
Let:
</p>

<pre>
dp(i) = maximum score difference the current player can achieve
starting from index i.
</pre>

<p>
The score difference is:
</p>

<pre>
(current player's total score) − (opponent's total score)
</pre>

<p>
This automatically represents both players' scores in one value.
</p>

<hr>

<h3>Approach</h3>

<p>
From every position, the current player has three choices:
</p>

<ul>
<li>Take 1 stone</li>
<li>Take 2 stones</li>
<li>Take 3 stones</li>
</ul>

<p>
Suppose the player takes stones whose sum is <code>take</code>.
After that, the opponent starts from the next position.
</p>

<p>
The opponent can achieve <code>dp(next)</code> score difference.
Since that advantage belongs to the opponent, it becomes a disadvantage for the current player.
</p>

<p>
Therefore:
</p>

<pre>
current difference = take − dp(next)
</pre>

<p>
We compute this for all three choices and keep the maximum.
</p>

<hr>

<h3>Algorithm</h3>

<ol>
<li>Start from the end of the array.</li>
<li>For each index:
<ul>
<li>Try taking 1 stone.</li>
<li>Try taking 2 stones.</li>
<li>Try taking 3 stones.</li>
</ul>
</li>
<li>For every choice:
<pre>
candidate = taken_sum − dp(next_index)
</pre>
</li>
<li>Store the maximum candidate.</li>
<li>Finally:
<ul>
<li>If <code>dp(0) &gt; 0</code>, Alice wins.</li>
<li>If <code>dp(0) &lt; 0</code>, Bob wins.</li>
<li>Otherwise, it is a tie.</li>
</ul>
</li>
</ol>

<hr>

<h3>Why This Works</h3>

<p>
The DP value always stores the maximum score difference the current player can guarantee.
</p>

<p>
Subtracting the opponent's best result correctly models optimal play from both sides.
Because every state depends only on the next three states, we compute the answer efficiently.
</p>

<hr>

<h3>Time Complexity</h3>

<p>
<code>O(n)</code>
</p>

<hr>

<h3>Space Complexity</h3>

<p>
<code>O(n)</code>
</p>

<hr>

<h3>Tags</h3>

<p>
Dynamic Programming, Game Theory, Memoization
</p>