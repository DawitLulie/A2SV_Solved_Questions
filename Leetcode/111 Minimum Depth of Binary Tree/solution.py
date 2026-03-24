class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            depth = 1

            if not left:
                depth += right
                
            elif not right:
                depth += left
                
            else:
                depth += min(left, right)

            return depth
        
        return dfs(root)