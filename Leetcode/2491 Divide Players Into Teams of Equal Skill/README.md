<h2><a href="https://leetcode.com/problems/divide-players-into-teams-of-equal-skill">2491. Divide Players Into Teams of Equal Skill</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>You are given an array <code>skill</code> of even length <code>2 * n</code>, where <code>skill[i]</code> represents the skill level of the <code>i<sup>th</sup></code> player. You need to divide these players into <code>n</code> teams of **two players each**, such that the sum of skill levels in each team is equal.</p>

<p>Return the sum of the **product of skills** of each team if it is possible to divide players into such teams. If it is impossible, return <code>-1</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation:
- Pair (3,4) → 3*4 = 12
- Pair (2,5) → 2*5 = 10
- Pair (1,3) → 1*3 = 3
Sum = 12 + 10 + 0 = 22
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: skill = [3,4]
Output: 12
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 ≤ skill.length ≤ 10⁵</li>
  <li>skill.length is even</li>
  <li>1 ≤ skill[i] ≤ 10⁵</li>
</ul>

---

###  Solution

**Approach (Greedy + Two-pointers):**  
1. Sort the `skill` array.  
2. Compute the target team sum as `skill[0] + skill[-1]`.  
3. Pair the smallest and largest skill players (`left` and `right`) iteratively.  
4. If any pair sum ≠ target, return -1.  
5. Otherwise, accumulate the product of each pair.

**Why this works:**  
- Sorting ensures the largest and smallest players are paired to maintain equal total skill.  
- Greedy pairing guarantees all teams meet the same sum if possible.

**Complexity:**  
- Time: O(n log n) — sorting  
- Space: O(1) extra  

---