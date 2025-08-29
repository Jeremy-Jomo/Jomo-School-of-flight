# 🏫 School Management CLI

A simple **command-line interface (CLI) school management system** built with **Python** and **SQLAlchemy ORM**.
This project allows you to manage students, teachers, and courses, including enrollment relationships between them.

---

## ✨ Features

- **Student Management**
  - Add, list, update, and delete students
- **Teacher Management**
  - Add, list, update, and delete teachers
- **Course Management**
  - Add and list courses with assigned teachers
- **Enrollment**
  - Enroll students in courses
  - View all students in a course
  - View all courses for a student

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **SQLAlchemy 1.4** (ORM + SQLite backend)
- **SQLite** (default database)

---

## 📂 Project Structure

```
.
├── lib/
│   └── school/
│       ├── cli.py       # Main CLI application
│       ├── db.py        # Database engine & session
│       └── models.py    # ORM models (Student, Teacher, Course, enrollment)
├── README.md            # Project documentation
└── requirements.txt     # Dependencies
```

---

## ⚙️ Setup & Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/school-management-cli.git
cd school-management-cli
```

2. **Create virtual environment (recommended)**

```bash
python3 -m venv venv
source venv/bin/aivate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Initialize the database**

The database will be automatically created (`student.db`) on first run.

---

## ▶️ Usage

Run the CLI:

```bash
python lib/school/cli.py
```
