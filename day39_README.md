# Day 39 - Dungeon Depth Calculator

## Problem Statement

A game developer designed an infinite dungeon.

The dungeon structure behaves exactly like a Binary Tree.

Your mission is to calculate the deepest level a player can reach before getting trapped.

This is the classic:

**Maximum Depth of Binary Tree**

problem.

---

# Objectives

- Solve Maximum Depth of Binary Tree
- Visualize recursive depth calculation
- Compare DFS approaches
- Handle edge cases

---

# Dungeon Structure

```text
                Entrance
               /       \
          Room A      Room B
          /    \
     Room C   Room D
      /
Boss Room
```

---

# What is Maximum Depth?

Maximum Depth = Number of nodes along the longest path from root to leaf.

For the above tree:

```text
Entrance
   ↓
Room A
   ↓
Room C
   ↓
Boss Room
```

Depth = 4

---

# Recursive DFS Approach

For every node:

1. Find depth of left subtree
2. Find depth of right subtree
3. Take maximum
4. Add 1 for current node

Formula:

```text
Depth(node) =
1 + max(
    Depth(left),
    Depth(right)
)
```

---

# Recursive Visualization

Starting at:

```text
Entrance
```

---

Visit Left:

```text
Room A
```

---

Visit Left Again:

```text
Room C
```

---

Visit Left Again:

```text
Boss Room
```

Leaf Node:

```text
Depth = 1
```

---

Backtrack:

```text
Room C

Depth = 1 + max(1,0)
      = 2
```

---

Backtrack:

```text
Room A

Depth = 1 + max(2,1)
      = 3
```

---

Backtrack:

```text
Entrance

Depth = 1 + max(3,1)
      = 4
```

Final Answer:

```text
4
```

---

# Edge Cases

### Empty Tree

```text
None
```

Depth:

```text
0
```

---

### Single Node

```text
Root
```

Depth:

```text
1
```

---

### Completely Skewed Tree

```text
A
 \
  B
   \
    C
     \
      D
```

Depth:

```text
4
```

---

# DFS Approaches

## Recursive DFS

Uses system call stack.

### Complexity

Time Complexity:

O(n)

Space Complexity:

O(h)

where h = tree height

---

## Iterative DFS

Uses explicit stack.

Also:

Time Complexity:

O(n)

Space Complexity:

O(h)

---

# Comparison

| Approach | Time | Space |
|-----------|--------|--------|
| Recursive DFS | O(n) | O(h) |
| Iterative DFS | O(n) | O(h) |

---

# Real-World Impact

Depth calculations are used in:

- AI Search Systems
- Recursive Analysis
- Infrastructure Monitoring
- File Systems
- Organization Hierarchies
- Dependency Graphs

---

# Conclusion

The Maximum Depth problem demonstrates how recursion naturally explores hierarchical structures and helps determine the longest path in a tree efficiently.