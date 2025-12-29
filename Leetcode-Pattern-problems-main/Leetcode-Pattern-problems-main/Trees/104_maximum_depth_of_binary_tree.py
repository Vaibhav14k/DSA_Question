from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1'''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.depth = -1
        def dfs(node,depth):
            if node.left is None and node.right is None:
                self.depth = max(self.depth,depth)
            if node.left:
                dfs(node.left,depth+1)
            if node.right:
                dfs(node.right,depth+1)
        dfs(root,1)
        return self.depth

