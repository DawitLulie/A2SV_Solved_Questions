<h2><a href="https://leetcode.com/problems/two-city-scheduling">1029. Two City Scheduling</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>A company is planning to interview <code>2n</code> people. You are given an array <code>costs</code> where <code>costs[i] = [aCost, bCost]</code>, the cost of flying the <code>i-th</code> person to city A is <code>aCost</code>, and the cost of flying them to city B is <code>bCost</code>.</p>

<p>Return the <strong>minimum cost</strong> to fly every person to a city such that exactly <code>n</code> people arrive in each city.</p>

---

### Example 1

<pre>
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
Send person 1 to city A (10)
Send person 2 to city A (30)
Send person 3 to city B (50)
Send person 4 to city B (20)

Total cost = 10 + 30 + 50 + 20 = 110
</pre>

### Example 2

<pre>
Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
</pre>

---

### Constraints

<ul>
<li>2n == costs.length</li>
<li>2 ≤ costs.length ≤ 100</li>
<li>costs.length is even</li>
<li>1 ≤ aCost, bCost ≤ 1000</li>
</ul>

---

# Solution

### Approach (Greedy + Sorting)

The key idea is to decide which people should go to city A and which should go to city B while minimizing the total cost.

For each person we calculate the difference between the costs of flying to the two cities:

<code>diff = bCost - aCost</code>

This tells us how beneficial it is to send a person to city B instead of city A.

Steps:

1. Sort the people by the difference <code>(bCost - aCost)</code>.
2. Send the first <code>n</code> people (who benefit most from city B) to city B.
3. Send the remaining <code>n</code> people to city A.
4. Sum the corresponding costs.

This greedy strategy ensures the minimum total cost.

---

### Complexity

- <strong>Time Complexity:</strong> O(n log n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

greedy, sorting, array