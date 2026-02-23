<h2><a href="https://codeforces.com/problemset/problem/2174/A">A. Needle in a Haystack</a></h2>
<img src='https://img.shields.io/badge/Difficulty-1300-orange' alt='Difficulty: 1300' />
<hr>

<p>You are given a string <code>s</code> and another string <code>t</code>, both consisting of lowercase English letters.</p>

<p>You may reorder (shuffle) the letters of <code>t</code>. Your goal is to make <code>s</code> appear at least once as a <strong>subsequence</strong> of the reordered string.</p>

<p>Among all valid reorderings, return the <strong>lexicographically smallest</strong> one.</p>

<p>If it is impossible, print <code>"Impossible"</code>.</p>

---

### 🔹 Definitions

- A string <code>a</code> is a subsequence of <code>b</code> if we can delete some characters from <code>b</code> (possibly none) to obtain <code>a</code>.
- A string is lexicographically smaller if:
  - It is a prefix of the other, or  
  - At the first different position, it has a smaller character.

---

### 🔹 Key Observations

1. If `t` does not contain enough letters to build `s`, answer is `"Impossible"`.

2. To make `s` a subsequence, we must:
   - Reserve the letters of `s`
   - Use the remaining letters freely

3. To get lexicographically smallest result:
   - Sort remaining letters
   - Insert `s` in the best position

---

###  Optimal Strategy

1. Count frequency of letters in `t`.
2. Subtract frequency of letters in `s`.
   - If any count becomes negative → print `"Impossible"`.
3. Build answer carefully:
   - We want the smallest lexicographic order.
   - Try placing `s` between smaller characters properly.

Important trick:
If `s[0]` exists multiple times in remaining letters, we must decide whether:
- Put all smaller letters first
- Then maybe some equal letters
- Then `s`
- Then remaining letters

Correct method:
- Collect all letters smaller than `s[0]`
- Then compare placing `s` before or after equal letters
- Choose smaller result

---

### ⏱ Complexity

- Time: O(n + 26) per test case
- Space: O(26)

---

### 📌 Example

Input: