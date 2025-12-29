# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Helper function to find the path from the root to a given value.
        def findPath(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            # Try to find the value in the left subtree
            if findPath(root.left, value, path):
                path.append('L')
                return True
            # Try to find the value in the right subtree
            if findPath(root.right, value, path):
                path.append('R')
                return True
            return False
        
        startPath = []
        destPath = []
        
        # Find the paths from the root to the startValue and destValue
        findPath(root, startValue, startPath)
        findPath(root, destValue, destPath)
        
        # Reverse the paths to get them from root to the respective nodes
        startPath = startPath[::-1]
        destPath = destPath[::-1]
        
        # Find the common prefix length
        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1
        
        # Steps to go up to the common ancestor
        up_moves = 'U' * (len(startPath) - i)
        # Steps to go down to the destination node
        down_moves = ''.join(destPath[i:])
        
        return up_moves + down_moves
