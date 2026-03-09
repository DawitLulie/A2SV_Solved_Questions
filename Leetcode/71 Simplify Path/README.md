<h2><a href="https://leetcode.com/problems/simplify-path">71. Simplify Path</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>Given a string <code>path</code>, which is an <strong>absolute path</strong> (starting with a slash <code>'/'</code>) to a file or directory in a Unix-style file system, convert it to the <strong>simplified canonical path</strong>.</p>

<p>In a Unix-style file system:</p>

<ul>
<li><code>.</code> refers to the current directory.</li>
<li><code>..</code> refers to the parent directory.</li>
<li>Multiple consecutive slashes (<code>//</code>) are treated as a single slash.</li>
<li>Any other name refers to a directory.</li>
</ul>

<p>The canonical path should follow these rules:</p>

<ul>
<li>The path must start with a single slash <code>/</code>.</li>
<li>Directories must be separated by a single slash.</li>
<li>The path must not end with a trailing slash (unless it is the root).</li>
<li>Use the shortest possible path.</li>
</ul>

---

### Example 1

<pre>
Input: path = "/home/"
Output: "/home"
</pre>

### Example 2

<pre>
Input: path = "/../"
Output: "/"
</pre>

### Example 3

<pre>
Input: path = "/home//foo/"
Output: "/home/foo"
</pre>

### Example 4

<pre>
Input: path = "/a/./b/../../c/"
Output: "/c"
</pre>

---

### Constraints

<ul>
<li>1 ≤ path.length ≤ 3000</li>
<li>path consists of English letters, digits, period <code>'.'</code>, slash <code>'/'</code>, and underscore <code>'_'</code>.</li>
<li>path is a valid absolute Unix path.</li>
</ul>

---

### Solution

**Approach (Stack):**

We process each directory in the path and simulate navigation using a **stack**.

Steps:

1. Split the path using `'/'`.
2. Traverse each component:
   - Ignore empty strings (`""`) and `"."` because they represent the current directory.
   - If the component is `".."`, pop from the stack (go to the parent directory) if possible.
   - Otherwise, push the directory name onto the stack.
3. Join the stack elements with `'/'` and prepend `'/'` to construct the canonical path.

---

### Complexity

- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)

Where `n` is the length of the path.

---

### Tags

stack, string