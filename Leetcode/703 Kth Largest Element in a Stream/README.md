<h2><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/">703. Kth Largest Element in a Stream</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Easy-green" alt="Difficulty: Easy" />

<hr>

<h3>Problem Statement</h3>

<p>
Design a class to find the <code>kth</code> largest element in a stream.
</p>

<p>
You are given an integer <code>k</code> and an integer array <code>nums</code>.
</p>

<p>
Implement the following:
</p>

<ul>
<li><code>KthLargest(int k, int[] nums)</code> initializes the object</li>
<li><code>add(int val)</code> adds a new value to the stream and returns the kth largest element</li>
</ul>

<hr>

<h3>Example:</h3>

<pre>
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4,5,8,2]], [3], [5], [10], [9], [4]]

Output:
[null, 4, 5, 5, 8, 8]
</pre>

<hr>

<h3>Constraints:</h3>

<ul>
<li><code>1 ≤ k ≤ 10⁴</code></li>
<li><code>0 ≤ nums.length ≤ 10⁴</code></li>
<li><code>-10⁴ ≤ nums[i] ≤ 10⁴</code></li>
<li><code>-10⁴ ≤ val ≤ 10⁴</code></li>
<li>At most <code>10⁴</code> calls will be made to add</li>
</ul>

<hr>

<h3>Approach (Min Heap)</h3>

<p>
We maintain a min heap of size <code>k</code>.
</p>

<p>
The heap always stores the largest <code>k</code> elements seen so far.
</p>

<ul>
<li>The smallest value inside the heap will be the kth largest element</li>
<li>So the answer is always at <code>heap[0]</code></li>
</ul>

<hr>

<h3>Step-by-Step</h3>

<ol>
<li>Create a min heap</li>
<li>Insert all initial numbers</li>
<li>If heap size becomes larger than <code>k</code>, remove the smallest</li>
<li>For every new value:
    <ul>
        <li>Push into heap</li>
        <li>If size exceeds <code>k</code>, pop one element</li>
    </ul>
</li>
<li>Return <code>heap[0]</code></li>
</ol>

<hr>

<h3>Why This Works</h3>

<p>
The heap only keeps the largest <code>k</code> elements.
</p>

<p>
Among those elements,
the smallest one is exactly the kth largest element overall.
</p>

<hr>

<h3>⏱️ Time Complexity</h3>

<p>
Each <code>add()</code> operation:
<code>O(log k)</code>
</p>

<hr>

<h3>💾 Space Complexity</h3>

<p>
<code>O(k)</code>
</p>

<hr>

<h3>🏷️ Tags</h3>

<p>
Heap, Priority Queue, Design
</p>