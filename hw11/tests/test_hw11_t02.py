from hw11.hw11_t02 import Order


def test_multiplier_discount():
    def morning_discount(order):
        return 0.5 * order.price

    order = Order(100, morning_discount)
    assert order.final_price() == 50


def test_subtraction_discount():
    def minus_one_point(order):
        return order.price - 1

    order = Order(50, minus_one_point)
    assert order.final_price() == 49.0


def test_new_strategy():
    def minus_one_point_each_order(order):
        order.discount += 1
        return max(10, order.price - order.discount)

    order = Order(13, minus_one_point_each_order)
    assert order.final_price() == 12
    assert order.final_price() == 11
    assert order.final_price() == 10
    assert order.final_price() == 10
