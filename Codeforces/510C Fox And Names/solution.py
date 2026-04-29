import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]

graph = [[] for _ in range(26)]
incoming = [0] * 26

# Build graph
for i in range(n - 1):
    word1 = words[i]
    word2 = words[i + 1]

    j = 0
    while j < len(word1) and j < len(word2) and word1[j] == word2[j]:
        j += 1

    # Edge case: prefix problem
    if j == len(word2) and len(word1) > len(word2):
        print("Impossible")
        sys.exit()

    if j < len(word1) and j < len(word2):
        u = ord(word1[j]) - 97
        v = ord(word2[j]) - 97
        graph[u].append(v)
        incoming[v] += 1

# Topological Sort
queue = deque()

for i in range(26):
    if incoming[i] == 0:
        queue.append(i)

result = []

while queue:
    node = queue.popleft()
    result.append(chr(node + 97))

    for nei in graph[node]:
        incoming[nei] -= 1
        if incoming[nei] == 0:
            queue.append(nei)

# Check if valid ordering exists
if len(result) == 26:
    print("".join(result))
else:
    print("Impossible")