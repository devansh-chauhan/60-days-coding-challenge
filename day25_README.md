# Day 25 - The Infinite Maze Trap

## Problem Statement

A game developer accidentally created a maze where some paths loop forever.

The goal is to detect whether players are trapped inside an infinite cycle before the game launches.

---

# Objectives

- Simulate maze paths using linked lists
- Detect cycles using fast and slow pointers
- Test multiple maze configurations
- Understand why cycle detection matters

---

# Linked List Representation

Maze paths are represented as linked lists.

Example:

```text id="m6z2vp"
A -> B -> C -> D -> None