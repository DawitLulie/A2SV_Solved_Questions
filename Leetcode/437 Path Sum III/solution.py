class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = Counter([0])

        self.result = 0

        def dfs(node, cur_sum):
            if not node:
                return

            cur_sum += node.val

            rem = cur_sum - targetSum
            if dic[rem] > 0:
                self.result += dic[rem]

            dic[cur_sum] += 1

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            dic[cur_sum] -= 1
            cur_sum -= node.val

        dfs(root, 0)

        return self.result
