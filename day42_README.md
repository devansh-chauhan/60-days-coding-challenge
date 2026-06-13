# Day 42 - Island Survival Simulator

## Problem Statement

A satellite system discovered hundreds of disconnected islands after a massive flood.

Your mission is to determine how many separate islands still exist.

This is the classic:

Number of Islands

problem.

---

# Objectives

- Solve Number of Islands
- Traverse grid using DFS
- Mark visited land cells
- Visualize graph traversal

---

# Grid Representation

Land:

```text
1
```

Water:

```text
0
```

Example Grid:

```text
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```

---

# Island Visualization

```text
Island 1

1 1
1 1
```

---

```text
Island 2

1
```

---

```text
Island 3

1 1
```

Total Islands:

```text
3
```

---

# DFS Traversal Strategy

Whenever we find land:

```text
1
```

We:

1. Count a new island
2. Explore all connected land
3. Mark visited cells

This prevents counting the same island multiple times.

---

# Traversal Example

Starting:

```text
1 1 0
1 1 0
0 0 0
```

Found:

```text
(0,0)
```

Run DFS.

Visit:

```text
(0,0)
(0,1)
(1,0)
(1,1)
```

Mark all as visited.

Entire island processed ✅

---

# Graph Perspective

Each land cell acts like a graph node.

Connections exist:

```text
Up
Down
Left
Right
```

DFS explores all connected nodes.

---

# Edge Cases

### Empty Grid

```text
[]
```

Result:

```text
0
```

---

### All Water

```text
0 0
0 0
```

Result:

```text
0
```

---

### One Giant Island

```text
1 1
1 1
```

Result:

```text
1
```

---

### Multiple Small Islands

```text
1 0 1
0 1 0
1 0 1
```

Result:

```text
5
```

---

# Complexity Analysis

## Time Complexity

O(rows × cols)

Every cell is visited once.

---

## Space Complexity

O(rows × cols)

Worst-case recursion stack.

---

# DFS vs BFS

| Approach | Time | Space |
|-----------|--------|--------|
| DFS | O(m×n) | O(m×n) |
| BFS | O(m×n) | O(m×n) |

Both are efficient.

---

# Real-World Impact

Graph traversal powers:

- Google Maps
- Social Networks
- Recommendation Systems
- Network Monitoring
- Distributed Systems
- Infrastructure Analysis

---

# Conclusion

The Number of Islands problem demonstrates how graph traversal techniques like DFS can efficiently identify connected components within large datasets.