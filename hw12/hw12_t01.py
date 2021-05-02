"""
Using ORM framework of your choice, create models classes created in Homework 6 (Teachers, Students, Homework and others).

Target database should be sqlite (filename main.db localted in current directory)
 - ORM framework should support migrations.
Utilizing that framework capabilities, create

    a migration file, creating all necessary database structures.
    a migration file (separate) creating at least one record in each created database table

    (*) optional task: write standalone script (get_report.py)
    that retrieves and stores the following information into CSV file report.csv

        for all done (completed) homeworks:
            Student name (who completed homework) Creation date Teacher name who created homework

Utilize ORM capabilities as much as possible, avoiding executing raw SQL queries.
"""

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKeyConstraint,
    Interval,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite+pysqlite:///main.db", echo=True, future=True)
Base = declarative_base()


class Homework(Base):
    __tablename__ = "homework"
    text = Column(String, primary_key=True)
    created = Column(DateTime, primary_key=True)
    deadline = Column(Interval)
    teacher_firstname = Column(String)
    teacher_lastname = Column(String)

    def __str__(self):
        return f"HW: {self.text}, created {self.created.strftime('%d/%m/%Y')}, deadline {self.deadline.days} days"


class Student(Base):
    __tablename__ = "student"
    first_name = Column(String, primary_key=True)
    last_name = Column(String, primary_key=True)
    middle_name = Column(String, primary_key=True, server_default="Bob")

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"


class Teacher(Base):
    __tablename__ = "teacher"
    first_name = Column(String, primary_key=True)
    last_name = Column(String, primary_key=True)

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"


class HomeworkResult(Base):
    __tablename__ = "homeworkresult"
    solution = Column(String, primary_key=True)
    created = Column(DateTime, primary_key=True)
    author_firstname = Column(String)
    author_lastname = Column(String)
    homework_text = Column(String)
    homework_created = Column(DateTime)
    __table_args__ = (
        ForeignKeyConstraint(
            (homework_text, homework_created),
            (Homework.text, Homework.created),
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            (author_firstname, author_lastname),
            (Student.first_name, Student.last_name),
            ondelete="CASCADE",
        ),
    )

    def __str__(self):
        return f"HW result: {self.solution}"


"""Base.metadata.create_all(bind=engine)"""
