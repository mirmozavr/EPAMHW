"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции.

(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""

import datetime
from collections import defaultdict
from typing import Any, Optional, Union


class Homework:
    """Homework class."""

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.today()

    def is_active(self) -> bool:
        """Check if homework is still active."""
        return datetime.datetime.today() < self.created + self.deadline


class DeadlineError(Exception):
    """Custom exception class."""


class Person:
    """Person class."""

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """Student class."""

    def do_homework(self, homework: Homework, solution: Union[str, int]) -> Any:
        """Check if not late for homework."""
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        else:
            raise DeadlineError("You are late")


class HomeworkResult:
    """HomeworkResult class."""

    def __init__(self, author: Student, homework: Homework, solution: Union[str, int]):
        self.author = author
        self.solution = str(solution)
        self.created = datetime.datetime.now()
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise ValueError("You gave not a Homework object")


class Teacher(Person):
    """Teacher class."""

    homework_done = defaultdict(set)

    def create_homework(self, text: str, deadline: int) -> Homework:
        """Create a Homework instance."""
        return Homework(text, deadline)

    def check_homework(self, hw_result: HomeworkResult) -> bool:
        """Check if homework is done."""
        if len(hw_result.solution) > 5:
            Teacher.homework_done[hw_result.homework].add(hw_result)
            return True
        return False

    def reset_results(self, reset_hw: Optional[Homework] = None) -> None:
        """Reset all or selected Homework results."""
        if reset_hw is None:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done[reset_hw].clear()
