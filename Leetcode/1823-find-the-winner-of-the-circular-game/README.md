# 1823. Find the Winner of the Circular Game

## Problem
There are `n` friends standing in a circle, numbered from `1` to `n`.

Starting from friend `1`, we count `k` people in order. The `k-th` person is removed from the circle.

After each removal, counting continues from the next person in the circle.

The process repeats until only one person remains.

Return the winner.

---

## Example
Input:
n = 5, k = 2

Output:
3

Explanation:
Start: 1 2 3 4 5  
Remove 2 → 1 3 4 5  
Remove 4 → 1 3 5  
Remove 1 → 3 5  
Remove 5 → 3  
Winner = 3

---

## Approach 1: Simulation using Queue

We use a queue to simulate the circular process.

### Steps:
1. Put all numbers from 1 to n into a queue.
2. Repeat until one element remains:
   - Move first `k-1` elements to the back.
   - Remove the front element (this is the k-th person).
3. Return the last remaining element.

---

## Complexity
Time: O(n × k)  
Space: O(n)

---

## Approach 2: Josephus Problem (Optimal)

This is a classic Josephus problem.

We use the formula:
f(n, k) = (f(n-1, k) + k) % n

Base case:
f(1, k) = 0

Final answer:
f(n, k) + 1

---

## Optimized Solution
Time: O(n)  
Space: O(1)

---

## Code (O(n))
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0

        for i in range(2, n + 1):
            winner = (winner + k) % i

        return winner + 1

---

## Summary
- Simulation is easy to understand.
- Josephus solution is optimal and interview-ready.