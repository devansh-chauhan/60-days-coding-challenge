# Day 16 - The Infinite Staircase Puzzle

## Problem Statement

A robot can climb either 1 or 2 steps at a time.

The goal is to calculate how many different ways the robot can reach step N.

---

# Recursive Solution

## Logic

To reach step N:
- The robot can come from step (N - 1)
- Or from step (N - 2)

So:

ways(n) = ways(n - 1) + ways(n - 2)

This is similar to the Fibonacci sequence.

---

# Recursion Tree Example

For n = 5:

                5
             /     \
            4       3
          /  \     / \
         3    2   2   1
        / \
       2   1

Many calculations repeat multiple times.

Example:
- ways(3) is recalculated repeatedly
- ways(2) is recalculated repeatedly

---

# Time Complexity

## Recursive Solution
- Time Complexity: O(2^n)
- Space Complexity: O(n)

### Problem
The recursive approach recalculates the same subproblems many times.

---

# Optimized Solution using Memoization

## Logic

Store previously computed results in a dictionary (memo).

Before calculating:
- Check if result already exists
- Reuse stored result

---

# Optimized Complexity

## Memoization Solution
- Time Complexity: O(n)
- Space Complexity: O(n)

---

# Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Recursive | O(2^n) | O(n) |
| Memoization | O(n) | O(n) |

---

# Observations

- Recursive solutions are elegant but inefficient for large inputs.
- Memoization avoids repeated calculations.
- Optimization dramatically improves execution speed.

---

# Real-World Impact

Recursive thinking is widely used in:
- AI search systems
- Pathfinding algorithms
- Game engines
- Dynamic programming
- Compiler design

---

# Conclusion

Memoization transforms expensive recursive solutions into scalable and efficient systems.