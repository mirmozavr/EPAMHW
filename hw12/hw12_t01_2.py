from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hw12.hw12_t01 import Homework, HomeworkResult, Student, Teacher

engine = create_engine("sqlite+pysqlite:///main.db", future=True)
session = sessionmaker(bind=engine)()

student = Student(first_name="John", last_name="Woo")
teacher = Teacher(first_name="Jet", last_name="Lee")
homework = Homework(
    text="Do the task",
    created=datetime(2021, 3, 15),
    deadline=timedelta(10),
    teacher_firstname="Jet",
    teacher_lastname="Lee",
)
homework_result = HomeworkResult(
    solution="Task",
    created=datetime(2021, 3, 20),
    author_firstname="John",
    author_lastname="Woo",
    homework_text="Do the task",
    homework_created=datetime(2021, 3, 15),
)

session.add_all([student, teacher, homework, homework_result])


session.commit()
