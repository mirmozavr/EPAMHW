from hw11.hw11_t02 import Order


def test_discount_program_modifies_final_price():
    def morning_discount() -> float:
        return 0.5

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50
