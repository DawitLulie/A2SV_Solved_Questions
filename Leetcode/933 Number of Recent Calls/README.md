<h2><a href="https://leetcode.com/problems/number-of-recent-calls">933. Number of Recent Calls</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>You have a <code>RecentCounter</code> class which counts the number of recent requests within a certain time frame.</p>

<p>Implement the <code>RecentCounter</code> class:</p>

<ul>
<li><code>RecentCounter()</code> Initializes the counter with zero recent requests.</li>
<li><code>int ping(int t)</code> Adds a new request at time <code>t</code>, where <code>t</code> represents some time in milliseconds, and returns the number of requests that has happened in the past <code>3000</code> milliseconds (including the new request).</li>
</ul>

<p>Specifically, return the number of requests that have happened in the inclusive range <code>[t - 3000, t]</code>.</p>

<p>It is guaranteed that every call to <code>ping</code> uses a strictly larger value of <code>t</code> than the previous call.</p>

---

### Example

<pre>
Input
["RecentCounter","ping","ping","ping","ping"]
[[],[1],[100],[3001],[3002]]

Output
[null,1,2,3,3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1,100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1,100,3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1,100,3001,3002], range is [2,3002], return 3
</pre>

---

### Constraints

<ul>
<li>1 ≤ t ≤ 10⁹</li>
<li>Each test case will call <code>ping</code> at most 10⁴ times.</li>
<li>Each call to <code>ping</code> will have a strictly larger <code>t</code> than the previous call.</li>
</ul>

---

### Solution

**Approach (Queue):**

We maintain a **queue** storing the timestamps of recent requests.

Steps:

1. When `ping(t)` is called:
   - Add `t` to the queue.
2. Remove timestamps from the front of the queue while they are **less than `t - 3000`**.
3. The remaining timestamps are within the valid range `[t - 3000, t]`.
4. Return the size of the queue.

Since timestamps always increase, we only remove outdated requests once.

---

### Complexity

- **Time Complexity:** O(1) amortized per operation  
- **Space Complexity:** O(n)

Where `n` is the number of pings within the last 3000 milliseconds.

---

### Tags

queue, design, sliding window