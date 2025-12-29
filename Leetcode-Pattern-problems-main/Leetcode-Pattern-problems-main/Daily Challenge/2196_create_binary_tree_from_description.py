from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        left = {}
        right = {}
        all_nodes = set()
        children = set()

        for parent, child, is_left in descriptions:
            if is_left:
                left[parent] = child
            else:
                right[parent] = child
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)
        
        root_val = (all_nodes - children).pop()
        root = TreeNode(root_val)
        nodes = {root_val: root}
        
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
        return root

obj = Solution()
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
obj.createBinaryTree(descriptions)