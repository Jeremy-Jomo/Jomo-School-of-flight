# 📚 School Management CLI

A command-line interface (CLI) tool to manage students, teachers, and courses using **Python, SQLAlchemy, and Alembic**. This project demonstrates ORM-based schema design, migrations, and a user-friendly CLI workflow.

---

## 🚀 Features

- Manage **Students** (Add, List, Update, Delete)
- Manage **Teachers** (Add, List, Update, Delete)
- Manage **Courses** (Add, List, View)
- **Enroll students** into courses
- View **students enrolled in a course**
- View **courses a student is taking**

---

## ⚙️ Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/school-cli.git
   cd school-cli
   ```

2. **Install dependencies:**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Run migrations with Alembic:**
   ```bash
   alembic upgrade head
   ```

4. **Start the CLI:**
   ```bash
   python lib/school/cli.py
   ```

---

## 🖥️ CLI Menu & Workflow

When you run the program, you’ll see this menu:

```
=== School Management CLI ===
1. Add Student
2. List Students
3. Update Student
4. Delete Student
5. Add Teacher
6. List Teachers
7. Update Teacher
8. Delete Teacher
9. Add Course
10. List Courses
11. Enroll Student in Course
12. List Students in a Course
13. List Courses for a Student
14. Exit
```

### **1. Add Student**
➡️ Prompts for student name and age, then adds them to the database.
Example:
```
Enter student name: Alice
Enter age: 20
✅ Student added successfully!
```

### **2. List Students**
➡️ Displays all students in the system with their IDs.
```
ID: 1 | Name: Alice | Age: 20
ID: 2 | Name: Bob | Age: 22
```

### **3. Update Student**
➡️ Update student’s name or age. Leave blank to keep existing values.
```
Enter student ID to update: 1
Enter new name (current: Alice): Alicia
Enter new age (current: 20):
✅ Student updated.
```

### **4. Delete Student**
➡️ Removes a student from the database by ID.

---

### **5. Add Teacher**
➡️ Prompts for teacher name and subject.

### **6. List Teachers**
➡️ Displays all teachers with IDs and subjects.

### **7. Update Teacher**
➡️ Update a teacher’s name or subject.

### **8. Delete Teacher**
➡️ Removes a teacher from the system.

---

### **9. Add Course**
➡️ Create a course and assign it to a teacher.
```
Enter course name: Software Engineering
Enter teacher ID: 1
✅ Course added successfully!
```

### **10. List Courses**
➡️ Shows all courses with teacher names.

---

### **11. Enroll Student in Course**
➡️ Assigns a student to a course (many-to-many relationship).

### **12. List Students in a Course**
➡️ Displays all students currently enrolled in a specific course.

### **13. List Courses for a Student**
➡️ Shows all courses that a particular student is enrolled in.

---

### **14. Exit**
➡️ Exits the CLI program gracefully.

---

## 📂 Project Structure

```
lib/
 └── school/
      ├── cli.py        # CLI logic
      ├── models.py     # SQLAlchemy models
      ├── database.py   # DB setup & session
alembic/                # Alembic migrations
Pipfile                 # Dependencies
README.md               # Documentation
```

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **SQLAlchemy 1.4** (ORM & schema design)
- **Alembic** (migrations)
- **Pipenv** (dependency management)

---

## 📜 License

This project is for educational purposes as part of Phase 3.