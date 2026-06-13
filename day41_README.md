# Day 41 - Family Reunion Locator

## Problem Statement

A genealogy company needs to reconnect lost family members.

Given two people in a family tree represented as a Binary Search Tree (BST), find their closest common ancestor.

This is the classic:

Lowest Common Ancestor (LCA) of BST

problem.

---

# Objectives

- Solve Lowest Common Ancestor of BST
- Visualize ancestor traversal
- Compare node values strategically
- Understand BST traversal decisions

---

# Family Tree

```text
                 20
               /    \
             10      30
            /  \    /  \
           5   15  25  35
```

Find LCA of:

```text
5 and 15
```

Answer:

```text
10
```

---

# What is Lowest Common Ancestor?

The Lowest Common Ancestor is the lowest node in the tree that has both target nodes as descendants.

Example:

```text
       10
      /  \
     5   15
```

Common Ancestor:

```text
10
```

---

# BST Property

For every node:

```text
Left Child < Node < Right Child
```

This property allows efficient searching.

---

# Traversal Strategy

Start at Root:

```text
20
```

Targets:

```text
5 and 15
```

Both values are smaller than:

```text
20
```

Move Left.

---

Current Node:

```text
10
```

Now:

```text
5 < 10
15 > 10
```

One node is on the left and the other is on the right.

This is the split point.

Therefore:

```text
LCA = 10
```

---

# Visualization

```text
                 20
                /
              10   ← LCA
             /  \
            5   15
```

Traversal:

```text
20
 ↓
10 ✅
```

---

# Why BST Makes It Efficient

Without BST property:

Need to search both subtrees.

Time Complexity:

```text
O(n)
```

---

With BST property:

We eliminate half the tree at every step.

Time Complexity:

```text
O(h)
```

where:

```text
h = height of tree
```

---

# Edge Cases

### Same Node

```text
LCA(10,10)
```

Answer:

```text
10
```

---

### One Node Is Ancestor

```text
       10
      /
     5
```

LCA:

```text
LCA(10,5)
```

Answer:

```text
10
```

---

### Root Is LCA

```text
       20
      /  \
    10   30
```

LCA:

```text
LCA(10,30)
```

Answer:

```text
20
```

---

# Complexity Analysis

## Time Complexity

O(h)

h = height of BST

Balanced BST:

```text
O(log n)
```

---

## Space Complexity

O(1)

Iterative solution uses constant extra space.

---

# Real-World Impact

Lowest Common Ancestor concepts are used in:

- File Systems
- Network Routing
- Organizational Hierarchies
- Version Control Systems
- Genealogy Platforms
- Dependency Management

---

# Conclusion

The BST property allows us to find the Lowest Common Ancestor efficiently by comparing node values and moving toward the split point where paths to both targets diverge.