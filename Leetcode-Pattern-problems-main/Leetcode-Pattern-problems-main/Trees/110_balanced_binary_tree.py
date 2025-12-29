class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def __init__(self) -> None:
        self.maxx = 0
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1
    '''def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        left = self.height(root.left)
        right = self.height(root.right)
        if(abs(left - right) > 1):
            return False
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        if not left or not right:
            return False
        return True'''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            if (left == -1 or right == -1): return -1
            if(abs(left - right) > 1): return -1
            return max(left,right) + 1
        return height(root) != True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)
# root.right.right.right.right = TreeNode(9)

obj = Solution()
print(obj.isBalanced(root)) 