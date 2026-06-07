# Day 35 - Hacker Signal Decoder

## Problem Statement

A cybersecurity team intercepted a mysterious hacker signal.

Repeated characters corrupt the decoding process.

The mission is to identify the longest unique signal pattern before repetition occurs.

This is the classic:

**Longest Substring Without Repeating Characters**

problem.

---

# Objectives

- Solve Longest Substring Without Repeating Characters
- Track character frequencies dynamically
- Optimize window expansion and shrinking
- Visualize pointer movement

---

# Example

Signal:

```text
abcabcbb
```

Possible Unique Substrings:

```text
abc
bca
cab
abc
```

Longest Length:

```text
3
```

---

# Naive Approach

Generate all substrings.

Check whether each substring contains duplicates.

---

## Complexity

Time Complexity:

O(n²)

Space Complexity:

O(n)

Not efficient for large signals.

---

# Optimized Sliding Window Approach

We maintain:

- Left Pointer
- Right Pointer
- Hash Set

The window always contains unique characters.

---

# Window Visualization

Signal:

```text
abcabcbb
```

---

### Step 1

Window:

```text
a
```

Unique

Length = 1

---

### Step 2

Window:

```text
ab
```

Unique

Length = 2

---

### Step 3

Window:

```text
abc
```

Unique

Length = 3

---

### Step 4

Next Character:

```text
a
```

Duplicate Found ❌

Shrink window from left.

Remove:

```text
a
```

Window becomes:

```text
bca
```

Continue processing.

---

# Pointer Movement

```text
Left  → Shrinks Window
Right → Expands Window
```

The window grows when characters are unique.

The window shrinks when duplicates appear.

---

# Why This Works

Every character:

- Enters the window once
- Leaves the window once

No character is processed repeatedly.

---

# Complexity Analysis

## Time Complexity

O(n)

Each character is visited at most twice.

---

## Space Complexity

O(n)

Hash set stores unique characters.

---

# Comparison

| Approach | Time Complexity |
|-----------|----------------|
| Naive | O(n²) |
| Sliding Window | O(n) |

---

# Real-World Impact

Variable Sliding Window techniques are used in:

- Cybersecurity Systems
- Network Traffic Analysis
- Data Compression
- NLP Pipelines
- Log Processing Systems
- Streaming Analytics

---

# Conclusion

The Sliding Window technique efficiently finds the longest unique sequence by dynamically expanding and shrinking the search window, reducing complexity from O(n²) to O(n).