class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)

root = TreeNode("Entrance")
root.left = TreeNode("Room A")
root.right = TreeNode("Room B")

root.left.left = TreeNode("Room C")
root.left.right = TreeNode("Room D")

root.left.left.left = TreeNode("Boss Room")

depth = max_depth(root)

print("Maximum Dungeon Depth:", depth)