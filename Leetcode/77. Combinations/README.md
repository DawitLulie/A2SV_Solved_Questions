# [77. Combinations](https://leetcode.com/problems/combinations)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Given two integers `n` and `k`, return **all possible combinations** of `k` numbers out of the range `[1, n]`. You may return the answer in any order.

---

## Example 1

Input: n = 4, k = 2  
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]  
Explanation: All possible 2-number combinations from [1,2,3,4] are listed above.

## Example 2

Input: n = 1, k = 1  
Output: [[1]]

---

## Constraints

- 1 ≤ n ≤ 20
- 1 ≤ k ≤ n

---

# Solution

## Approach (Backtracking / Recursive DFS)

**Key idea:** We can build combinations by **incrementally adding numbers** and backtracking.

**Steps:**

1. Start with an empty combination `[]`.
2. At each step, choose the next number from the current range to include.
3. Recurse to build the combination until its length is `k`.
4. Add the combination to the result list.
5. Backtrack by removing the last number and trying the next candidate.

---

## Complexity

- **Time Complexity:** O(C(n,k) * k) — there are C(n,k) combinations, each of length k.  
- **Space Complexity:** O(k) — recursion stack + O(C(n,k)) for result storage.

---

## Tags

backtracking, recursion, combinatorics, dfs