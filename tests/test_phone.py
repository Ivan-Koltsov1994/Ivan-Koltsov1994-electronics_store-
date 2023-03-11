from scr.phone import Phone
import pytest


def test_phone_init():
    """Тестируем инициализацию и методы класса Phone"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000
    assert phone1.amount == 5
    assert  phone1.number_of_sim == 2


def test_phone_repr():
    """Тестируем метод __repr__  класса Phone"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.__repr__() == 'Марка телефона: iPhone 14, цена: 120000, в наличии: 5, количество сим-карт: 2 '


def test_phone_str():
    """Тестируем метод __str__  класса Phone"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.__str__() == 'Товар: iPhone 14'

def test_phone_number_of_sim():
    """Тестируем метод метод определения количества Сим- карт адектватно работает в классе Phone """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    with pytest.raises(Exception):
        phone1.number_of_sim = '"Количество физических SIM-карт должно быть целым числом больше нуля."'

def test_phone_add():
    """Тестируем метод __add__"""
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 14", 120_000, 5, 3)
    assert phone1.__add__(phone2) == 5
