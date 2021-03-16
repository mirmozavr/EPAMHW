import datetime

from hw5.hw5_t01 import Homework, Student, Teacher


def test_attributes_of_teacher_class():
    teacher = Teacher("Smith", "Adam")
    assert teacher.last_name, teacher.first_name == ("Smith", "Adam")


def test_attributes_of_student_class():
    student = Student("Doe", "John")
    assert student.last_name, student.first_name == ("Doe", "John")


def test_attributes_of_homework_class():
    homework = Homework("Tasks", 3)
    assert homework.text, homework.deadline == ("Tasks", 3)


def test_negative_is_active_method_of_homework_class():
    homework = Homework("Tasks", 3)
    homework.created = datetime.datetime(1980, 1, 1)
    homework.deadline = datetime.timedelta(1)
    assert homework.is_active() is False


def test_positive_is_active_method_of_homework_class():
    homework = Homework("Tasks", 3)
    homework.created = datetime.datetime(2000, 1, 1)
    homework.deadline = datetime.timedelta(days=100000)
    assert homework.is_active() is True


def test_negative_do_homework_of_student_class():
    homework = Homework("Task", 3)
    homework.created = datetime.datetime(1980, 1, 1)
    homework.deadline = datetime.timedelta(1)
    student = Student("Doe", "John")
    assert student.do_homework(homework) is None


def test_positive_do_homework_of_student_class():
    homework = Homework("Task", 3)
    homework.created = datetime.datetime(2000, 1, 1)
    homework.deadline = datetime.timedelta(days=100000)
    student = Student("Doe", "John")
    assert student.do_homework(homework) is homework


def test_create_homework_of_teacher_class():
    teacher = Teacher("Smith", "Adam")
    homework = teacher.create_homework("Task", 5)
    assert isinstance(homework, Homework) is True
    assert homework.text == "Task"
    assert homework.deadline == datetime.timedelta(5)
