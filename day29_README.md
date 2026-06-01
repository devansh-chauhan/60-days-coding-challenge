# Day 29 - Viral Hashtag Tracker

## Problem Statement

A social media company wants to identify trending hashtags in real time.

The goal is to find the Top K most frequently used hashtags efficiently.

---

# Objectives

- Analyze hashtag frequency
- Find Top K frequent hashtags
- Compare sorting and heap approaches
- Visualize trending outputs

---

# Example Dataset

Hashtags:

#AI
#Python
#AI
#Coding
#Python
#AI

---

# Frequency Analysis

Frequency Table:

| Hashtag | Count |
|----------|--------|
| #AI | 5 |
| #Python | 4 |
| #Coding | 2 |
| #ML | 2 |
| #DataScience | 1 |

---

# Trending Output

Top 3 Trending Hashtags:

1. #AI
2. #Python
3. #Coding

---

# Approach 1: Sorting

## Steps

1. Count frequencies
2. Sort frequency table
3. Return first K elements

### Time Complexity

O(n log n)

### Space Complexity

O(n)

---

# Approach 2: Heap

## Steps

1. Count frequencies
2. Maintain Top K elements using heap
3. Return largest K frequencies

### Time Complexity

O(n log k)

### Space Complexity

O(n)

---

# Performance Comparison

| Approach | Time Complexity |
|-----------|----------------|
| Sorting | O(n log n) |
| Heap | O(n log k) |

---

# Why Heap Is Better

When K is small and data is huge:

Example:

1 Million hashtags

Need only Top 10

Heap avoids sorting everything.

This makes it much faster.

---

# Trending Visualization

Frequency Counts:

#AI          █████
#Python      ████
#Coding      ██
#ML          ██
#DataScience █

---

# Real-World Impact

Frequency analysis powers:

- Twitter/X Trending Topics
- Instagram Explore Page
- YouTube Trending
- Spotify Charts
- Search Engine Analytics

---

# Conclusion

Heap-based solutions scale better for large datasets because they focus only on the most important K elements instead of sorting all data.