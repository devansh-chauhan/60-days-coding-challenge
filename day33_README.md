# Day 33 - Defective Robot Factory

## Problem Statement

A robot factory accidentally released defective robots.

Versions are released sequentially:

Version 1 → Good
Version 2 → Good
Version 3 → Good
Version 4 → Bad
Version 5 → Bad
Version 6 → Bad

Once a version becomes defective, all subsequent versions are also defective.

The goal is to find the FIRST bad version while minimizing expensive API calls.

---

# Objectives

- Solve First Bad Version problem
- Minimize API calls
- Track search boundaries carefully
- Handle edge cases correctly

---

# Available API

```python
isBadVersion(version)
```