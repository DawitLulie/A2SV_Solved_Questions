# [78. Subsets](https://leetcode.com/problems/subsets)
![Difficulty: Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Given an integer array `nums` of unique elements, return **all possible subsets** (the power set). The solution set must not contain duplicate subsets. You can return the solution in any order.

---

## Example 1

Input: nums = [1,2,3]  
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]  
Explanation: All possible subsets of [1,2,3] are listed above.

## Example 2

Input: nums = [0]  
Output: [[],[0]]

---

## Constraints

- 1 ≤ nums.length ≤ 10
- -10 ≤ nums[i] ≤ 10
- All elements of nums are **unique**

---

# Solution

## Approach (Backtracking / Recursive DFS)

**Key idea:** We can build subsets by **recursively deciding** whether to include each element.

**Steps:**

1. Start with an empty subset `[]`.
2. At each step, choose the current element to **include** or **exclude**.
3. Recursively move to the next element.
4. Add each generated subset to the result list.

**Backtracking version:**

- Maintain a current path (subset).  
- Explore all possibilities by including/excluding elements.  
- Pop elements from the path after recursion to backtrack.

---

## Complexity

- **Time Complexity:** O(n * 2^n) — there are 2^n subsets, and each subset can take up to n time to copy.  
- **Space Complexity:** O(n) — recursion stack (path) + O(2^n) for the result.

---

## Tags

backtracking, recursion, subset, dfs, combinatorics