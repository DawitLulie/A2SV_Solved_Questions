<h2><a href="https://codeforces.com/problemset/problem/1741/D">1741D. Masha and a Beautiful Tree</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: 1300' />
<hr>

<p>
Masha has an array representation of a binary tree. A tree is considered <b>beautiful</b> if:
</p>

<ul>
<li>Size = 1 → always beautiful</li>
<li>Otherwise:
    <ul>
        <li>Both halves are beautiful</li>
        <li>All elements in the left half are strictly less than those in the right half</li>
    </ul>
</li>
</ul>

<p>
You can only perform one operation:
<b>swap the left and right halves</b>.
</p>

<p>
Return the <b>minimum number of swaps</b> required, or <code>-1</code> if impossible.
</p>

<hr>

<h3>🔹 Example:</h3>

<pre>
<b>Input:</b>
1
4
3 1 2 4

<b>Output:</b>
1
</pre>

<hr>

<h3> Approach (Merge Sort Style):</h3>

<p>
We solve this problem using a <b>modified merge sort</b>.
</p>

<p>
Instead of sorting normally, we:
</p>

<ul>
<li>Divide the array into two halves</li>
<li>Recursively process each half</li>
<li>During merge, decide whether to swap halves</li>
</ul>

<hr>

<h3>🔧 Merge Logic:</h3>

<p>
At each merge step:
</p>

<ul>
<li>If <code>left[0] &lt; right[0]</code> → keep order</li>
<li>Otherwise → swap halves and increase operation count</li>
</ul>

<p>
This works because:
</p>

<ul>
<li>Each half is already processed (like sorted segments)</li>
<li>We only need to decide correct ordering between halves</li>
</ul>

<hr>

<h3> Final Check:</h3>

<p>
After full merging:
</p>

<ul>
<li>Verify the array is strictly increasing</li>
<li>If not → return <code>-1</code></li>
</ul>

<hr>

<h3> Why This Works:</h3>

<p>
This approach mimics building the beautiful tree:
</p>

<ul>
<li>Each recursive call ensures smaller segments are valid</li>
<li>Merge step ensures correct relative ordering</li>
<li>Swaps simulate flipping tree nodes</li>
</ul>

<p>
If the final array is not strictly increasing, it means no sequence of swaps can fix it.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n log n)</code> — due to merge sort recursion</p>

<h3> Space Complexity:</h3>
<p><code>O(n)</code> — due to array slicing and merging</p>

<hr>

<h3> Tags:</h3>
<p>Divide and Conquer, Merge Sort, Greedy</p>