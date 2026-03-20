class Treeroot:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: Optional[Treeroot]) -> int:
        total = 0

        if not root:
            return 0
            
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    total += root.left.left.val

                if root.left.right:
                    total += root.left.right.val


            if root.right:
                if root.right.left:
                    total += root.right.left.val

                if root.right.right:
                    total += root.right.right.val

        left = self.sumEvenGrandparent(root.left)
        right = self.sumEvenGrandparent(root.right)
        
        return total + left + right
        
        