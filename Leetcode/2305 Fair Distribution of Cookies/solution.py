class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        self.result = float('inf')

        def dfs(index):
            if index == len(cookies):
                self.result = min(self.result, max(children))
                return

            for i in range(k):
                if children[i] + cookies[index] >= self.result:
                    continue

                children[i] += cookies[index]
                dfs(index + 1)
                children[i] -= cookies[index]

                if children[i] == 0:
                    break

        dfs(0)
        return self.result