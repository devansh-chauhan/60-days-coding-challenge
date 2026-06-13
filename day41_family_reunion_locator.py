class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    current = root
    while current:
        if p < current.value and q < current.value:
            current = current.left
        elif p > current.value and q > current.value:
            current = current.right
        else:
            return current

    return None


root = TreeNode(20)

root.left = TreeNode(10)
root.right = TreeNode(30)

root.left.left = TreeNode(5)
root.left.right = TreeNode(15)

root.right.left = TreeNode(25)
root.right.right = TreeNode(35)

person1 = 5
person2 = 15

ancestor = lowest_common_ancestor(root, person1, person2)

print("Person 1:", person1)
print("Person 2:", person2)
print("Lowest Common Ancestor:", ancestor.value)