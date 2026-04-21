<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays">4. Median of Two Sorted Arrays</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
Given two sorted arrays <code>nums1</code> and <code>nums2</code>, return the median of the combined sorted array.
</p>

<p>
The required time complexity is <code>O(log (m+n))</code>.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> nums1 = [1,3], nums2 = [2]
<b>Output:</b> 2.0
</pre>

<pre>
<b>Input:</b> nums1 = [1,2], nums2 = [3,4]
<b>Output:</b> 2.5
</pre>

<hr>

<h3>Approach (Binary Search on Value):</h3>

<p>
Instead of partitioning arrays, we binary search on the <b>value range</b>.
</p>

<ul>
<li>We try to find the k-th smallest element</li>
<li>Use <code>bisect</code> to count how many elements are ≤ or ≥ a value</li>
<li>This allows us to decide if we need to move left or right</li>
</ul>

<hr>

<h3>Key Idea:</h3>

<p>
Let:
</p>

<ul>
<li><code>k = (n + m - 1) // 2</code> → index of median (0-based)</li>
</ul>

<p>
We find:
</p>

<ul>
<li>Left median → largest number such that count ≤ k</li>
<li>Right median → smallest number such that count ≥ k</li>
</ul>

<p>
Final answer = average of both
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Binary search for left median:
    <ul>
        <li>Count elements smaller than mid using <code>bisect_left</code></li>
        <li>If count &gt; k → move left</li>
        <li>Else → move right</li>
    </ul>
</li>

<li>Binary search for right median:
    <ul>
        <li>Count elements greater than mid using <code>bisect_right</code></li>
        <li>If count &gt; k → move right</li>
        <li>Else → move left</li>
    </ul>
</li>

<li>Take average of both results</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
We are not merging arrays. Instead, we use binary search to directly find the correct value.
</p>

<p>
Using <code>bisect</code>, we efficiently count how many elements satisfy a condition in each array.
</p>

<p>
This allows us to simulate finding the k-th element without actually building the array.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(log(range) * (log m + log n))</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(1)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Binary Search, Array, Bisect</p>