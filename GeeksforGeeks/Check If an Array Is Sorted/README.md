<h2><a href="https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1">Check If an Array Is Sorted</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>Given an array of integers, determine whether the array is sorted in non‑decreasing order.</p>

<p>An array is considered sorted if <code>arr[i] ≤ arr[i+1]</code> for every <code>0 ≤ i &lt; n‑1</code>.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input:
n = 5
arr[] = {1, 2, 3, 4, 5}
Output:
Yes
Explanation:
Array is already sorted.
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input:
n = 5
arr[] = {1, 3, 2, 4, 5}
Output:
No
Explanation:
Since 3 &gt; 2, the array is not sorted.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
  <li>1 ≤ n ≤ 10⁵</li>
  <li>−10⁹ ≤ arr[i] ≤ 10⁹</li>
</ul>

---

###  Solution

**Approach:**  
- Traverse the array from left to right.
- Check for any index where <code>arr[i] > arr[i+1]</code>.
- If found, the array is not sorted.
- Otherwise, it is sorted.

**Complexity:**  
- Time: O(n) — one pass through the array  
- Space: O(1) — constant extra space  

---