class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node:
                arr.append("#")
                return

            arr.append("," + str(node.val))

            dfs(node.left, arr)
            dfs(node.right, arr)
        
        arr1 = []
        arr2 = []

        dfs(subRoot, arr1)
        dfs(root, arr2)

        arr1 = "".join(arr1)
        arr2 = "".join(arr2)
        
        return arr1 in arr2



            
        