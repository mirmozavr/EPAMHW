"""
Необходимо создать 3 класса и взаимосвязь между ними.

(Student, Teacher, Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Optional


class Homework:
    """Homework class."""

    def __init__(self, text: str, deadline_days: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline_days)
        self.created = datetime.datetime.today()

    def is_active(self) -> bool:
        """Check if homework is still active."""
        return datetime.datetime.today() < self.created + self.deadline


class Student:
    """Student class."""

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework) -> Optional[Homework]:
        """Check if not late for homework."""
        if homework.is_active():
            return homework
        print("You are late")  # noqa: T001,R503


class Teacher:
    """Teacher class."""

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Create a Homework instance."""
        return Homework(text, deadline)
