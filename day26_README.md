# Day 26 - The Secret Message Decoder

## Problem Statement

An encrypted communication system stores messages in a linked chain.

One corrupted message must be removed before transmission.

The challenge is to remove the nth node from the end using a single traversal approach.

---

# Objectives

- Build a linked list message chain
- Remove nth node from end
- Optimize using two pointers
- Understand single-pass traversal

---

# Example

Original Chain:

Msg1 -> Msg2 -> Msg3 -> Msg4 -> Msg5 -> None

Remove 2nd node from end

Result:

Msg1 -> Msg2 -> Msg3 -> Msg5 -> None

---

# Two Pointer Strategy

We use:

1. Fast Pointer
2. Slow Pointer

### Step 1

Move fast pointer (n + 1) steps ahead.

Example:

Slow = Dummy
Fast = Dummy

After moving fast:

Slow -> Dummy
Fast -> Msg3

### Step 2

Move both pointers together.

When fast reaches the end:

- Slow will be just before the node to remove.

### Step 3

Update links:

slow.next = slow.next.next

Node is removed.

---

# Visualization

Original:

Dummy -> M1 -> M2 -> M3 -> M4 -> M5

Remove 2nd from end (M4)

After Removal:

Dummy -> M1 -> M2 -> M3 -> M5

---

# Why Single-Pass Traversal Matters

Naive Approach:

1. Traverse list to count nodes
2. Traverse again to remove node

Total:
- Two passes

Optimized Approach:

- Fast and slow pointers
- Only one traversal

Benefits:
- Faster execution
- Lower latency
- Better for large datasets

---

# Complexity Analysis

## Time Complexity

O(n)

Single traversal through the linked list.

## Space Complexity

O(1)

Only two pointers used.

---

# Real-World Impact

This optimization is useful in:

- Network packet processing
- Real-time communication systems
- Streaming applications
- Database engines
- Memory-efficient systems

---

# Conclusion

The two-pointer technique allows efficient node removal in one pass, making linked list operations faster and more scalable.