class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)

        print(root.value, end=" ")

        inorder_recursive(root.right)

def inorder_iterative(root):
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        print(current.value, end=" ")

        current = current.right

root = TreeNode("King")

root.left = TreeNode("Prince_A")
root.right = TreeNode("Prince_B")

root.left.left = TreeNode("Duke_A")
root.left.right = TreeNode("Duke_B")

root.right.left = TreeNode("Duke_C")
root.right.right = TreeNode("Duke_D")

print("Recursive Inorder Traversal:")
inorder_recursive(root)

print("\n")

print("Iterative Inorder Traversal:")
inorder_iterative(root)