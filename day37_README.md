# Day 37 - Cookie Distribution Crisis

## Problem Statement

A festival organizer must distribute cookies to children.

Each child has a greed factor representing the minimum cookie size needed to make them happy.

Each cookie has a size.

The goal is to maximize the number of satisfied children.

This is the classic:

**Assign Cookies**

problem.

---

# Objectives

- Solve Assign Cookies
- Sort greed factors and cookie sizes
- Maximize satisfied children
- Understand greedy decision-making

---

# Example

Greed Factors:

```text
[1, 2, 3]
```

Cookie Sizes:

```text
[1, 1]
```

Result:

```text
1 Happy Child
```

---

# Greedy Strategy

## Step 1

Sort greed factors:

```text
[1, 2, 3]
```

Sort cookie sizes:

```text
[1, 1]
```

---

## Step 2

Try satisfying the least greedy child first.

Why?

Because smaller cookies can satisfy smaller requirements.

This leaves larger cookies available for greedier children later.

---

# Visualization

Children:

```text
[1, 2, 3]
```

Cookies:

```text
[1, 1]
```

---

Child Needs:

```text
1
```

Cookie Available:

```text
1
```

Satisfied ✅

---

Next Child Needs:

```text
2
```

Cookie Available:

```text
1
```

Not Enough ❌

---

No More Cookies.

Result:

```text
1 Happy Child
```

---

# Why Greedy Works

Always satisfy the child with the smallest requirement first.

If a small cookie can satisfy a child:

- Use it immediately
- Save larger cookies for larger requirements

This guarantees the maximum number of satisfied children.

---

# Another Example

Children:

```text
[1, 2]
```

Cookies:

```text
[1, 2, 3]
```

Assignments:

```text
1 → Child 1
2 → Child 2
```

Result:

```text
2 Happy Children
```

---

# Complexity Analysis

## Sorting

Greed Array:

O(n log n)

Cookie Array:

O(m log m)

---

## Matching Process

O(n + m)

---

## Overall Complexity

Time Complexity:

O(n log n + m log m)

Space Complexity:

O(1)

(ignoring sorting space)

---

# Real-World Impact

Greedy algorithms are used in:

- Resource Allocation
- Job Scheduling
- Network Routing
- Logistics Planning
- CPU Scheduling
- Load Balancing Systems

---

# Why This Scales

Instead of trying every possible assignment:

Brute Force:

```text
Exponential possibilities
```

Greedy:

```text
Sort once
Assign efficiently
```

Much faster for large datasets.

---

# Conclusion

The greedy approach maximizes satisfied children by always making the locally optimal choice—matching the smallest suitable cookie with the least greedy child first.