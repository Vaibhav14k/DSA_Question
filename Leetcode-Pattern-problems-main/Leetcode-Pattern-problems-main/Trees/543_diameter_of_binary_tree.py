class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.maxx = 0
    def height(self,root):
        if root is None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1
    '''def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        l = self.height(root.left)
        print("left height-->",l)
        r = self.height(root.right)
        print("right height-->",r)
        self.maxx = max(l+r,self.maxx)
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        return self.maxx'''
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        self.maxx = max(left+right,self.maxx)
        return 1 + max(left,right)

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
obj.diameterOfBinaryTree(root)
print("Max diameter is --> ",obj.maxx)