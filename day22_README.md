# Day 22 - Theme Park FastPass Simulator

## Problem Statement

A futuristic theme park needs a ride scheduling system where:
- Normal visitors wait in a regular queue
- VIP visitors get priority access

The goal is to process visitors efficiently without chaos.

---

# Objectives

- Implement a normal queue system
- Add VIP priority handling
- Process users in correct order
- Visualize queue operations step-by-step

---

# Queue Concept

A queue follows:
FIFO (First In First Out)

The first user entering the queue gets processed first.

---

# System Design

## Two Queues Used

### 1. VIP Queue
Stores priority visitors.

### 2. Normal Queue
Stores regular visitors.

---

# Processing Logic

1. Process VIP queue first
2. If VIP queue empty:
   - Process normal queue

This ensures priority handling.

---

# Example Flow

## Visitors Enter

```text id="d4j8wu"
Alice  -> Normal Queue
Bob    -> Normal Queue
Charlie -> VIP Queue
Eva     -> VIP Queue