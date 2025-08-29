from lib.school.db import SessionLocal
from lib.school.models import Student, Teacher, Course

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
        print("9. Add Course")
        print("10. List Courses")
        print("11. Enroll Student in Course")
        print("12. List Students in a Course")
        print("13. List Courses for a Student")
        print("14. Exit")

        choice = input("Enter choice: ")

        # -------- Students --------
        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            student = Student(name=name, age=age)
            session.add(student)
            session.commit()
            print(f"✅ Student '{name}' added.")

        elif choice == "2":
            students = session.query(Student).all()
            if students:
                for s in students:
                    print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}")
            else:
                print("No students found.")

        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            student = session.get(Student, student_id)
            if student:
                student.name = input(f"Enter new name (current: {student.name}): ") or student.name
                age = input(f"Enter new age (current: {student.age}): ")
                student.age = int(age) if age.strip() else student.age
                session.commit()
                print("✅ Student updated.")
            else:
                print("⚠️ Student not found.")

        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            student = session.get(Student, student_id)
            if student:
                session.delete(student)
                session.commit()
                print("✅ Student deleted.")
            else:
                print("⚠️ Student not found.")

        # -------- Teachers --------
        elif choice == "5":
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            teacher = Teacher(name=name, subject=subject)
            session.add(teacher)
            session.commit()
            print(f"✅ Teacher '{name}' added.")

        elif choice == "6":
            teachers = session.query(Teacher).all()
            if teachers:
                for t in teachers:
                    print(f"ID: {t.id}, Name: {t.name}, Subject: {t.subject}")
            else:
                print("No teachers found.")

        elif choice == "7":
            teacher_id = int(input("Enter teacher ID to update: "))
            teacher = session.get(Teacher, teacher_id)
            if teacher:
                teacher.name = input(f"Enter new name (current: {teacher.name}): ") or teacher.name
                teacher.subject = input(f"Enter new subject (current: {teacher.subject}): ") or teacher.subject
                session.commit()
                print("✅ Teacher updated.")
            else:
                print("⚠️ Teacher not found.")

        elif choice == "8":
            teacher_id = int(input("Enter teacher ID to delete: "))
            teacher = session.get(Teacher, teacher_id)
            if teacher:
                session.delete(teacher)
                session.commit()
                print("✅ Teacher deleted.")
            else:
                print("⚠️ Teacher not found.")

        # -------- Courses --------
        elif choice == "9":
            name = input("Enter course name: ")
            teacher_id = int(input("Enter teacher ID for this course: "))
            teacher = session.get(Teacher, teacher_id)
            if teacher:
                course = Course(name=name, teacher=teacher)
                session.add(course)
                session.commit()
                print(f"✅ Course '{name}' added with teacher {teacher.name}.")
            else:
                print("⚠️ Teacher not found.")

        elif choice == "10":
            courses = session.query(Course).all()
            if courses:
                for c in courses:
                    teacher_name = c.teacher.name if c.teacher else "None"
                    print(f"ID: {c.id}, Name: {c.name}, Teacher: {teacher_name}")
            else:
                print("No courses found.")

        elif choice == "11":
            student_id = int(input("Enter student ID: "))
            course_id = int(input("Enter course ID: "))
            student = session.get(Student, student_id)
            course = session.get(Course, course_id)
            if student and course:
                course.students.append(student)
                session.commit()
                print(f"✅ Student {student.name} enrolled in {course.name}.")
            else:
                print("⚠️ Invalid student or course ID.")

        elif choice == "12":
            course_id = int(input("Enter course ID: "))
            student = session.get(Student, student_id)
            if course:
                if course.students:
                    print(f"Students in {course.name}:")
                    for s in course.students:
                        print(f"- {s.name} (ID {s.id})")
                else:
                    print("No students enrolled in this course.")
            else:
                print("⚠️ Course not found.")

        elif choice == "13":
            student_id = int(input("Enter student ID: "))
            course = session.get(Course, course_id)
            if student:
                if student.courses:
                    print(f"Courses for {student.name}:")
                    for c in student.courses:
                        print(f"- {c.name} (ID {c.id})")
                else:
                    print("Student not enrolled in any courses.")
            else:
                print("⚠️ Student not found.")

        elif choice == "14":
            print("👋 Exiting..." \
            "BYEEEE👋👋👋👋")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
