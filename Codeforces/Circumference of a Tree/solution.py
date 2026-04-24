import sys
from collections import deque

input = sys.stdin.readline
n = int(input().strip())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(node):

    visited = [False] * (n + 1)
    queue = deque([(node, 0)])
    visited[node] = True
    last = (node, 0)

    while queue:
        node = queue.popleft()
        level = node[1]
        for nei in graph[node[0]]:
            if not visited[nei]:
                queue.append((nei, level + 1))
                visited[nei] = True
                last = (nei, level + 1)

    return last


val = bfs(1)
result = bfs(val[0])
print(result[1] * 3)
