<h2><a href="https://leetcode.com/problems/count-of-smaller-numbers-after-self">315. Count of Smaller Numbers After Self</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>
Given an integer array <code>nums</code>, return an integer array <code>counts</code> where 
<code>counts[i]</code> is the number of smaller elements to the right of <code>nums[i]</code>.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> nums = [5,2,6,1]
<b>Output:</b> [2,1,1,0]
</pre>

<pre>
<b>Input:</b> nums = [-1]
<b>Output:</b> [0]
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>1 ≤ nums.length ≤ 10⁵</code></li>
<li><code>-10⁴ ≤ nums[i] ≤ 10⁴</code></li>
</ul>

<hr>

<h3>Approach (Merge Sort):</h3>

<p>
We use a modified merge sort to count smaller elements efficiently.
</p>

<ul>
<li>Keep track of original indices</li>
<li>While merging:
    <ul>
        <li>If right element is smaller → increase counter</li>
        <li>If left element is placed → add count</li>
    </ul>
</li>
</ul>

<hr>

<h3>Steps:</h3>

<ol>
<li>Store elements as (value, index)</li>
<li>Apply merge sort</li>
<li>During merge:
    <ul>
        <li>If left value ≤ right → add current count to result</li>
        <li>Else → increment count</li>
    </ul>
</li>
<li>Return result array</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
Merge sort naturally compares left and right halves.
</p>

<p>
We use this property to count how many smaller elements come after each number.
</p>

<p>
This avoids brute force <code>O(n²)</code>.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n log n)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Merge Sort, Divide and Conquer, Array</p>