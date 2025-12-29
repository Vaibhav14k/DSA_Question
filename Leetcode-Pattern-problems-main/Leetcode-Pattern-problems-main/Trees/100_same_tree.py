class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

obj = Solution()
print(obj.isSameTree(root,root)) 