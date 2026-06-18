# Day 46 - Robot Energy Saver

## Problem Statement

A robot must travel across dangerous rooftops.

Each step requires a certain amount of energy.

The robot can climb either:

- 1 step
- 2 steps

Your goal is to find the minimum energy required to reach the top.

This is the classic:

Min Cost Climbing Stairs

problem.

---

# Objectives

- Solve Min Cost Climbing Stairs
- Compare Recursion vs Dynamic Programming
- Store intermediate results
- Visualize state transitions

---

# Example

Cost Array:

```text
[10, 15, 20]
```

Meaning:

```text
Step 0 → Cost 10
Step 1 → Cost 15
Step 2 → Cost 20
```

Robot can start at:

```text
Step 0
or
Step 1
```

---

# Best Path

Option 1:

```text
Start at 0

10 → 20

Total = 30
```

---

Option 2:

```text
Start at 1

15

Total = 15
```

Minimum Cost:

```text
15
```

---

# Recursive Approach

For every step:

```text
Cost(i)

=
Minimum of:

Cost(i-1)
Cost(i-2)
```

Recursive Formula:

```text
f(i) = min(
f(i-1)+cost[i-1],
f(i-2)+cost[i-2]
)
```

---

# Problem With Recursion

Many states are recalculated repeatedly.

Example:

```text
f(5)
├── f(4)
│   ├── f(3)
│   └── f(2)
└── f(3)
```

Notice:

```text
f(3)
```

is computed multiple times.

This causes inefficiency.

---

# Dynamic Programming Solution

Store previously calculated results.

Instead of recomputing:

```text
Use dp array
```

Example:

```text
dp[0] = 0
dp[1] = 0

dp[2] = min(15,10)
```

Build solution step-by-step.

---

# State Transition Visualization

Cost:

```text
[10,15,20]
```

DP Table:

```text
dp[0] = 0
dp[1] = 0

dp[2] = min(
0+15,
0+10
)

= 10
```

---

```text
dp[3] = min(
10+20,
0+15
)

= 15
```

Final Answer:

```text
15
```

---

# Recursion vs DP

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Recursion | O(2^n) | O(n) |
| DP | O(n) | O(n) |

---

# Why DP Is Better

Recursion:

```text
Repeated calculations
```

DP:

```text
Compute once
Reuse forever
```

This dramatically improves performance.

---

# Edge Cases

### Single Step

```text
[10]
```

Answer:

```text
0
```

Can start at top.

---

### Two Steps

```text
[10,15]
```

Answer:

```text
10
```

---

### Empty Array

```text
[]
```

Answer:

```text
0
```

---

# Real-World Impact

Dynamic Programming is used in:

- Route Optimization
- Robotics
- AI Planning
- Logistics
- Financial Forecasting
- Resource Allocation

---

# Conclusion

Dynamic Programming transforms an expensive recursive solution into an efficient linear-time solution by storing and reusing intermediate results.