<h2><a href="https://codeforces.com/problemset/problem/2126/D">2126D. This Is the Last Time</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1200-yellow' alt='Difficulty: 1200' />
<hr>

<p>You are given <strong>n casinos</strong> numbered from <code>1</code> to <code>n</code>. Each casino has three integers: <code>l<sub>i</sub></code>, <code>r<sub>i</sub></code>, and <code>real<sub>i</sub></code> (with <code>l<sub>i</sub> ≤ real<sub>i</sub> ≤ r<sub>i</sub></code>). You start with <code>k</code> coins.</p>

<p>You can play at casino <code>i</code> only if your current number of coins <code>x</code> satisfies <code>l<sub>i</sub> ≤ x ≤ r<sub>i</sub></code>. After playing, your number of coins becomes <code>real<sub>i</sub></code>.  
You can visit the casinos in any order, and you are not required to visit all of them. Each casino can be played at most once.</p>

<p>Your task is to find the <strong>maximum final number of coins</strong> you can obtain after optimally choosing which casinos to visit.</p>

<p><strong>Example Input:</strong></p>
<pre>
5
3 1
2 3 3
1 2 2
3 10 10
1 0
1 2 2
1 2
1 2 2
2 2
1 3 2
2 4 4
2 5
1 10 5
3 6 5
</pre>

<p><strong>Example Output:</strong></p>
<pre>
10
0
2
4
5
</pre>

<p><strong>Explanation:</strong></p>
<p>In the first test case, you can visit casino 2 first (coins become 2), then casino 1 (coins become 3), and finally casino 3 (coins become 10), giving the maximum final coins.</p>

<p><strong>Constraints:</strong></p>
<ul>
  <li><code>1 ≤ t ≤ 10⁴</code></li>
  <li><code>1 ≤ n ≤ 10⁵</code></li>
  <li><code>0 ≤ k ≤ 10⁹</code></li>
  <li><code>0 ≤ l<sub>i</sub> ≤ real<sub>i</sub> ≤ r<sub>i</sub> ≤ 10⁹</code></li>
  <li>The sum of <code>n</code> over all test cases does not exceed <code>10⁵</code>.</li>
</ul>

---

###  Solution

**Approach:**  
- Sort the casinos by their minimum requirement <code>l<sub>i</sub></code>.  
- Iterate over the sorted list and at any point where your current coins fall into the valid range <code>[l<sub>i</sub>, r<sub>i</sub>]</code>, update your coins to <code>real<sub>i</sub></code>.  
- Use a greedy strategy to always play at every accessible casino as soon as possible.

**Complexity:**  
- Time: <code>O(n log n)</code> — for sorting each test case  
- Space: <code>O(1)</code> additional (ignoring input storage)  

---

###  Tags

data structures, greedy, sortings :contentReference[oaicite:0]{index=0}
