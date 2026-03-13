<h2><a href="https://leetcode.com/problems/lemonade-change">860. Lemonade Change</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />
<hr>

<p>At a lemonade stand, each lemonade costs <code>$5</code>. Customers are standing in a queue to buy from you and order one at a time.</p>

<p>Each customer will pay with a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <code>$5</code>.</p>

<p>Return <code>true</code> if you can provide every customer with the correct change, otherwise return <code>false</code>.</p>

---

### Example 1

<pre>
Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers we collect three $5 bills.
From the fourth customer we collect a $10 bill and give back a $5.
From the fifth customer we give a $10 and a $5.
</pre>

### Example 2

<pre>
Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers we collect two $5 bills.
For the next two customers we give change with $5 bills.
For the last customer we cannot give the required change.
</pre>

---

### Constraints

<ul>
<li>1 ≤ bills.length ≤ 10⁵</li>
<li>bills[i] is either 5, 10, or 20</li>
</ul>

---

# Solution

### Approach (Greedy + Counter)

We simulate the process of giving change.

Key ideas:

- A $5 bill needs no change.
- A $10 bill needs one $5 bill as change.
- A $20 bill needs either:
  - $10 + $5, or
  - three $5 bills.

Steps:

1. Use a <code>Counter</code> to track how many $5 and $10 bills we have.
2. Iterate through each bill in the array.
3. If the bill is $10:
   - We must give one $5 bill.
4. If the bill is $20:
   - Prefer giving $10 + $5 if possible.
   - Otherwise give three $5 bills.
5. If we cannot give change at any step, return <code>False</code>.

If all customers are served successfully, return <code>True</code>.

---

### Complexity

- <strong>Time Complexity:</strong> O(n)  
- <strong>Space Complexity:</strong> O(1)

---

### Tags

greedy, simulation, hash table