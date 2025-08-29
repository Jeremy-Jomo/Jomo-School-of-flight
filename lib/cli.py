from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

my_engine = create_engine("sqlite:///student.db")
my_session= sessionmaker(bind=my_engine)
working_session = my_session()
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}', age={self.age})"




Base.metadata.create_all(bind=my_engine)
student1=Student(name="Alice", age=20)
student2=Student(name="Bob", age=22)
student3=Student(name="jomo",age=20)


working_session.add(student1)
working_session.add_all([student2,student3])
working_session.commit()
all_students=working_session.query(Student).all()
print(all_students)