class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [-float('inf')]
        def pathsum(root):
            if root is None:
                return 0
            left_sum = max(pathsum(root.left),0)
            right_sum = max(pathsum(root.right),0)
            res[0] = max(res[0],root.val+left_sum+right_sum)
            print("left-->",left_sum)
            print("right-->",right_sum)
            print("sum-->",root.val+left_sum+right_sum)
            return root.val + max(left_sum,right_sum)
        pathsum(root)
        return res[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

obj = Solution()
print(obj.maxPathSum(root))