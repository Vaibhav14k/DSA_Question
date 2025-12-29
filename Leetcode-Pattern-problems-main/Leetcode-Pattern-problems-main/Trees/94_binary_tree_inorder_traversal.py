from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def inorder(Node):
            if Node is None:
                return []
            return inorder(Node.left) + [Node.val] + inorder(Node.right)
        return inorder(root)

    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack = []
        result = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result

obj = Solution()
print(obj.inorderTraversal(TreeNode()))