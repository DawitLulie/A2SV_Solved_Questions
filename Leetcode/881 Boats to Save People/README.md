<h2><a href="https://leetcode.com/problems/boats-to-save-people">881. Boats to Save People</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an array <code>people</code> where <code>people[i]</code> represents the weight of the <code>i<sup>th</sup></code> person and an integer <code>limit</code> representing the maximum weight a boat can carry. Each boat can carry at most **two people** at the same time, provided the sum of their weights is at most <code>limit</code>. Return the minimum number of boats to carry every person.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat can carry both people (1+2 ≤ 3).
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: Boats can be [1,2], [2], [3].
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: people = [3,5,3,4], limit = 5
Output: 4
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ people.length ≤ 5 × 10⁴</li>
  <li>1 ≤ people[i] ≤ limit ≤ 3 × 10⁴</li>
</ul>

---

###  Solution

**Approach (Greedy, Two-pointers):**  
1. Sort the `people` array.  
2. Initialize two pointers: `i = 0` (lightest) and `j = n-1` (heaviest).  
3. While `i ≤ j`:
   - If `people[i] + people[j] ≤ limit`, place both in one boat (`i++`, `j--`).  
   - Else, put only the heavier person (`j--`).  
   - Increment boat count.  
4. Return the total boats used.

**Why this works:**  
- Always pairing the heaviest remaining person with the lightest maximizes the chance of carrying two people per boat.

**Complexity:**  
- Time: O(n log n) — sorting  
- Space: O(1) extra  

---