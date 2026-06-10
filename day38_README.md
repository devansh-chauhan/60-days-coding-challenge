# Day 38 - Ancient Kingdom Family Tree

## Problem Statement

An ancient kingdom preserved royal family records in a hierarchical tree structure.

The goal is to traverse the royal lineage in the correct order and reveal hidden secrets.

This challenge introduces Binary Trees and Inorder Traversal.

---

# Objectives

- Build a Binary Tree
- Perform Inorder Traversal
- Visualize Traversal Order
- Compare Recursive and Iterative Approaches

---

# Royal Family Tree

```text
                King
               /    \
        Prince_A   Prince_B
          /   \      /   \
     Duke_A Duke_B Duke_C Duke_D
```

---

# What is Inorder Traversal?

Traversal Order:

```text
Left → Root → Right
```

For every node:

1. Visit Left Subtree
2. Visit Current Node
3. Visit Right Subtree

---

# Traversal Visualization

Starting at King:

Step 1:

Move Left

```text
King → Prince_A → Duke_A
```

Visit:

```text
Duke_A
```

---

Step 2:

Back to:

```text
Prince_A
```

Visit:

```text
Prince_A
```

---

Step 3:

Visit:

```text
Duke_B
```

---

Step 4:

Back to:

```text
King
```

Visit:

```text
King
```

---

Continue Right Subtree:

```text
Duke_C
Prince_B
Duke_D
```

---

Final Inorder Traversal:

```text
Duke_A Prince_A Duke_B King Duke_C Prince_B Duke_D
```

---

# Recursive Approach

Uses function calls automatically.

```python
inorder(left)
visit(root)
inorder(right)
```

### Complexity

Time Complexity:

O(n)

Space Complexity:

O(h)

where h = tree height

---

# Iterative Approach

Uses an explicit stack.

### Steps

1. Push left nodes into stack
2. Pop node
3. Visit node
4. Move right

### Complexity

Time Complexity:

O(n)

Space Complexity:

O(h)

---

# Recursive vs Iterative

| Approach | Time | Space |
|-----------|--------|--------|
| Recursive | O(n) | O(h) |
| Iterative | O(n) | O(h) |

---

# Real-World Impact

Tree traversals are used in:

- File Systems
- Databases
- Compilers
- Search Engines
- HTML DOM Structures
- Organization Hierarchies

---

# Conclusion

Binary Trees provide an efficient way to represent hierarchical data. Inorder traversal systematically visits nodes in Left → Root → Right order and forms the foundation for many advanced tree algorithms.