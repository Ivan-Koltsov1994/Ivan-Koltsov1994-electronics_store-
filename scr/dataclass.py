class Product:
    pay_rate = 1  # атрибут устанавливает уровень цен
    all = []  # атрибутдля хранения созданных экземпляров класса

    def __new__(cls, *args, **kwargs):
        print("Создается новый экземпляр Product.")
        return super().__new__(cls)

    def __init__(self, name, price, amount):
        print("Инициализируется новый экземпляр Product.")
        self.name = name
        self.price = price
        self.amount = amount
        self.all.append(self)

    def apply_discount(self):
        """Метод возвращает общую стоимость конкретного товара в магазине"""
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        """Метод возвращает цену товара с установленной скидкой"""
        total = self.price * self.amount
        return total