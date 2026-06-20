# Day 48 - Alien Language Translator

## Problem Statement

Scientists intercepted messages from an alien civilization.

Your mission is to determine the minimum number of edits required to transform one message into another.

Allowed Operations:

1. Insert
2. Delete
3. Replace

Each operation costs 1 unit of translation energy.

This is the classic:

Edit Distance (Levenshtein Distance)

problem.

---

# Objectives

- Solve Edit Distance
- Build DP Table Visualization
- Track Insert/Delete/Replace Costs
- Compare Recursive vs Dynamic Programming Approaches

---

# Example

Word 1:

horse

Word 2:

ros

Goal:

Transform:

horse → ros

Minimum Operations:

3

---

# Operations Example

horse

Remove 'h'

orse

Replace 'r' with 'o'

rose

Remove 'e'

ros

Total Cost = 3

---

# Recursive Approach

For every mismatch we have 3 choices:

Insert

Delete

Replace

Formula:

f(i,j) = 1 + min(

Insert,

Delete,

Replace

)

If characters match:

f(i,j) = f(i-1,j-1)

---

# Problem With Recursion

Many states are recalculated repeatedly.

Example:

f(5,3)

├── f(4,3)

├── f(5,2)

└── f(4,2)

The same subproblems appear multiple times.

Time complexity becomes exponential.

---

# Dynamic Programming Solution

Store results of subproblems in a table.

DP Cell Meaning:

dp[i][j]

=

Minimum edits required to convert:

word1[0:i]

into

word2[0:j]

---

# DP Table Visualization

Convert:

horse → ros

```text
      ""  r  o  s
""    0  1  2  3
h     1  1  2  3
o     2  2  1  2
r     3  2  2  2
s     4  3  3  2
e     5  4  4  3
```

Final Answer:

```text
dp[5][3] = 3
```

---

# State Transition

If characters match:

```text
dp[i][j] = dp[i-1][j-1]
```

Otherwise:

```text
dp[i][j] = 1 + min(
Insert,
Delete,
Replace
)
```

---

# Recursive vs DP

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Recursion | O(3^n) | O(n) |
| Dynamic Programming | O(m × n) | O(m × n) |

---

# Why DP Is Better

Recursion:

Repeated calculations

Dynamic Programming:

Solve once

Store result

Reuse result

Much faster for larger strings.

---

# Edge Cases

### Same Strings

```text
abc
abc
```

Answer:

```text
0
```

---

### Empty String

```text
""
abc
```

Answer:

```text
3
```

---

### Completely Different Strings

```text
abc
xyz
```

Answer:

```text
3
```

---

# Real-World Impact

Edit Distance algorithms are used in:

- Spell Checkers
- Autocorrect Systems
- DNA Sequence Matching
- NLP Applications
- Search Engines
- Plagiarism Detection

---

# Conclusion

The Edit Distance problem demonstrates how Dynamic Programming efficiently solves complex transformation problems by storing intermediate results and avoiding redundant computation.