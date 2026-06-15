# Day 43 - Zombie City Escape Map

## Problem Statement

A zombie outbreak has trapped survivors inside a city grid.

The goal is to find the shortest escape route from the top-left corner to the bottom-right corner.

This is the classic:

Shortest Path in Binary Matrix

problem.

---

# Objectives

- Solve Shortest Path in Binary Matrix
- Implement BFS traversal
- Track visited locations
- Visualize level-by-level exploration

---

# Grid Representation

Safe Cell:

```text
0
```

Blocked Cell (Zombie Zone):

```text
1
```

Example:

```text
0 1 0
0 0 0
1 0 0
```

---

# Why BFS?

BFS explores nodes level by level.

The first time we reach the destination:

```text
Guaranteed shortest path
```

This makes BFS perfect for shortest-path problems in unweighted graphs.

---

# Grid as a Graph

Each cell acts as a node.

Possible movements:

```text
↖ ↑ ↗
←   →
↙ ↓ ↘
```

Total:

```text
8 Directions
```

---

# Traversal Visualization

Grid:

```text
0 1 0
0 0 0
1 0 0
```

Start:

```text
(0,0)
```

Distance:

```text
1
```

---

Level 1

```text
(0,0)
```

---

Level 2

```text
(1,0)
(1,1)
```

---

Level 3

```text
(0,2)
(1,2)
(2,1)
(2,2)
```

Destination Found ✅

---

Shortest Path:

```text
(0,0)
   ↓
(1,1)
   ↓
(2,2)
```

Length:

```text
3
```

---

# BFS Algorithm

1. Start from top-left cell
2. Add cell to queue
3. Explore all valid neighbors
4. Mark visited cells
5. Continue level by level
6. Stop when destination is reached

---

# Edge Cases

### Start Blocked

```text
1 0
0 0
```

Answer:

```text
-1
```

---

### Destination Blocked

```text
0 0
0 1
```

Answer:

```text
-1
```

---

### No Path Exists

```text
0 1
1 0
```

Answer:

```text
-1
```

---

### Single Cell

```text
0
```

Answer:

```text
1
```

---

# Complexity Analysis

## Time Complexity

O(n²)

Each cell is visited at most once.

---

## Space Complexity

O(n²)

Queue and visited tracking.

---

# Why BFS Beats DFS Here

DFS:

```text
May find a path
Not necessarily shortest
```

BFS:

```text
Always finds shortest path first
```

Because it explores level by level.

---

# Real-World Impact

Shortest path algorithms are used in:

- GPS Navigation
- Emergency Response Systems
- Robotics
- Delivery Optimization
- Network Routing
- Autonomous Vehicles

---

# Conclusion

BFS is the ideal solution for shortest-path problems in unweighted graphs because it guarantees the shortest route while exploring nodes systematically level by level.