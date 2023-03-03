import csv


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
    def name(self, name: str) -> None:
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

    @classmethod
    def instantiate_from_csv(cls):
        """Метод cчитывает данные из csv-файла и создает экземпляры класса,
        инициализируя их данными из файла"""
        items = []
        path = '../items.csv'
        with open(path, 'r', encoding='windows-1251', newline='') as csvfile:
            list = csv.DictReader(csvfile)
            for row in list:
                items.append(cls(row['name'], int(row['price']), int(row['quantity'])))
        return items

    @staticmethod
    def is_integer_num(num):
        """Метод  проверяет, является ли число (например, полученное из csv-файла) целым, если нет, то возвращает в
        виде целого """
        if isinstance(num, int):
            return True
        if isinstance(num, float):
            return num.is_integer()
        return False


#Product.instantiate_from_csv()
#print(len(Product.all))
#print(Product.all)
#Product.instantiate_from_csv()  # создание объектов из данных файла
#print(len(Product.all))  # в файле 5 записей с данными по товарам
#item1 = Product.all[0]
#print(item1.name)
#print(Product.is_integer_num(5))
#print(Product.is_integer_num(5.0))
#print(Product.is_integer_num(5.5))
