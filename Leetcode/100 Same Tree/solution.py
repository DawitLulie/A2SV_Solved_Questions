class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.arr1 = []
        self.arr2 = []

        def dfs(node, arr):
            if not node:
                arr.append(node)
                return 

            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
            
            return arr

        return  dfs(p, self.arr1) == dfs(q, self.arr2)



            
        