# Day 18 - Ancient Bracket Decoder

## Problem Statement

An ancient civilization stored messages using nested brackets.

The goal is to verify whether a message is properly balanced before it can be decoded.

---

# Objective

- Validate bracket sequences
- Handle multiple bracket types
- Test invalid edge cases
- Understand stack behavior

---

# Bracket Types

Supported brackets:
- ()
- {}
- []

---

# Approach — Using Stack

A stack follows:
LIFO (Last In First Out)

## Algorithm

1. Traverse each character
2. If opening bracket:
   - Push into stack
3. If closing bracket:
   - Check top of stack
   - Validate matching pair
4. At the end:
   - Stack should be empty

---

# Example

Input:

```python
{[()]}