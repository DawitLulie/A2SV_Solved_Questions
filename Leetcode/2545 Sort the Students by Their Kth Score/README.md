<h2><a href="https://leetcode.com/problems/sort-the-students-by-their-kth-score">2545. Sort the Students by Their Kth Score</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>You are given a 2D integer array <code>score</code> where <code>score[i]</code> is the list of scores of the <code>i<sup>th</sup> student in all subjects.  
You are also given an integer <code>k</code>.</p>

<p>Sort the students by their score in the <strong>k<sup>th</sup> subject</strong> in decreasing order, and return the resulting array.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2
Output: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
Explanation:
The 2nd index (0-based) scores are: [9,11,3] → sorted: [11,9,3]
Students are reordered accordingly.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: score = [[3,4],[5,1],[10,9]], k = 0
Output: [[10,9],[5,1],[3,4]]
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ score.length ≤ 250</li>
  <li><code>score[i].length == m</li>
  <li>1 ≤ m ≤ 100</li>
  <li><code>0 ≤ score[i][j] ≤ 100</code></li>
  <li>0 ≤ k < m</li>
</ul>

---

###  Solution

**Approach:**  
- Sort the array of students by the <code>k<sup>th</sup></code> score in **descending order**.  
- Use the built-in sort function with a custom key:  
  <pre>
  key=lambda student: student[k]
  </pre>  
  and set `reverse=True`.

**Complexity:**  
- Time: O(n log n) — sorting n students  
- Space: O(1) extra (ignoring output)  

---