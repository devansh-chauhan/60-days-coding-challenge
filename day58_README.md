# Day 58 - Mock Interview Arena

## Overview

This challenge simulates a real software engineering interview consisting of three sections:

* Data Structures & Algorithms
* Debugging
* System Design

---

## Part 1 – DSA Challenge

### Problem

Validate whether a string containing brackets is balanced.

### Approach

* Use a stack.
* Push opening brackets.
* Match closing brackets.
* Return true only if the stack is empty at the end.

**Complexity**

* Time: O(n)
* Space: O(n)

---

## Part 2 – Debugging Challenge

### Bug

The algorithm initialized the maximum value with `0`.

This fails for arrays containing only negative numbers.

### Fix

Initialize using the first element of the array.

---

## Part 3 – System Design

### Scenario

Design a URL Shortener.

### Components

* Client
* Backend API
* URL Generator
* Database
* Redirect Service

### Request Flow

User

↓

Backend

↓

Generate Short Code

↓

Store Mapping

↓

Return Short URL

### Future Enhancements

* Analytics dashboard
* Rate limiting
* Caching
* Distributed database
* Load balancing

---

## Key Learnings

* Interviews assess problem-solving, communication, and design skills.
* Clear explanations are as important as correct code.
* Considering edge cases is essential during debugging.
* System design requires balancing scalability, simplicity, and maintainability.

## Technologies Used

* Python
* Stack (DSA)
* Basic debugging techniques
* High-level system design concepts
