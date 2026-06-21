# Day 49 - Ultimate Engineering Gauntlet

## Problem 1: Number of Islands

### Thought Process
The grid can be treated as a graph where each land cell is connected to neighboring land cells.

### Solution Choice
DFS traversal.

### Complexity
Time: O(m × n)
Space: O(m × n)

### Tradeoff
DFS is simple and efficient. BFS would provide similar complexity.

---

## Problem 2: House Robber

### Thought Process
At each house:

1. Rob it
2. Skip it

Need maximum profit while avoiding adjacent houses.

### Solution Choice
Dynamic Programming.

### Complexity
Time: O(n)
Space: O(1)

### Tradeoff
DP avoids exponential recursion.

---

## Problem 3: Two Sum

### Thought Process
Brute force checks every pair.

Optimization uses a hash map to store previously seen values.

### Complexity

Brute Force:
Time: O(n²)

Optimized:
Time: O(n)

Space: O(n)

### Tradeoff
Uses additional memory to significantly reduce runtime.

---

# Engineering Reflection

A correct solution is not always enough.

Engineers must consider:

- Scalability
- Memory usage
- Maintainability
- Tradeoffs
- Communication

The best solution balances correctness and efficiency.