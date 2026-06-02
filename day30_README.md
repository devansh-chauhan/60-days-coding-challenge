# Day 30 - Hacker Tournament Finals

## Challenge

Solve two medium-level algorithm problems while focusing on:

- Optimization
- Scalability
- Complexity Analysis
- Tradeoff Discussion

---

# Problem 1: Longest Substring Without Repeating Characters

## Approach

Used Sliding Window + Hash Set.

The window expands until a duplicate is found.

When duplicate appears:
- Move left pointer
- Remove characters from set

## Why It Scales

Naive Approach:
O(n²)

Optimized Approach:
O(n)

Each character enters and leaves the window at most once.

## Tradeoff

Extra memory is used for the hash set.

Space Complexity:
O(n)

---

# Problem 2: Container With Most Water

## Approach

Used Two Pointer Optimization.

Start:
- Left pointer at beginning
- Right pointer at end

Move the pointer with smaller height.

## Why It Scales

Naive Approach:
Check every pair

O(n²)

Optimized Approach:
Single traversal

O(n)

## Tradeoff

Requires understanding of pointer movement logic but dramatically improves performance.

Space Complexity:
O(1)

---

# Complexity Summary

| Problem | Brute Force | Optimized |
|----------|------------|------------|
| Longest Substring | O(n²) | O(n) |
| Container With Most Water | O(n²) | O(n) |

---

# Key Learning

Good engineering is not only about solving a problem.

It is about:
- Reducing unnecessary work
- Choosing efficient data structures
- Understanding scalability
- Communicating tradeoffs