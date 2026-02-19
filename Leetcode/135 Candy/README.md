<h2><a href="https://leetcode.com/problems/candy">135. Candy</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' />
<hr>

<p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following rules:</p>
<ul>
  <li>Each child must have at least one candy.</li>
  <li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>Return the minimum number of candies you need to distribute.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the children as [2,1,2].
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the children as [1,2,1].
The third child gets 1 candy because it is not higher than its left neighbor.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>n == ratings.length</li>
  <li>1 &lt;= n &lt;= 2 * 10⁴</li>
  <li>0 &lt;= ratings[i] &lt;= 2 * 10⁴</li>
</ul>

---

### Solution

**Approach:**  
- Initialize an array <code>candies</code> with 1 candy for each child.  
- Traverse from left to right: if the current child has a higher rating than the previous, give one more candy than the previous.  
- Traverse from right to left: if the current child has a higher rating than the next, update the candies to be the max of current and next + 1.  
- Sum all candies.

**Complexity:**  
- Time: O(n) — two passes through the array  
- Space: O(n) — for the candies array  

---
