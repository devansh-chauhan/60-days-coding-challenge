# Day 47 - Treasure Dungeon Collector

## Problem Statement

A treasure hunter explores a dungeon filled with gold rooms.

However, robbing two adjacent rooms triggers an alarm.

Your mission is to collect the maximum possible treasure without entering adjacent rooms.

This is the classic:

House Robber Problem

---

# Objectives

- Solve House Robber
- Compare Greedy vs Dynamic Programming
- Track Optimal Substructure
- Visualize Decision Making

---

# Example

Treasure Rooms:

```text
[2, 7, 9, 3, 1]
```

---

# Rules

If you rob a room:

```text
You cannot rob adjacent rooms.
```

Example:

```text
[2, 7, 9, 3, 1]
```

Possible Choice:

```text
2 + 9 + 1 = 12
```

Maximum Treasure:

```text
12
```

---

# Why Greedy Fails

Consider:

```text
[2, 1, 1, 2]
```

Greedy:

```text
2 + 1 = 3
```

Optimal:

```text
2 + 2 = 4
```

Greedy misses the best solution.

---

# Dynamic Programming Idea

At each room we have two choices:

1. Skip current room
2. Rob current room

Formula:

```text
dp[i] = max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

Meaning:

Take the best of:

- Skipping current room
- Robbing current room

---

# State Transition Visualization

Rooms:

```text
[2, 7, 9, 3, 1]
```

DP Table:

```text
dp[0] = 2

dp[1] = max(2,7)
      = 7

dp[2] = max(7,2+9)
      = 11

dp[3] = max(11,7+3)
      = 11

dp[4] = max(11,11+1)
      = 12
```

Final Answer:

```text
12
```

---

# Decision Tree

```text
Room 4

Choose:

Skip
│
└── dp[3]

OR

Rob
│
└── dp[2] + value
```

DP stores the best answer at every step.

---

# Optimal Substructure

The solution for:

```text
Room i
```

depends only on:

```text
Room i-1
Room i-2
```

This makes Dynamic Programming possible.

---

# Complexity Analysis

## Greedy

Time:

```text
O(n)
```

But not always correct.

---

## Dynamic Programming

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# Space Optimization

Instead of storing the entire DP array:

Store only:

```text
prev1
prev2
```

Space becomes:

```text
O(1)
```

---

# Real-World Impact

Constraint optimization appears in:

- Investment Planning
- Budget Allocation
- Resource Scheduling
- Supply Chain Management
- AI Decision Systems

---

# Conclusion

The House Robber problem demonstrates how Dynamic Programming finds globally optimal solutions by storing and reusing results from smaller subproblems.