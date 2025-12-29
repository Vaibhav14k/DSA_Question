class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),height(node.right))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

print(height(root))