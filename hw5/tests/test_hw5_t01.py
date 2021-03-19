import datetime

from hw5.hw5_t01 import Homework, Student, Teacher


def test_attributes_of_teacher_class():
    teacher = Teacher("Smith", "Adam")
    assert teacher.last_name == "Smith"
    assert teacher.first_name == "Adam"


def test_attributes_of_student_class():
    student = Student("Doe", "John")
    assert student.last_name == "Doe"
    assert student.first_name == "John"


def test_attributes_of_homework_class():
    homework = Homework("Tasks", 3)
    assert homework.text == "Tasks"
    assert homework.deadline == datetime.timedelta(3)


def test_homework_is_not_active_return_false():
    homework = Homework("Tasks", 3)
    homework.created = datetime.datetime(1980, 1, 1)
    homework.deadline = datetime.timedelta(1)
    assert homework.is_active() is False


def test_homework_is_active_return_true():
    homework = Homework("Tasks", 3)
    homework.created = datetime.datetime(2000, 1, 1)
    homework.deadline = datetime.timedelta(days=100000)
    assert homework.is_active() is True


def test_do_homework_when_homework_is_not_active_return_none():
    homework = Homework("Task", 3)
    homework.created = datetime.datetime(1980, 1, 1)
    homework.deadline = datetime.timedelta(1)
    student = Student("Doe", "John")
    assert student.do_homework(homework) is None


def test_do_homework_when_homework_is_active_return_same_homework():
    homework = Homework("Task", 3)
    homework.created = datetime.datetime(2000, 1, 1)
    homework.deadline = datetime.timedelta(days=100000)
    student = Student("Doe", "John")
    assert student.do_homework(homework) is homework


def test_teacher_is_creating_homework_instance():
    teacher = Teacher("Smith", "Adam")
    homework = teacher.create_homework("Task", 5)
    assert isinstance(homework, Homework) is True
    assert homework.text == "Task"
    assert homework.deadline == datetime.timedelta(5)
