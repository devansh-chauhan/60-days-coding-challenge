# Day 51 - Food Delivery Empire

## Problem Statement

A startup is launching a food delivery platform.

The system must manage:

- Users
- Restaurants
- Orders
- Delivery Tracking

This project simulates a mini backend architecture similar to platforms like Swiggy and Zomato.

---

# Objectives

- Design core entities
- Model relationships
- Simulate order flow
- Document architecture decisions

---

# Core Entities

## User

Represents a customer.

Responsibilities:

- Place orders
- Track orders

---

## Restaurant

Represents food providers.

Responsibilities:

- Receive orders
- Prepare food

---

## Delivery Partner

Represents delivery agents.

Responsibilities:

- Pick up orders
- Deliver orders

---

## Order

Represents an active transaction.

Stores:

- Order ID
- Customer
- Restaurant
- Item
- Status

---

# Architecture Diagram

User
 |
 | Places Order
 ↓
Order
 |
 |
 ↓
Restaurant
 |
 | Prepares Food
 ↓
Delivery Partner
 |
 | Delivers Order
 ↓
Customer

---

# Order Lifecycle

Step 1

Placed

↓

Step 2

Preparing

↓

Step 3

Out for Delivery

↓

Step 4

Delivered

---

# Why This Design?

Each class has a single responsibility.

Benefits:

- Easy maintenance
- Better scalability
- Reusable components

Example:

Adding payment support later:

```python
class Payment:
    pass
```

No major changes required.

---

# Engineering Decisions

## Encapsulation

Each object manages its own behavior.

Example:

```python
restaurant.prepare_order()
```

---

## Separation of Concerns

User:

Places orders

Restaurant:

Prepares food

Delivery Partner:

Handles logistics

---

## Scalability

Future additions:

- Payments
- Multiple restaurants
- Ratings
- Live tracking
- Notifications

Can be added easily.

---

# Complexity Analysis

Order Creation:

O(1)

Order Tracking:

O(1)

Status Update:

O(1)

Space Complexity:

O(n)

where n = number of orders.

---

# Real-World Impact

System design concepts like these are used in:

- Swiggy
- Zomato
- Uber Eats
- Amazon Logistics
- Foodpanda

---

# Conclusion

Building systems using proper entities and relationships creates scalable software that can handle growing business requirements.