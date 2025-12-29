class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def postorder(root: 'Node') -> list[int]:
        result = []
        def traversal(node):
            if node is None:
                return []
            for child in node.children:
                traversal(child)
            result.append(node.val)
        traversal(root)
        return result

def preorder(root):
    result = []
    def traversal(node):
        if node is None:
            return []
        result.append(node.val)
        for child in node.children:
            traversal(child)
    traversal(root)
    return result

def inorder(root):
    result = []
    def traversal(node):
        if node is None:
            return []
        n = len(node.children)
        for i in range(n//2):
            traversal(node.children[i])
        result.append(node.val)
        for i in range(n//2, n):
            traversal(node.children[i])
    traversal(root)
    return result