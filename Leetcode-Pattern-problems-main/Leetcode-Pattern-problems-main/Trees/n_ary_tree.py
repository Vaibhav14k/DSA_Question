class TreeNode:
    def __init__(self,val=None):
        self.val = val
        self.child = []
    
    def add_child(self,node):
        self.child.append(node)


# Root node
root = TreeNode('A')

# Children of the root
child1 = TreeNode('B')
child2 = TreeNode('C')
child3 = TreeNode('D')

# Adding children to root
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

# Adding children to the first child
child1.add_child(TreeNode('E'))
child1.add_child(TreeNode('F'))

# Adding a child to the second child
child2.add_child(TreeNode('G'))

# Adding children to the third child
child3.add_child(TreeNode('H'))
child3.add_child(TreeNode('I'))
child3.add_child(TreeNode('J'))

# Traversal
def dfs_traversal(node):
    if node is None:
        return
    print(node.val,end="")
    for child in node.child:
        dfs_traversal(child)

dfs_traversal(root)
