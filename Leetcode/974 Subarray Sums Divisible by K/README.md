<h2><a href="https://leetcode.com/problems/subarray-sums-divisible-by-k">974. Subarray Sums Divisible by K</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the number of non-empty subarrays that have a sum divisible by <code>k</code>.</p>

<p>A <strong>subarray</strong> is a contiguous part of an array.</p>

---

### Example 1

<pre>
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
</pre>

### Example 2

<pre>
Input: nums = [5], k = 9
Output: 0
</pre>

---

### Constraints

<ul>
<li>1 ≤ nums.length ≤ 3 * 10⁴</li>
<li>-10⁴ ≤ nums[i] ≤ 10⁴</li>
<li>2 ≤ k ≤ 10⁴</li>
</ul>

---

### Solution

**Approach (Prefix Sum + Hash Map)**

We use prefix sums and store the remainder of the sum when divided by <code>k</code>.

Key idea:

If two prefix sums have the same remainder when divided by <code>k</code>, the subarray between them is divisible by <code>k</code>.

Example:

If  
<pre>
prefix1 % k = r
prefix2 % k = r
</pre>

Then

<pre>
(prefix2 - prefix1) % k = 0
</pre>

So the subarray between them has a sum divisible by <code>k</code>.

Steps:

1. Keep a running prefix sum.
2. Compute the remainder:  
   <pre>
   remainder = prefix_sum % k
   </pre>
3. If the same remainder appeared before, it means a valid subarray exists.
4. Count how many times each remainder appears using a dictionary.

We initialize the dictionary with:

<pre>
{0: 1}
</pre>

This handles cases where the prefix sum itself is divisible by <code>k</code>.

---

### Complexity

- **Time:** O(n)  
- **Space:** O(k)

---

### Tags

prefix sum, hash table