<h1 align="center">2226. Maximum Candies Allocated to K Children</h1>

<p align="center">
<b>Difficulty:</b> Medium
</p>

---

## Problem Link
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

---

## Problem Summary

You are given:
- An array `candies[]` where each element represents a pile of candies.
- An integer `k` representing the number of children.

You need to:
- Divide candies into equal portions.
- Each child must receive the same number of candies.
- You can split piles, but you cannot combine them.

Return the maximum number of candies each child can get.

---

## Examples

Example 1:
Input: candies = [5,8,6], k = 3  
Output: 5  

Example 2:
Input: candies = [2,5], k = 11  
Output: 0  

---

## Constraints

- 1 <= candies.length <= 10^5  
- 1 <= candies[i] <= 10^7  
- 1 <= k <= 10^12  

---

## Approach (Binary Search)

This problem is solved using binary search on the answer.

Step 1: Define search range  
- Minimum candies per child = 1  
- Maximum candies = max(candies)  

Step 2: Check if a value works  
For a given value `mid`, calculate how many children can be served:

total_children = sum(candy // mid for candy in candies)

- If total_children >= k → valid  
- Otherwise → invalid  

Step 3: Binary search  
- If valid → try a larger value  
- If not valid → try a smaller value  

---

## Why This Works

The answer is monotonic:
- If a value works, all smaller values also work.
- If a value does not work, all larger values will also not work.

This allows the use of binary search.

---

## Time Complexity

O(n log M)  
where M = max(candies)

---

## Space Complexity

O(1)

---

## Tags

Binary Search  
Greedy  