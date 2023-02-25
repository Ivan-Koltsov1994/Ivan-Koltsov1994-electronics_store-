from scr.dataclass import Product

def test_Product():
    """Тестируем класс Product"""
    prod1 = Product("Айфон", 30000, 20)
    prod1.pay_rate = 0.8
    prod1.apply_discount()
    prod1.calculate_total_price()

    assert prod1.name == "Айфон"
    assert prod1.price == 24000.0
    assert prod1.amount == 20
