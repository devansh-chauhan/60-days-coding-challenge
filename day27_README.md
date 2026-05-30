# Day 27 - Social Media Fraud Detector

## Problem Statement

A social media platform suspects bots are repeatedly posting duplicate content.

The goal is to detect whether the same content appears again within a limited distance K.

---

# Objectives

- Track repeated activity using hashing
- Detect duplicates within K distance
- Simulate social media events
- Understand why hashing improves performance

---

# Example

Posts:

[
"Hello World",
"AI is awesome",
"Python",
"Hello World"
]

K = 3

The duplicate "Hello World" appears again after 3 positions.

Result:
Fraud Detected ✅

---

# Approach Using Hashing

We use a hash map (dictionary).

The hash map stores:

Post Content → Last Seen Index

Example:

{
"Hello World": 0,
"Python": 2
}

---

# Algorithm

1. Traverse posts one by one
2. Check if post already exists in hash map
3. Calculate distance

distance = current_index - previous_index

4. If distance ≤ K:
   - Duplicate detected
5. Update latest index

---

# Visualization

Posts:

Index: 0
Post: Hello World

Store:

{
"Hello World": 0
}

---

Index: 3
Post: Hello World

Distance:

3 - 0 = 3

Since:

3 ≤ K

Fraud Alert Triggered

---

# Why Hashing Improves Performance

Without Hashing:

- Compare every post with every other post
- Nested loops required

Time Complexity:

O(n²)

---

With Hashing:

- Instant lookup using dictionary
- Single traversal

Time Complexity:

O(n)

---

# Complexity Analysis

## Optimized Solution

Time Complexity:
O(n)

Space Complexity:
O(n)

---

# Comparison

| Approach | Time Complexity |
|-----------|----------------|
| Brute Force | O(n²) |
| Hashing | O(n) |

---

# Real-World Impact

Hashing is heavily used in:

- Fraud Detection Systems
- Spam Filtering
- Cybersecurity Monitoring
- Social Media Platforms
- Authentication Systems

---

# Conclusion

Hashing allows duplicate detection in a single pass, making fraud detection systems scalable and efficient for millions of events.