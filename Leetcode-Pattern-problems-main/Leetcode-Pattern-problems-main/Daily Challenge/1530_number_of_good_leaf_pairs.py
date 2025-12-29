# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        
        def dfs(node):
            if not node:
                return []
            
            # If it's a leaf node
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Count all pairs of leaves from left and right subtrees
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.count += 1
            
            # Return the updated distances
            return [n + 1 for n in left_distances + right_distances]
        
        dfs(root)
        return self.count
