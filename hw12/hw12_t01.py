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

from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Interval, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Homework(Base):
    __tablename__ = "homework"
    text = Column(String, primary_key=True)
    created = Column(DateTime, primary_key=True)
    deadline = Column(Interval)


class Student(Base):
    __tablename__ = "student"
    first_name = Column(String, primary_key=True)
    last_name = Column(String, primary_key=True)


class Teacher(Base):
    __tablename__ = "teacher"
    first_name = Column(String, primary_key=True)
    last_name = Column(String, primary_key=True)


class HomeworkResult(Base):
    solution = Column(String, primary_key=True)
    created = Column(DateTime, primary_key=True)
    author_firstname = Column(String)
    author_lastname = Column(String)
    homework_text = Column(String)
    homework_created = Column(DateTime)
    __table_args__ = (
        ForeignKeyConstraint(
            (homework_text, homework_created, author_firstname, author_lastname),
            (Homework.text, Homework.created, Student.first_name, Student.last_name),
            ondelete="CASCADE",
        ),
    )
