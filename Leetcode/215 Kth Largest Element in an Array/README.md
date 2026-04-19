<h2><a href="https://leetcode.com/problems/kth-largest-element-in-an-array">215. Kth Largest Element in an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<h3>📌 Problem Summary</h3>
<p>
You are given an array of integers <code>nums</code> and an integer <code>k</code>.
</p>

<p>
Your task is to find the <b>kth largest element</b> in the array.
</p>

<p>
⚠️ Important:
<ul>
<li>This is based on <b>sorted order</b>, not distinct elements</li>
<li>Duplicates are counted normally</li>
</ul>
</p>

<hr>

<h3>🧠 Intuition</h3>

<p>
Instead of sorting the array (which takes <code>O(n log n)</code>), we try something smarter.
</p>

<p>
We do <b>binary search on the answer</b>.
</p>

<p>
That means:
</p>

<ul>
<li>We guess a value <code>mid</code></li>
<li>Then we check: how many numbers are ≥ <code>mid</code>?</li>
</ul>

<p>
This tells us whether our guess is too small or too large.
</p>

<hr>

<h3>🔍 Key Idea</h3>

<p>
We want to find the <b>largest number</b> such that:
</p>

<pre>
at least k numbers are ≥ that number
</pre>

<p>
This exactly matches the definition of kth largest.
</p>

<hr>

<h3>⚙️ Step-by-Step Approach</h3>

<ol>
<li>Initialize:
    <ul>
        <li><code>low = min(nums)</code></li>
        <li><code>high = max(nums)</code></li>
    </ul>
</li>

<li>Repeat while <code>low ≤ high</code>:
    <ul>
        <li>Compute <code>mid</code></li>
        <li>Count how many numbers are ≥ <code>mid</code></li>
    </ul>
</li>

<li>Decision:
    <ul>
        <li>If count < k → too few numbers → move left (<code>high = mid - 1</code>)</li>
        <li>If count ≥ k → valid → try bigger (<code>low = mid + 1</code>)</li>
    </ul>
</li>

<li>Final Answer:
    <ul>
        <li>Return <code>high</code></li>
    </ul>
</li>
</ol>

<hr>

<h3>📊 Example Walkthrough</h3>

<pre>
nums = [3,2,1,5,6,4], k = 2
</pre>

<p>
Sorted: <code>[6,5,4,3,2,1]</code>
</p>

<p>
Answer should be: <b>5</b>
</p>

<p>
Binary search process:
</p>

<ul>
<li>mid = 3 → count ≥3 = 4 → valid → go right</li>
<li>mid = 5 → count ≥5 = 2 → valid → go right</li>
<li>mid = 6 → count ≥6 = 1 → too small → go left</li>
</ul>

<p>
Final answer = <b>5</b>
</p>

<hr>

<h3>💡 Why This Approach Works</h3>

<p>
We are not searching for index, but for a <b>value</b>.
</p>

<p>
Binary search works because:
</p>

<ul>
<li>If a value works → smaller values also work</li>
<li>If a value fails → larger values will also fail</li>
</ul>

<p>
So the answer space is <b>monotonic</b>, which allows binary search.
</p>

<hr>

<h3>⚠️ Common Mistakes</h3>

<ul>
<li>Confusing kth largest with kth smallest</li>
<li>Using <code>&gt;</code> instead of <code>≥</code></li>
<li>Returning <code>low</code> instead of <code>high</code></li>
<li>Forgetting duplicates</li>
</ul>

<hr>

<h3>🚀 Alternative Approaches</h3>

<h4>1. Sorting</h4>
<ul>
<li>Sort descending and return <code>nums[k-1]</code></li>
<li>Time: <code>O(n log n)</code></li>
</ul>

<h4>2. Min Heap</h4>
<ul>
<li>Keep heap of size k</li>
<li>Time: <code>O(n log k)</code></li>
</ul>

<h4>3. Quickselect (Best)</h4>
<ul>
<li>Average: <code>O(n)</code></li>
<li>Most optimal for interviews</li>
</ul>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n log(max - min))</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(1)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Binary Search, Array, Selection Algorithm</p>