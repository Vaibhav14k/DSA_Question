from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right

def pre_order(Node):
    if Node is None:
        return []
    return  [Node.val] + pre_order(Node.left) +  pre_order(Node.right) 

# BFS Traversal
def bfs(Node):
    if Node is None:
        return []
    queue = [Node]
    results = []
    while queue:
        node = queue.pop(0)
        results.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return results

def LevelWiseTraversal(Node):
    if Node is None:
        return []
    queue = deque([Node])
    results = []
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        results.append(level)
    return results

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


pre = pre_order(root)
print(pre) 

print(bfs(root))
print(LevelWiseTraversal(root))