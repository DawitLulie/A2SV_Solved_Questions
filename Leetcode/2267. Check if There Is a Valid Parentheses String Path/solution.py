class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        memo = {}

        def dp(x, y, balance):
            if x >= n or y >= m:
                return False

            if grid[x][y] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            if x == n - 1 and y == m - 1:
                return balance == 0

            state = (x, y, balance)

            if state in memo:
                return memo[state]

            memo[state] = (
                dp(x + 1, y, balance) or
                dp(x, y + 1, balance)
            )

            return memo[state]

        if grid[0][0] == ')':
            return False

        if grid[n - 1][m - 1] == '(':
            return False

        if (n + m) % 2 == 0:
            return False

        return dp(0, 0, 0)