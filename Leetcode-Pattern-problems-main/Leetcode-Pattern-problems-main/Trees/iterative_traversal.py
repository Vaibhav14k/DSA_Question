from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        # If position of right and left swap here then preorder of right part is given first in output
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def inorderTraversal( root: Optional[TreeNode]) -> list[int]:
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

def postorderTraversal( root: Optional[TreeNode]) -> list[int]:
        stack1 = [root]
        stack2 = []
        result = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        print([i.val for i in stack2]) # if i add right and then left it will become preorder
        while stack2:
            node = stack2.pop()
            result.append(node.val)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(10)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

# Binary Tree Diagram:
# 
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
#    /       / \
#   10      8   9

print(preorderTraversal(root))
print("---"*20)
print(inorderTraversal(root))
print("---"*20)
print(postorderTraversal(root))