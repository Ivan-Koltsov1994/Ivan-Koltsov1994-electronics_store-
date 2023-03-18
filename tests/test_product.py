from scr.product import Product
import pytest


def test_product_init():
    """Тестируем инициализацию и методы класса Product"""
    prod1 = Product("Айфон", 30000, 20)
    assert prod1.name == "Айфон"
    assert prod1.price == 30000
    assert prod1.amount == 20


def test_product_repr():
    """Тестируем метод __repr__  класса Product"""
    item = Product('Полиграф', 1600, 4)
    assert item.__repr__() == 'Товар: Полиграф, цена: 1600, в наличии: 4'


def test_product_str():
    """Тестируем метод __str__  класса Product"""
    item = Product('Полиграф', 1600, 3)
    assert item.__str__() == 'Товар: Полиграф'


def test_product_discount():
    """Тестируем метод применения скидки в классе Product"""
    prod1 = Product("Самсунг", 30000, 20)
    prod1.pay_rate = 0.8
    prod1.apply_discount()
    assert prod1.price == 24000.0


def test_product_calculate_total():
    """Тестируем метод расчета суммарной стоимости товара в классе Product"""
    prod1 = Product("Самсунг", 30000, 20)
    assert prod1.calculate_total_price() == 600000


def test_product_name():
    """Тестируем метод возвращения имени и при не прохождении проверки длины имени возвращает инициализированное имя
    в классе Product """
    prod1 = Product("Cмартфорн", 30000, 20)
    prod1.name = "Cамсунг"
    assert prod1.name == "Cамсунг"
    with pytest.raises(Exception):
        prod1.name = 'Длина названия товара больше 10 символов'


def test_product_instantiate_from_csv():
    """Тестируем, что метод адекватно обрабатывает данные в массив в классе Product """
    path = "items.csv"
    Product.instantiate_from_csv(path)
    item1 = Product.all[0]
    assert item1 is not None


def test_product_is_integer_num():
    """Тестируем статический метод определения целого числа в методе класса Product"""

    assert Product.is_integer_num(10) is True
    assert Product.is_integer_num(5.0) is True
    assert Product.is_integer_num(7.5) is False


def test_product_file_not_found_error():
    """Тестируем ожидаемую обработку исключения FileNotFoundError в связи с отсутствием файла"""
    path = '../items.csv'
    assert Product.instantiate_from_csv(path) == print(f"По указанному пути  файл item.csv отсутствует")


def test_product_instantiate_csv_error():
    """Тестируем ожидаемую обработка исключения InstantiateCSVError, так как файл поврежден"""
    path = 'items_err.csv'
    assert Product.instantiate_from_csv(path) == print("Файл item.csv поврежден")
