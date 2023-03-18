from scr.product import Product
from scr.phone import Phone
from scr.keyboard import KeyBoard


def main():
    # Считываем данные из  csv-файла и создаем экземпляры класса, выводим длину массива
    # path = 'items.csv'
    # Product.instantiate_from_csv(path)
    # print(len(Product.all))
    # print(Product.all)

    # Добавляем к классу Товара магические методы __repr__ и __str__
    # item1 = Product("Смартфон", 10000, 20)
    # print(item1)

    # смартфон iPhone 14, цена 120_000, количетсво товара 5, симкарт 2
    # phone1 = Phone("iPhone 14", 120_000, 5, 2)
    # print(phone1)

    # print(repr(phone1))
    # phone1.number_of_sim = 0

    # phone2 = Phone("iPhone 14", 120_000, 5, 2)
    # print(phone1.__add__(phone2))

    #kb = KeyBoard('Dark Project KD87A', 9600, 5)
    #print(kb)
    #print(kb.language)
    #kb.change_lang()
    #print(kb.language)
    #kb.change_lang()
    #print(kb.language)
    #print(KeyBoard.__mro__)
    #kb.language = 'CH'

    # Файл items.csv отсутствует.
    path = '../items.csv'
    Product.instantiate_from_csv(path)

    # В файле items.csv удалена последняя колонка.
    path = 'items_err.csv'
    Product.instantiate_from_csv(path)



if __name__ == '__main__':
    main()
