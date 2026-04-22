<h2><a href="https://leetcode.com/problems/is-graph-bipartite/">785. Is Graph Bipartite?</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>

<p>
There is an undirected graph with <code>n</code> nodes, where each node is numbered between <code>0</code> and <code>n - 1</code>.
You are given a 2D array <code>graph</code>, where <code>graph[i]</code> is a list of nodes adjacent to node <code>i</code>.
</p>

<p>
Return <code>true</code> if the graph is <b>bipartite</b>, otherwise return <code>false</code>.
</p>

<p>
A graph is bipartite if we can divide the nodes into two groups such that:
<ul>
<li>No two adjacent nodes are in the same group</li>
</ul>
</p>

<hr>

<h3>Examples:</h3>

<pre>
<b>Input:</b> graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
<b>Output:</b> false
</pre>

<pre>
<b>Input:</b> graph = [[1,3],[0,2],[1,3],[0,2]]
<b>Output:</b> true
</pre>

<hr>

<h3>Constraints:</h3>
<ul>
<li><code>1 ≤ graph.length ≤ 100</code></li>
<li><code>0 ≤ graph[i].length &lt; n</code></li>
<li><code>graph[i]</code> does not contain <code>i</code></li>
<li>All values of <code>graph[i]</code> are unique</li>
<li>The graph is undirected</li>
</ul>

<hr>

<h3>Approach (DFS Coloring):</h3>

<p>
We try to color the graph using two colors: <code>0</code> and <code>1</code>.
</p>

<ul>
<li>If two connected nodes have the same color → not bipartite</li>
<li>If we can color all nodes without conflict → bipartite</li>
</ul>

<hr>

<h3>Steps:</h3>

<ol>
<li>Create a <code>color</code> array initialized with <code>-1</code> (not colored)</li>
<li>Loop through each node (to handle disconnected graphs)</li>
<li>If node is not colored:
    <ul>
        <li>Assign a color (0)</li>
        <li>Start DFS</li>
    </ul>
</li>
<li>In DFS:
    <ul>
        <li>For each neighbor:
            <ul>
                <li>If not colored → give opposite color</li>
                <li>If same color → return false</li>
            </ul>
        </li>
    </ul>
</li>
<li>If no conflict found → return true</li>
</ol>

<hr>

<h3>Why This Works:</h3>

<p>
A bipartite graph means no odd-length cycles.
</p>

<p>
By coloring alternately, we ensure:
<ul>
<li>Neighbors always have different colors</li>
<li>If conflict appears → graph is not bipartite</li>
</ul>
</p>

<hr>

<h3>⏱️ Time Complexity:</h3>
<p><code>O(V + E)</code></p>

<h3>💾 Space Complexity:</h3>
<p><code>O(V)</code></p>

<hr>

<h3>🏷️ Tags:</h3>
<p>Graph, DFS, BFS, Coloring</p>