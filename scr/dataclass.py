class Product:
    pay_rate = 1  # атрибут устанавливает уровень цен
    all = []  # атрибутдля хранения созданных экземпляров класса

    def __new__(cls, *args, **kwargs):
        print("Создается новый экземпляр Product.")
        return super().__new__(cls)

    def __init__(self, name, price, amount):
        print("Инициализируется новый экземпляр Product.")
        self.__name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        """Возвращает имя товара, при превышении 10 символов возвращете исключение """
        if len(name) <= 10:
            self.__name = name
        else:
            print('Длина наименования товара превышает 10 символов')


    def apply_discount(self):
        """Метод возвращает общую стоимость конкретного товара в магазине"""
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        """Метод возвращает цену товара с установленной скидкой"""
        total = self.price * self.amount
        return total


item = Product('Телеdddddddфоh', 10000, 5)
item.name = ')))))))))))cdcvdf'
print(item.name)



