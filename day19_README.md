# Day 19 - Min Stack

## Problem Statement

A futuristic vault stores temperature readings every second.

The goal is to build a system that can instantly return the minimum recorded temperature at any moment.

---

# Objectives

- Build a custom Min Stack
- Support:
  - push()
  - pop()
  - getMin()
- Maintain O(1) minimum lookup
- Test using random inputs

---

# What is a Min Stack?

A Min Stack is a special stack that supports retrieving the minimum element instantly.

Unlike a normal stack:
- push → O(1)
- pop → O(1)
- getMin → O(1)

---

# Approach

We use:
1. Main Stack
2. Min Stack

## Main Stack
Stores all values.

## Min Stack
Tracks minimum values only.

Whenever:
- A smaller value is pushed → store it in min stack
- Minimum value is popped → remove from min stack

---

# Example

## Push Operations

```text id="p5q1st"
Push 5
Min = 5

Push 3
Min = 3

Push 7
Min = 3