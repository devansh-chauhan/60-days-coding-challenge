# Day 15 - The Duplicate Spy Detector

## Problem Statement

A secret agency intercepted a suspicious list of agent IDs.
The goal is to detect whether duplicate IDs exist before the spies infiltrate the system.

---

# Objectives

- Implement brute-force duplicate detection
- Implement optimized duplicate detection using sets
- Compare execution speed
- Analyze scalability for 1 million IDs

---

# Solutions

## 1. Brute Force Approach

### Logic
Compare every ID with every other ID using nested loops.

### Time Complexity
O(n²)

### Space Complexity
O(1)

### Drawback
Very slow for large datasets because comparisons increase rapidly.

---

## 2. Optimized Set-Based Approach

### Logic
Use a set to store visited IDs.
If an ID already exists in the set, a duplicate is found.

### Time Complexity
O(n)

### Space Complexity
O(n)

### Advantage
Extremely fast even for very large datasets.

---

# Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|---|---|---|
| Brute Force | O(n²) | O(1) |
| Optimized Set | O(n) | O(n) |

---

# Observations

- Brute force becomes impractical for 1 million IDs.
- Set-based lookup scales efficiently.
- Optimization dramatically improves performance in large systems.

---

# Real-World Impact

Duplicate detection is widely used in:

- Fraud prevention systems
- Authentication services
- Banking transaction validation
- Database indexing
- Cybersecurity systems

---

# Conclusion

Efficient algorithms are critical in large-scale systems.
Using hashing (sets) significantly improves lookup and duplicate detection performance.