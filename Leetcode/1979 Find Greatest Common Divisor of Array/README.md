<h2><a href="https://leetcode.com/problems/find-greatest-common-divisor-of-array">1979. Find Greatest Common Divisor of Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an integer array <code>nums</code>, return <em>the greatest common divisor (GCD)</em> of the smallest number and the largest number in <code>nums</code>.</p>

<p>The <strong>GCD</strong> of two numbers is the largest positive integer that divides both numbers.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
Smallest = 2
Largest = 10
GCD(2, 10) = 2
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [7,5,6,8,3]
Output: 1
</pre>

<p><strong>Example 3:</strong></p>
<pre>
Input: nums = [3,3]
Output: 3
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>2 ≤ nums.length ≤ 1000</li>
  <li>1 ≤ nums[i] ≤ 1000</li>
</ul>

---

###  Solution

**Approach:**

1. Find the minimum and maximum values in the array.
2. Compute the GCD of these two numbers using:
   - Euclidean Algorithm  
   - or built-in `math.gcd()` in Python.

**Why it works:**  
The problem specifically asks for the GCD of only the smallest and largest elements — not the whole array.

**Complexity:**

- Time: O(n) — to find min and max  
- GCD computation: O(log(min(a, b)))  
- Space: O(1) extra  

---