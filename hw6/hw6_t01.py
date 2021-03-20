# noqa: D205,D400
"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):  # noqa: ANN001,ANN002,ANN201
    class NewClass:
        count = 0

        def __init__(self, *args, **kwargs):  # noqa: ANN001,ANN002,ANN003
            cls.__init__(self, *args, **kwargs)
            NewClass.count += 1

        def get_created_instances(self) -> int:
            return NewClass.count

        def reset_instances_counter(self) -> int:
            temp = NewClass.count
            NewClass.count = 0
            return temp  # noqa: R504

    return NewClass


@instances_counter
class User:
    """Pass."""
