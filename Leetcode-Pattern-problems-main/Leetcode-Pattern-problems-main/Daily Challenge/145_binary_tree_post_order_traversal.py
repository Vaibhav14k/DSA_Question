# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,root):
        if root is None:
            return []
        return self.solve(root.left) + self.solve(root.right) + [root.val]
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        return self.solve(root)
