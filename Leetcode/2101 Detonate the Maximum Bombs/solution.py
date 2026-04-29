class Solution:
    def maximumDetonation(self, bombs):
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                dx = bombs[i][0] - bombs[j][0]
                dy = bombs[i][1] - bombs[j][1]

                if dx*dx + dy*dy <= bombs[i][2] * bombs[i][2]:
                    graph[i].append(j)

        def dfs(index, visited):
            visited[index] = True
            count = 1

            for nei in graph[index]:
                if not visited[nei]:
                    count += dfs(nei, visited)

            return count

        result = 0
        for i in range(n):
            visited = [False] * n
            result = max(result, dfs(i, visited))

        return result