<h2><a href="https://leetcode.com/problems/combination-sum-ii">40. Combination Sum II</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a collection of candidate numbers <code>candidates</code> and a target number <code>target</code>, find all unique combinations in <code>candidates</code> where the candidate numbers sum to <code>target</code>. Each number in <code>candidates</code> may only be used once in the combination.</p>

<h3>Examples:</h3>

<pre><strong>Example 1:</strong>
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

<strong>Example 2:</strong>
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
</pre>

<h3>Constraints:</h3>
<ul>
<li>1 <= candidates.length <= 100</li>
<li>1 <= candidates[i] <= 50</li>
<li>1 <= target <= 30</li>
</ul>

<h3>Approach:</h3>
<p>This problem is solved using <strong>backtracking</strong>. The steps are:</p>
<ol>
<li>Sort the candidates. This helps in skipping duplicates easily.</li>
<li>Use a recursive function to explore all possible combinations:</li>
<ul>
<li>At each step, iterate through candidates starting from the current index.</li>
<li>If the current candidate is the same as the previous one (and not the first in this loop), skip it to avoid duplicate combinations.</li>
<li>Add the candidate to the current combination.</li>
<li>Recursively call the function with updated target (target - candidate) and next index (i + 1, because each number can only be used once).</li>
<li>Backtrack by removing the last added candidate to try the next possibility.</li>
</ul>
<li>If the target becomes zero, the current combination is valid and added to the result.</li>
</ol>

<h3>Why this works:</h3>
<p>By sorting and skipping duplicates, we ensure each combination is unique. Backtracking explores all valid combinations without missing any, while pruning branches where the target is exceeded.</p>

<h3>Time Complexity:</h3>
<p>O(2^n), because in the worst case we explore every subset of candidates.</p>

<h3>Space Complexity:</h3>
<p>O(n) for recursion stack and temporary combination storage.</p>