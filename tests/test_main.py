from scr.dataclass import Product


def test_product_init():
    """Тестируем инициализацию и методы класса Product"""
    prod1 = Product("Айфон", 30000, 20)
    assert prod1.name == "Айфон"
    assert prod1.price == 30000
    assert prod1.amount == 20


def test_product_discount():
    """Тестируем метод применения скидки"""
    prod1 = Product("Самсунг", 30000, 20)
    prod1.pay_rate = 0.8
    prod1.apply_discount()
    assert prod1.price == 24000.0


def test_product_calculate_total():
    """Тестируем метод рассчета суммарной стоимости товара"""
    prod1 = Product("Самсунг", 30000, 20)
    assert prod1.calculate_total_price() == 600000


def test_product_name():
    """Тестируем метод возвращения имени и при не прохождении проверки длины имени возвращает инициализированное имя"""
    prod1 = Product("Самсунг", 30000, 20)
    prod1.name ='Супермегайфона'
    assert prod1.name == "Самсунг"

