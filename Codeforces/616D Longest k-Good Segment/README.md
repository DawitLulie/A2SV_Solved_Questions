<h2><a href="https://codeforces.com/problemset/problem/616/D">616D. Longest k‑Good Segment</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1700-orange' alt='Difficulty: 1700' />
<hr>

<p>You are given an array of <code>n</code> integers <code>a[1…n]</code> and an integer <code>k</code>.  
A segment (contiguous subarray) <code>a[l…r]</code> is called <strong>k‑good</strong> if every distinct number in the segment appears at least <code>k</code> times.</p>

<p>Your task is to find the length of the longest <strong>k‑good segment</strong>.</p>

---

### Input

- The first line contains two integers <code>n</code> and <code>k</code>  
- The second line contains <code>n</code> integers <code>a[i]</code>

Constraints:
<ul>
<li>1 ≤ n ≤ 10⁵</li>
<li>1 ≤ k ≤ n</li>
<li>0 ≤ a[i] ≤ 10⁹</li>
</ul>

---

### Output

- Print one integer — the length of the longest k‑good segment.

---

### Example

```
Input:
7 2
1 2 1 3 1 2 2

Output:
4
```

Explanation: The longest segment where each distinct number appears at least 2 times is **[1,2,1,3,1,2,2]** → the longest valid segment is **[1,2,1,2]** of length 4.

---

### Approach (Two‑Pointers + Frequency Counting)

Use a sliding window to maintain a current segment and track frequencies:

1. Use two pointers `left = 0` and `right = 0`, and a map `freq` to store frequency of elements in the window.
2. Also maintain a counter `bad` for how many distinct elements fail to meet the ≥ k requirement.
3. Expand the window by increasing `right`:
   - Increase `freq[a[right]]`.
   - When a new element appears and `freq[a[right]] < k`, increase `bad`.
   - When an element becomes ≥ k, decrease `bad`.
4. While `bad > 0`, move `left` forward:
   - Decrease `freq[a[left]]`.
   - Update `bad` accordingly.
5. At each step, if `bad == 0`, update the longest segment length:
   - `ans = max(ans, right - left + 1)`

---

### Complexity

- **Time:** O(n) — each pointer moves at most n times  
- **Space:** O(n) — for frequency map
