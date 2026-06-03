# Day 31 - Dutch Flag Sorting Machine

## Problem Statement

A robotics factory sorts colored capsules moving through conveyor belts.

Colors:
- Red = 0
- White = 1
- Blue = 2

The goal is to sort them efficiently while minimizing swaps.

---

# Objectives

- Solve Sort Colors problem
- Avoid built-in sorting
- Optimize swaps
- Visualize pointer movement

---

# Dutch National Flag Algorithm

This problem is solved using three pointers:

- low
- mid
- high

The array is divided into four regions:

[ Reds | Whites | Unknown | Blues ]

---

# Pointer Roles

## low

Tracks where the next Red (0) should go.

## mid

Current element being processed.

## high

Tracks where the next Blue (2) should go.

---

# Example

Input:

[2, 0, 2, 1, 1, 0]

---

# Step 1

low = 0
mid = 0
high = 5

Current:

[2, 0, 2, 1, 1, 0]

2 found

Swap with high

Result:

[0, 0, 2, 1, 1, 2]

---

# Step 2

0 found

Swap low and mid

Result:

[0, 0, 2, 1, 1, 2]

Move low and mid

---

# Final Result

[0, 0, 1, 1, 2, 2]

---

# Why This Is Optimal

Naive Approach:

- Count colors
- Rewrite array

or

- Use built-in sorting

Time Complexity:
O(n log n)

---

Optimized Approach:

Single traversal

Time Complexity:
O(n)

Space Complexity:
O(1)

---

# Complexity Analysis

| Operation | Complexity |
|------------|------------|
| Sorting | O(n) |
| Extra Space | O(1) |

---

# Real-World Impact

Sorting algorithms power:

- Logistics systems
- Inventory management
- Search engines
- Database indexing
- Warehouse automation

---

# Conclusion

The Dutch National Flag Algorithm sorts three categories efficiently using only one traversal and constant extra space.