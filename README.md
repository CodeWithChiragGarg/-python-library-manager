<div align="center">

# 🧠 Library Intelligence System

### A role-based Python library engine designed with structured logic, secure access flow, and modular operations.

</div>

---

## ⚡ System Overview

This project is a **command-line Library Management System** built in Python.  
It follows a simple but intelligent architecture where operations are divided into two access layers:

```text
Admin Layer  → Controls books and users
User Layer   → Views, issues, and returns books
```

---

## 🧩 Core Logic

```python
library = {}   # Stores book records
users = {}     # Stores user credentials
```

The system uses:
- Dictionary-based data storage
- Function-driven modular design
- Role-based access control
- Password verification
- Menu-driven execution flow

---

## 🔐 Access Control

```text
Admin → Password protected
User  → User ID + auto-generated password
```

User password is generated from the last 4 digits of the user ID.

---

## 🚀 Features

```text
ADMIN CONTROL
├── Add Book
├── Remove Book
├── Display Books
├── Add User
└── Remove User

USER CONTROL
├── View Books
├── Issue Book
└── Return Book
```

---

## ▶️ Run System

```bash
python library_management.py
```

---

## 🛠️ Tech Stack

```text
Python | Functions | Dictionaries | Loops | Conditional Logic
```

---

## 👨‍💻 Developer

**Chirag Garg**  
B.Tech CSE — Data Science
