"""
Optional task.

(*) optional task: write standalone script (get_report.py)
that retrieves and stores the following information into CSV file report.csv

    for all done (completed) homeworks:
        Student name (who completed homework) Creation date Teacher name who created homework

Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hw12.hw12_t01 import Homework, HomeworkResult, Student, Teacher

engine = create_engine("sqlite+pysqlite:///main.db", future=True)
session = sessionmaker(bind=engine)()

query = (
    session.query(
        Student.first_name,
        Student.last_name,
        HomeworkResult.solution,
        Homework.created,
        Teacher.first_name,
        Teacher.last_name,
    )
    .filter(
        HomeworkResult.homework_text == Homework.text,
        HomeworkResult.author_lastname == Student.last_name,
        Homework.teacher_lastname == Teacher.last_name,
        Homework.teacher_firstname == Teacher.first_name,
    )
    .all()
)

with open("report.csv", "w") as file:
    for item in query:
        file.write(",".join(map(str, item)) + "\n")
