class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        result = []
        def traversal(node):
            if node is None:
                return []
            for child in node.children:
                traversal(child)
            result.append(node.val)
        traversal(root)
        return result

