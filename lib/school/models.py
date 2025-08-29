# lib/school/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.school.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    teachers = relationship("Teacher", back_populates="student")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String, nullable=False)

    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="teachers")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name='{self.name}', subject='{self.subject}')>"
