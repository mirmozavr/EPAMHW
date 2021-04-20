from hw11.hw11_t02 import Order


def test_multiplier_discount():
    def morning_discount(order):
        order.discount = 0.5 * order.price

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50


def test_subtraction_discount():
    def minus_one_point(order):
        order.discount = 1

    order_1 = Order(50, minus_one_point)
    assert order_1.final_price() == 49.0
