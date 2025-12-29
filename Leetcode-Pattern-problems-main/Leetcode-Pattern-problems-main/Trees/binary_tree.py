class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def pre_order(Node):
    if Node is None:
        return []
    return [Node.val] + pre_order(Node.left) + pre_order(Node.right)
def in_order(Node):
    if Node is None:
        return []
    return  in_order(Node.left) + [Node.val]  + in_order(Node.right)
def post_order(Node):
    if Node is None:
        return []
    return post_order(Node.left) + post_order(Node.right) + [Node.val] 

pre = pre_order(root)
print(pre) 
inn = in_order(root)
print(inn) 
post = post_order(root)
print(post) 