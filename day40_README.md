# Day 40 - Corrupted Kingdom Records

## Problem Statement

A digital kingdom archive stores records using a Binary Search Tree (BST).

Unfortunately, corrupted entries may violate BST rules.

Your mission is to determine whether the tree is still a valid BST.

This is the classic:

Validate Binary Search Tree Problem

---

# Objectives

- Solve Validate Binary Search Tree
- Track valid ranges during traversal
- Test invalid tree structures
- Understand BST validation logic

---

# Binary Search Tree Rules

For every node:

Left Subtree:

Node Value < Current Value

Right Subtree:

Node Value > Current Value

And both subtrees must also be valid BSTs.

---

# Valid BST Example

```text
          8
        /   \
       3     10
      / \      \
     1   6      14
```

Validation:

```text
1 < 3 < 8
6 > 3 and < 8
10 > 8
14 > 10
```

Result:

```text
Valid BST
```

---

# Invalid BST Example

```text
          8
        /   \
       3     10
      / \
     1  12
```

Problem:

```text
12 is in the left subtree of 8
but

12 > 8
```

BST Rule Violated ❌

Result:

```text
Invalid BST
```

---

# Validation Logic

Instead of checking only parent-child relationships, we track a valid range for every node.

Example:

Root:

```text
8
```

Allowed Range:

```text
(-∞, +∞)
```

---

Left Child:

```text
3
```

Allowed Range:

```text
(-∞, 8)
```

---

Right Child:

```text
10
```

Allowed Range:

```text
(8, +∞)
```

---

Each recursive call updates these boundaries.

If any node falls outside its valid range:

```text
Return False
```

---

# Visualization

Valid BST:

```text
          8
        /   \
       3     10
```

Ranges:

```text
8  → (-∞, +∞)

3  → (-∞, 8)

10 → (8, +∞)
```

All values satisfy constraints ✅

---

# Edge Cases

### Empty Tree

```text
None
```

Result:

```text
True
```

An empty tree is considered a valid BST.

---

### Single Node

```text
5
```

Result:

```text
True
```

---

### Duplicate Values

```text
    5
   /
  5
```

Result:

```text
False
```

Duplicates are not allowed in this implementation.

---

# Complexity Analysis

## Time Complexity

O(n)

Every node is visited exactly once.

---

## Space Complexity

O(h)

Where:

h = height of tree

Space is used by recursion stack.

---

# Why This Scales

Brute Force Validation:

Repeated subtree checks

Can become:

```text
O(n²)
```

Optimized Range Validation:

Single DFS Traversal

```text
O(n)
```

Much more efficient for large trees.

---

# Real-World Impact

BST validation concepts are used in:

- Database Indexing
- Search Systems
- Distributed Architectures
- Hierarchical Data Storage
- File System Structures

---

# Conclusion

Tracking valid ranges during DFS traversal guarantees that every node satisfies BST rules, making validation both correct and efficient.