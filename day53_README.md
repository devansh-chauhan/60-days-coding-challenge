# Day 53 - Secret Vault Database

## Problem Statement

A cybersecurity company stores sensitive vault records inside a secure database.

The system must support:

* Create records
* Read records
* Update records
* Delete records

This challenge introduces database fundamentals using SQLite.

---

## Objectives

* Create a SQLite database
* Implement CRUD operations
* Store vault records
* Execute efficient SQL queries

---

## Database Schema

Table: vault_records

| Column      | Type                |
| ----------- | ------------------- |
| id          | INTEGER PRIMARY KEY |
| secret_name | TEXT                |
| secret_code | TEXT                |

---

## CRUD Operations

### Create

Insert new vault records.

```sql
INSERT INTO vault_records
(secret_name, secret_code)
VALUES ('Project X', 'A123');
```

### Read

Retrieve all records.

```sql
SELECT * FROM vault_records;
```

### Update

Modify existing records.

```sql
UPDATE vault_records
SET secret_code='X999'
WHERE id=1;
```

### Delete

Remove records.

```sql
DELETE FROM vault_records
WHERE id=2;
```

### Search

Find specific records.

```sql
SELECT *
FROM vault_records
WHERE secret_name='Project X';
```

---

## Architecture

Application
|
v
SQLite Database
|
v
vault_records Table

CRUD Operations

Create
Read
Update
Delete

---

## Why SQLite?

* Lightweight
* No server setup
* Easy to learn
* Widely used for local applications

---

## Complexity Analysis

Insert: O(1)

Search (Indexed Primary Key): O(log n)

Update: O(log n)

Delete: O(log n)

Space Complexity: O(n)

where n = number of records.

---

## Real-World Applications

Databases power:

* Banking Systems
* Healthcare Platforms
* E-commerce Websites
* Social Media Platforms
* Enterprise Applications

---

## Conclusion

Databases are the foundation of modern software systems. SQLite provides an excellent introduction to storing, retrieving, and managing structured data efficiently.
