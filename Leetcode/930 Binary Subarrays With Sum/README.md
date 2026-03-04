<h2><a href="https://leetcode.com/problems/binary-subarrays-with-sum">930. Binary Subarrays With Sum</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a binary array <code>nums</code> and an integer <code>goal</code>, return the number of non-empty subarrays with a sum equal to <code>goal</code>.</p>

---

### Example 1

<pre>
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The subarrays are [1,0,1], [0,1,0,1], [1,0,1], [1,0,1]
</pre>

### Example 2

<pre>
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
Explanation: All subarrays of zeros have sum 0.
</pre>

---

### Constraints

<ul>
  <li>1 ≤ nums.length ≤ 3 × 10⁴</li>
  <li>nums[i] is either 0 or 1</li>
  <li>0 ≤ goal ≤ nums.length</li>
</ul>

---

### Solution

**Approach (Prefix Sum + Hash Map):**

1. Initialize a hashmap <code>count</code> with <code>{0:1}</code> to store counts of prefix sums.
2. Iterate through the array, maintain <code>prefix_sum</code>.
3. For each element, check if <code>prefix_sum - goal</code> exists in the hashmap.  
   - If yes, add its count to the result.
4. Increment the count of the current <code>prefix_sum</code> in the hashmap.

**Why this works:**  
- If <code>prefix_sum[j] - prefix_sum[i] = goal</code>, then subarray <code>nums[i..j-1]</code> sums to <code>goal</code>.  
- Hashmap tracks the number of previous prefix sums efficiently.

---

### Complexity

- **Time:** O(n) — single pass through the array  
- **Space:** O(n) — hashmap to store prefix sums

---

### Tags

array, hash map, prefix sum