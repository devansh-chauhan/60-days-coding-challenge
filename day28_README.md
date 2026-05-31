# Day 28 - The Lost Treasure Coordinates

## Problem Statement

A pirate captain left behind a treasure map with hidden coordinate pairs.

The goal is to find two coordinates whose sum equals the target treasure location.

This is the classic Two Sum problem.

---

# Objectives

- Solve the Two Sum problem
- Build brute-force and optimized solutions
- Compare execution times
- Visualize lookup process

---

# Example

Coordinates:

[2, 7, 11, 15]

Target:

9

Answer:

2 + 7 = 9

Indices:

[0, 1]

---

# Solution 1: Brute Force

## Approach

Check every possible pair.

Pseudo Flow:

2 + 7 = 9 ✅

Return indices.

---

## Complexity

Time Complexity:
O(n²)

Space Complexity:
O(1)

---

# Solution 2: Optimized Hash Map

## Approach

Store previously seen numbers.

For each number:

complement = target - current_number

Check if complement already exists.

If yes:
Found answer instantly.

---

# Lookup Visualization

Coordinates:

[2, 7, 11, 15]

Target = 9

Step 1:

Current = 2

Complement = 7

Store:

{
2 : 0
}

---

Step 2:

Current = 7

Complement = 2

Found 2 in hash map ✅

Answer:

[0,1]

---

# Why Hashing Is Faster

Without Hashing:

Compare every pair.

O(n²)

---

With Hashing:

Single traversal.

O(n)

---

# Performance Comparison

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |

---

# Real-World Impact

Pair matching techniques are used in:

- Financial transaction systems
- Recommendation engines
- Search optimization
- Fraud detection
- Data analytics

---

# Conclusion

Hashing transforms the Two Sum problem from a quadratic solution into a linear-time solution, making it scalable for large datasets.