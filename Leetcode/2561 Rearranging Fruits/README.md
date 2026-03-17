<h2><a href="https://leetcode.com/problems/rearranging-fruits">2561. Rearranging Fruits</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given two integer arrays <code>basket1</code> and <code>basket2</code> representing two baskets of fruits. You want to make both baskets equal by performing some swap operations.</p>

<p>In one operation, you can swap any fruit from <code>basket1</code> with any fruit from <code>basket2</code>. The cost of swapping two fruits with values <code>x</code> and <code>y</code> is <code>min(x, y)</code>.</p>

<p>Return the <strong>minimum total cost</strong> to make the two baskets equal. If it's impossible, return <code>-1</code>.</p>

---

### Example 1

<pre>
Input: basket1 = [1,2,2,2], basket2 = [2,3,3,3]
Output: 2
Explanation: Swap 1 from basket1 with 2 from basket2 at cost min(1,2)=1, 
then swap 2 from basket1 with 3 from basket2 at cost min(2,3)=1. Total cost = 2.
</pre>

### Example 2

<pre>
Input: basket1 = [4,2,2,2], basket2 = [1,4,3,3]
Output: -1
Explanation: It's impossible to make the baskets equal.
</pre>

---

### Constraints

<ul>
<li>1 ≤ basket1.length, basket2.length ≤ 10⁵</li>
<li>1 ≤ basket1[i], basket2[i] ≤ 10⁹</li>
</ul>

---

# Solution

### Approach (Greedy + Counting)

Key idea: Match the frequency of each fruit in both baskets.

1. Count the frequency of each fruit in both baskets.
2. Check for impossibility: if total count of any fruit is odd, return -1.
3. Compute the number of swaps required for each fruit.
4. Sort the list of candidate swaps and use the cheaper option: either swap directly or use the smallest fruit as an intermediary.
5. Sum the minimum costs for all swaps.

This ensures the minimum total swap cost.

---

### Complexity

- **Time Complexity:** O(n log n) due to sorting swaps  
- **Space Complexity:** O(n)

---

### Tags

greedy, hash table, sorting
