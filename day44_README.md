# Day 44 - University Course Planner

## Problem Statement

A university has created a course schedule where some courses depend on others.

Students can only take a course after completing its prerequisites.

Your mission is to determine whether all courses can be completed.

This is the classic:

Course Schedule Problem

---

# Objectives

- Solve Course Schedule
- Detect cycles in dependency graph
- Implement BFS (Topological Sort)
- Visualize prerequisite relationships

---

# Example 1

Courses:

```text
0 → 1 → 2 → 3
```

Prerequisites:

```python
[
 [1,0],
 [2,1],
 [3,2]
]
```

Possible Order:

```text
0 → 1 → 2 → 3
```

Result:

```text
Can Graduate = True
```

---

# Example 2

Prerequisites:

```text
0 → 1
↑   ↓
└───┘
```

Dependencies:

```python
[
 [1,0],
 [0,1]
]
```

Cycle Exists ❌

Result:

```text
Can Graduate = False
```

---

# Graph Representation

Each course is a node.

Prerequisite relationship:

```text
A → B
```

means:

```text
Complete A before B
```

---

# Why Cycles Are a Problem

Example:

```text
Course A requires B

Course B requires A
```

Neither can be completed first.

Students get stuck forever.

This is called a cycle.

---

# Kahn's Algorithm (BFS Topological Sort)

Step 1:

Calculate indegree of every course.

Indegree = Number of prerequisites.

---

Step 2:

Add all courses with:

```text
indegree = 0
```

to queue.

---

Step 3:

Process queue.

Remove completed course.

Reduce indegree of dependent courses.

---

Step 4:

If all courses are completed:

```text
No Cycle
```

Otherwise:

```text
Cycle Exists
```

---

# Visualization

Courses:

```text
0 → 1 → 2 → 3
```

Initial Indegree:

```text
0 : 0
1 : 1
2 : 1
3 : 1
```

Queue:

```text
[0]
```

Process:

```text
0 → 1 → 2 → 3
```

All courses completed ✅

---

# Edge Cases

### No Courses

```text
0
```

Answer:

```text
True
```

---

### No Prerequisites

```text
[]
```

Answer:

```text
True
```

---

### Direct Cycle

```text
0 → 1
1 → 0
```

Answer:

```text
False
```

---

# Complexity Analysis

## Time Complexity

O(V + E)

Where:

- V = Number of Courses
- E = Number of Prerequisites

---

## Space Complexity

O(V + E)

For graph and queue storage.

---

# DFS vs BFS

| Approach | Time | Space |
|-----------|---------|---------|
| DFS Cycle Detection | O(V+E) | O(V+E) |
| BFS Topological Sort | O(V+E) | O(V+E) |

Both are efficient.

---

# Real-World Impact

Dependency graphs are used in:

- University Scheduling
- Package Managers (npm, pip)
- CI/CD Pipelines
- Build Systems
- Task Scheduling
- Workflow Automation

---

# Conclusion

The Course Schedule problem demonstrates how graph cycle detection helps determine whether dependencies can be resolved successfully. Topological Sorting provides an efficient way to verify if a valid execution order exists.