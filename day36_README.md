# Day 36 - Water Reservoir Architect

## Problem Statement

A futuristic city needs an efficient reservoir system.

Given multiple wall heights, find two walls that can store the maximum amount of water.

This is the classic:

**Container With Most Water**

problem.

---

# Objectives

- Solve Container With Most Water
- Compare brute-force vs optimized solution
- Visualize pointer movement
- Understand why moving the smaller wall works

---

# Example

Walls:

```text
[1,8,6,2,5,4,8,3,7]
```

Maximum Water:

```text
49
```

---

# Formula

Water Stored:

```text
Area = Width × Height
```

Where:

```text
Width = Right Index - Left Index

Height = Minimum of both walls
```

Example:

```text
Wall A = 8
Wall B = 7

Width = 7

Area = 7 × min(8,7)
     = 49
```

---

# Brute Force Approach

Check every possible pair.

For each pair:

1. Calculate width
2. Calculate area
3. Update maximum

---

## Complexity

Time Complexity:

O(n²)

Space Complexity:

O(1)

---

# Optimized Two Pointer Approach

Use:

```text
Left Pointer
Right Pointer
```

Initially:

```text
left = 0
right = n - 1
```

Calculate area.

Then move the smaller wall.

---

# Pointer Movement Visualization

Array:

```text
[1,8,6,2,5,4,8,3,7]
```

---

### Step 1

```text
Left = 1
Right = 7

Width = 8

Area = 8 × 1 = 8
```

Smaller wall = 1

Move Left →

---

### Step 2

```text
Left = 8
Right = 7

Width = 7

Area = 7 × 7 = 49
```

Maximum Found ✅

---

# Why Move The Smaller Wall?

Suppose:

```text
Height Left = 3
Height Right = 8
```

Area depends on:

```text
min(3,8)
```

which is:

```text
3
```

Moving the taller wall cannot increase the minimum height.

The shorter wall is limiting the area.

Therefore:

Move the smaller wall and search for a taller one.

This is the key optimization.

---

# Why Moving The Larger Wall Doesn't Help

Example:

```text
3 ........ 8
```

Area depends on:

```text
min(3,8) = 3
```

If we move:

```text
8 → 7
```

The limiting factor is still:

```text
3
```

Area cannot improve.

Only replacing the smaller wall may increase capacity.

---

# Complexity Comparison

| Approach | Time Complexity |
|-----------|----------------|
| Brute Force | O(n²) |
| Two Pointers | O(n) |

---

# Real-World Impact

Optimization techniques like this are used in:

- Infrastructure Planning
- Memory Allocation
- Resource Balancing
- Network Optimization
- Capacity Planning Systems

---

# Conclusion

The Two Pointer approach reduces complexity from O(n²) to O(n) by intelligently eliminating impossible candidates and focusing only on potentially better solutions.