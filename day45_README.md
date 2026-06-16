# Day 45 - Emergency Room Simulator

## Problem Statement

A hospital emergency room must prioritize patients based on the severity of their condition.

Patients with more critical conditions should be treated before less severe cases.

This challenge demonstrates how Priority Queues work.

---

# Objectives

- Build a patient priority system
- Use a heap-based priority queue
- Process highest-priority patients first
- Simulate incoming emergency requests

---

# What is a Priority Queue?

Unlike a normal queue:

```text
First In → First Out (FIFO)
```

A Priority Queue processes elements based on priority.

Higher Priority:

```text
Processed First
```

---

# Example

Patients Arrive:

```text
John   → Severity 3
Emma   → Severity 8
David  → Severity 5
Sophia → Severity 10
```

Treatment Order:

```text
Sophia → 10
Emma   → 8
David  → 5
John   → 3
```

---

# Why Use a Heap?

Python's heapq module provides an efficient heap implementation.

Operations:

| Operation | Complexity |
|------------|------------|
| Insert | O(log n) |
| Remove Highest Priority | O(log n) |
| Peek Highest Priority | O(1) |

---

# Visualization

Incoming Patients:

```text
John (3)
Emma (8)
David (5)
Sophia (10)
```

Priority Queue:

```text
       Sophia(10)
       /       \
   Emma(8)   David(5)
    /
John(3)
```

---

Processing:

```text
Sophia
↓
Emma
↓
David
↓
John
```

---

# Why Negative Values?

Python's heapq is a Min Heap.

It always removes the smallest value first.

To simulate a Max Heap:

```python
heapq.heappush(heap, (-priority, item))
```

Higher severity becomes higher priority.

---

# Edge Cases

### No Patients

```text
Queue Empty
```

Output:

```text
No patients waiting.
```

---

### Same Severity

```text
Patient A → 5
Patient B → 5
```

Both can be processed according to heap order.

---

# Complexity Analysis

## Adding Patient

```text
O(log n)
```

---

## Treating Patient

```text
O(log n)
```

---

## Space Complexity

```text
O(n)
```

where n = number of patients.

---

# Real-World Impact

Priority Queues are used in:

- Hospital Scheduling Systems
- CPU Scheduling
- Cloud Resource Allocation
- Network Routing
- Event Processing Systems
- Operating Systems

---

# Conclusion

Priority Queues ensure that the most important tasks are processed first. By using heaps, we achieve efficient insertion and removal while maintaining correct priority order.