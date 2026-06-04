# Day 32 - Hidden Number Vault

## Problem Statement

A hacker buried secret access codes inside a giant sorted vault.

Searching every number one by one would be slow.

The goal is to find the target code efficiently using Binary Search.

---

# Objectives

- Implement Iterative Binary Search
- Visualize search space shrinking
- Compare Linear Search vs Binary Search
- Understand performance differences

---

# Example

Vault:

[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

Target:

35

Result:

Found at Index 6

---

# Linear Search

## How It Works

Check each element one by one.

Example:

5 ❌
10 ❌
15 ❌
20 ❌
25 ❌
30 ❌
35 ✅

Found

---

# Binary Search

## How It Works

Works only on sorted arrays.

Instead of checking every element:

- Find middle element
- Decide which half may contain target
- Ignore the other half

Repeat until found.

---

# Search Space Visualization

Array:

[5,10,15,20,25,30,35,40,45,50]

Target = 35

Step 1:

Middle = 25

35 > 25

Ignore left half

Remaining:

[30,35,40,45,50]

---

Step 2:

Middle = 40

35 < 40

Ignore right half

Remaining:

[30,35]

---

Step 3:

Middle = 35

Found ✅

---

# Why Binary Search Is Faster

Linear Search:

Check every element.

Worst Case:

O(n)

---

Binary Search:

Halves search space each step.

Worst Case:

O(log n)

---

# Performance Comparison

| Algorithm | Time Complexity |
|------------|----------------|
| Linear Search | O(n) |
| Binary Search | O(log n) |

---

# Example

1,000,000 Elements

Linear Search:

May check 1,000,000 items.

Binary Search:

About 20 comparisons.

Huge difference.

---

# Real-World Impact

Binary Search powers:

- Databases
- Search Engines
- Recommendation Systems
- File Systems
- Large-scale Indexing

---

# Conclusion

Binary Search dramatically improves performance by eliminating half of the search space during every step.