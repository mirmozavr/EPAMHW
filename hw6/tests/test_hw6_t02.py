import datetime
from unittest.mock import Mock

import pytest

from hw6.hw6_t02 import DeadlineError, Homework, HomeworkResult, Student, Teacher


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
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(homework, "Solution")


def test_do_homework_when_homework_is_active_return_homework_result():
    homework = Homework("Task", 3)
    homework.created = datetime.datetime(2000, 1, 1)
    homework.deadline = datetime.timedelta(days=100000)
    student = Student("Doe", "John")

    homework_result = student.do_homework(homework, "Solution")

    assert isinstance(homework_result, HomeworkResult)
    assert homework_result.author is student
    assert homework_result.solution == "Solution"
    assert homework_result.homework is homework


def test_teacher_is_creating_homework_instance():
    teacher = Teacher("Smith", "Adam")
    homework = teacher.create_homework("Task", 5)
    assert isinstance(homework, Homework) is True
    assert homework.text == "Task"
    assert homework.deadline == datetime.timedelta(5)


def test_check_homework_with_not_valid_homework():
    teacher = Teacher("Smith", "Adam")
    homework_result = Mock()
    homework_result.solution = "short"
    assert teacher.check_homework(homework_result) is False


def test_check_homework_with_valid_homework():
    homework = Homework("Task", 3)
    teacher = Teacher("Smith", "Adam")

    homework_result = Mock()
    homework_result.solution = "long enough"
    homework_result.homework = homework

    teacher.check_homework(homework_result)
    assert teacher.homework_done == {homework: {homework_result}}


def test_reset_all_results_from_homework_dictionary():
    Teacher.homework_done.clear()  # to clear dict from previous tests

    homework = Homework("Task", 3)
    teacher = Teacher("Smith", "Adam")

    homework_result = Mock()
    homework_result.solution = "long enough"
    homework_result.homework = homework

    teacher.check_homework(homework_result)
    teacher.reset_results()
    assert teacher.homework_done == {}


def test_reset_selected_results_from_homework_dictionary():
    """Add results for 2 homeworks, then delete results for 1st one."""
    Teacher.homework_done.clear()  # to clear dict from previous tests

    homework = Homework("Task", 3)
    homework2 = Homework("Another Task", 5)
    teacher = Teacher("Smith", "Adam")

    homework_result = Mock()
    homework_result.solution = "long enough"
    homework_result.homework = homework

    homework_result2 = Mock()
    homework_result2.solution = "another long enough"
    homework_result2.homework = homework2

    teacher.check_homework(homework_result)
    teacher.check_homework(homework_result2)
    teacher.reset_results(homework)
    assert teacher.homework_done == {homework: set(), homework2: {homework_result2}}


def test_homework_result_reject_invalid_homework():
    with pytest.raises(TypeError, match="Not a Homework object"):
        HomeworkResult("author", "invalid homework", "solution")


def test_no_repetitive_homework_results_in_homework_done():
    teacher = Teacher("Smith", "Adam")
    homework = Homework("Task", 3)
    student = Student("Doe", "John")
    teacher.reset_results()
    homework_result = student.do_homework(homework, "Solution")

    teacher.check_homework(homework_result)
    teacher.check_homework(homework_result)
    teacher.check_homework(homework_result)
    assert teacher.homework_done == {homework: {homework_result}}
