from lib.school.db import SessionLocal
from lib.school.models import Student, Teacher

def main():
    session = SessionLocal()

    while True:
        print("\n=== School Management CLI ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Teacher")
        print("6. List Teachers")
        print("7. Update Teacher")
        print("8. Delete Teacher")
        print("9. Exit")

        choice = input("Enter choice: ")

        # -------- Students --------
        if choice == "1":  # Add Student
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student = Student(name=name, age=age)
            session.add(student)
            session.commit()
            print(f"✅ Student '{name}' added.")

        elif choice == "2":  # List Students
            students = session.query(Student).all()
            if students:
                for s in students:
                    print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}")
            else:
                print("No students found.")

        elif choice == "3":  # Update Student
            student_id = int(input("Enter student ID to update: "))
            student = session.query(Student).get(student_id)
            if student:
                student.name = input(f"Enter new name (current: {student.name}): ") or student.name
                age = input(f"Enter new age (current: {student.age}): ")
                student.age = int(age) if age.strip() else student.age
                session.commit()
                print("✅ Student updated.")
            else:
                print("⚠️ Student not found.")

        elif choice == "4":  # Delete Student
            student_id = int(input("Enter student ID to delete: "))
            student = session.query(Student).get(student_id)
            if student:
                session.delete(student)
                session.commit()
                print("✅ Student deleted.")
            else:
                print("⚠️ Student not found.")

        # -------- Teachers --------
        elif choice == "5":  # Add Teacher
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")

            student_id = input("Enter student ID (or leave blank): ")
            student = session.query(Student).get(int(student_id)) if student_id.strip() else None

            teacher = Teacher(name=name, subject=subject, student=student)
            session.add(teacher)
            session.commit()
            print(f"✅ Teacher '{name}' added.")

        elif choice == "6":  # List Teachers
            teachers = session.query(Teacher).all()
            if teachers:
                for t in teachers:
                    student_name = t.student.name if t.student else "None"
                    print(f"ID: {t.id}, Name: {t.name}, Subject: {t.subject}, Student: {student_name}")
            else:
                print("No teachers found.")

        elif choice == "7":  # Update Teacher
            teacher_id = int(input("Enter teacher ID to update: "))
            teacher = session.query(Teacher).get(teacher_id)
            if teacher:
                teacher.name = input(f"Enter new name (current: {teacher.name}): ") or teacher.name
                teacher.subject = input(f"Enter new subject (current: {teacher.subject}): ") or teacher.subject
                student_id = input("Enter new student ID (leave blank to keep): ")
                if student_id.strip():
                    teacher.student = session.query(Student).get(int(student_id))
                session.commit()
                print("✅ Teacher updated.")
            else:
                print("⚠️ Teacher not found.")

        elif choice == "8":  # Delete Teacher
            teacher_id = int(input("Enter teacher ID to delete: "))
            teacher = session.query(Teacher).get(teacher_id)
            if teacher:
                session.delete(teacher)
                session.commit()
                print("✅ Teacher deleted.")
            else:
                print("⚠️ Teacher not found.")

        elif choice == "9":  # Exit
            print("👋 Exiting...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
