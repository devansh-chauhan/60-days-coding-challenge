# Day 50 - Superhero Academy Simulator

## Problem Statement

A futuristic academy trains superheroes with unique powers, energy levels, and combat styles.

The system should be flexible enough to support hundreds of heroes in the future.

This challenge focuses on Object-Oriented Programming (OOP).

---

# Objectives

- Create a Hero base class
- Implement inheritance
- Use method overriding
- Simulate hero battles

---

# OOP Concepts Used

## 1. Class

A class acts as a blueprint.

Example:

```python
class Hero:
```

---

## 2. Object

An object is an instance of a class.

```python
hero = Hero("FlashX", 100)
```

---

## 3. Inheritance

Child classes inherit properties from the parent class.

```python
class FireHero(Hero):
```

Benefits:

- Code Reusability
- Scalability
- Cleaner Design

---

## 4. Method Overriding

Each hero has a unique attack style.

Base Class:

```python
def attack():
    basic attack
```

Child Class:

```python
def attack():
    special attack
```

The child implementation replaces the parent version.

---

# Class Hierarchy

Hero
│
├── SpeedHero
│
├── FireHero
│
└── IceHero

---

# Battle Simulation

Heroes:

FlashX → Lightning Dash

Inferno → Fire Blast

Glacier → Frost Strike

Each hero uses its own attack implementation.

---

# Why OOP?

Without OOP:

- Duplicate code
- Hard to maintain
- Difficult to scale

With OOP:

- Reusable code
- Better organization
- Easy to add new heroes

Example:

```python
class WaterHero(Hero):
```

Can be added without changing existing code.

---

# Complexity Analysis

Displaying hero info:

Time Complexity:

O(n)

where n = number of heroes

Space Complexity:

O(n)

for storing hero objects

---

# Real-World Impact

Object-Oriented Programming is used in:

- Game Development
- Banking Systems
- Enterprise Applications
- Mobile Apps
- Web Applications
- Simulation Engines

---

# Conclusion

OOP helps build scalable and maintainable systems by organizing data and behavior into reusable classes. Inheritance and method overriding allow new features to be added with minimal code changes.