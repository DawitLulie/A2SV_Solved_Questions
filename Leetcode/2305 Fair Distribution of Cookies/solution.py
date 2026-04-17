from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # Sort in descending order → helps pruning faster
        cookies.sort(reverse=True)

        # Each child’s current total cookies
        children = [0] * k

        # Our answer (minimum unfairness)
        self.best = float('inf')

        def backtrack(index):
            # If all cookies are assigned
            if index == len(cookies):
                # unfairness = max cookies any child has
                self.best = min(self.best, max(children))
                return

            # Try giving current cookie to each child
            for i in range(k):
                # Assign cookie
                children[i] += cookies[index]

                # Prune: if already worse than best, stop exploring
                if children[i] < self.best:
                    backtrack(index + 1)

                # Undo assignment (backtrack)
                children[i] -= cookies[index]

                # Optimization: avoid duplicate states
                # If this child had 0 before assignment,
                # no need to try other empty children
                if children[i] == 0:
                    break

        backtrack(0)
        return self.best