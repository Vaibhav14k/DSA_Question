# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right  

class Solution:
    def solve(self,node,target):
        if not node:
            return False
        if not node.left and not node.right and node.val == target:
            return True
        return self.solve(node.left,target-node.val) or self.solve(node.right,target-node.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.solve(root,targetSum)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
obj = Solution()
print(obj.hasPathSum(root, 8))  