<h2><a href="https://leetcode.com/problems/top-k-frequent-words/">692. Top K Frequent Words</a></h2>
<img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty: Medium"/>
<hr>

<p>
Given an array of strings <code>words</code> and an integer <code>k</code>, return the <code>k</code> most frequent strings.
</p>

<p>
The answer should be sorted by frequency from highest to lowest. If two words have the same frequency, sort them lexicographically.
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> words = ["i","love","leetcode","i","love","coding"], k = 2
<b>Output:</b> ["i","love"]
</pre>

<pre>
<b>Input:</b> words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
<b>Output:</b> ["the","is","sunny","day"]
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li>1 ≤ words.length ≤ 500</li>
<li>1 ≤ words[i].length ≤ 10</li>
<li><code>words[i]</code> consists of lowercase English letters.</li>
<li><code>k</code> is in the range <code>[1, the number of unique words]</code></li>
</ul>

<hr>

<h3>Approach (HashMap + Min Heap):</h3>

<p>
We first count the frequency of each word using a hashmap, then use a heap to keep the top k frequent words.
</p>

<p>
We use a <b>min heap</b> so that the smallest frequency (or lexicographically larger word in case of tie) can be removed easily when size exceeds k.
</p>

<hr>

<h3>Steps:</h3>

<ol>
<li>Count frequency of each word using <code>Counter</code></li>
<li>Push each (frequency, word) into a heap</li>
<li>Sort using:
    <ul>
        <li>Higher frequency first</li>
        <li>If tie → lexicographically smaller word first</li>
    </ul>
</li>
<li>Keep heap size ≤ k</li>
<li>Extract results from heap</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
The heap ensures we always keep only the top k elements efficiently without sorting the full list.
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(n log k)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(n)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Heap, HashMap, Sorting, Bucket Sort</p>