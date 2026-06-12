class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(node, low=float('-inf'), high=float('inf')):
    if node is None:
        return True

    if node.value <= low or node.value >= high:
        return False

    return (
        is_valid_bst(node.left, low, node.value)
        and
        is_valid_bst(node.right, node.value, high)
    )

valid_root = TreeNode(8)

valid_root.left = TreeNode(3)
valid_root.right = TreeNode(10)

valid_root.left.left = TreeNode(1)
valid_root.left.right = TreeNode(6)

valid_root.right.right = TreeNode(14)

print("Valid BST:", is_valid_bst(valid_root))


invalid_root = TreeNode(8)

invalid_root.left = TreeNode(3)
invalid_root.right = TreeNode(10)

invalid_root.left.left = TreeNode(1)
invalid_root.left.right = TreeNode(12) 

print("Invalid BST:", is_valid_bst(invalid_root))