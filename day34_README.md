# Day 34 - Energy Drink Analyzer

## Problem Statement

A gaming company wants to analyze player energy spikes during tournaments.

The goal is to find the maximum average energy boost within a fixed-size window.

This is the classic Maximum Average Subarray problem.

---

# Objectives

- Solve Maximum Average Subarray
- Implement Fixed-Size Sliding Window
- Compare Naive vs Optimized Solutions
- Visualize Window Movement

---

# Example

Energy Readings:

```text
[1, 12, -5, -6, 50, 3]
```

Window Size:

```text
k = 4
```

Possible Windows:

```text
[1, 12, -5, -6]
Average = 0.5

[12, -5, -6, 50]
Average = 12.75

[-5, -6, 50, 3]
Average = 10.5
```

Maximum Average:

```text
12.75
```

---

# Naive Approach

For every possible window:

1. Calculate sum again
2. Calculate average
3. Track maximum average

---

## Complexity

Time Complexity:

O(n × k)

Space Complexity:

O(1)

---

# Sliding Window Approach

Instead of recalculating every window:

1. Calculate first window sum
2. Remove outgoing element
3. Add incoming element
4. Update maximum

---

# Window Visualization

Array:

```text
[1, 12, -5, -6, 50, 3]
```

Window Size = 4

---

### Window 1

```text
[1, 12, -5, -6]
```

Sum = 2

Average = 0.5

---

### Slide Right

Remove:

```text
1
```

Add:

```text
50
```

New Window:

```text
[12, -5, -6, 50]
```

Sum = 51

Average = 12.75

---

### Slide Right Again

Remove:

```text
12
```

Add:

```text
3
```

New Window:

```text
[-5, -6, 50, 3]
```

Sum = 42

Average = 10.5

---

# Why Sliding Window Is Better

Naive:

Recalculate every window from scratch.

```text
O(n × k)
```

---

Sliding Window:

Reuse previous calculation.

```text
O(n)
```

---

# Performance Comparison

| Approach | Time Complexity |
|-----------|----------------|
| Naive | O(n × k) |
| Sliding Window | O(n) |

---

# Real-World Impact

Sliding Window techniques are used in:

- Streaming Analytics
- Financial Monitoring
- Real-Time Dashboards
- Sensor Data Processing
- Network Traffic Analysis

---

# Conclusion

Sliding Window optimization avoids redundant calculations and makes real-time analytics systems significantly faster and more scalable.