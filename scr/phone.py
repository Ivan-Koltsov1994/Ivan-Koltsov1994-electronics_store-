from  scr.product import Product


class Phone(Product):
    """Класс наследуемый от класса Product"""

    def __init__(self, name: str, price: int, quantity: int,
                 number_of_sim: int):  # переопределяем метод базового класса
        super().__init__(name, price, quantity)  # вызываем  базового класса
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f'Марка телефона: {self.name}, цена: {self.price}, в наличии: {self.amount}, количество сим-карт' \
               f': {self.__number_of_sim} '

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) :
        """При количество SIM-карт меньше нуля выдает ошибку """
        if self.number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        if self.number_of_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other) -> int:
        """Метод скадывает экземпляры класса Phone с другим по кол-ву количество товаров в наличии"""
        if isinstance(other, Phone):
            return int(self.number_of_sim) + int(other.number_of_sim)
        else:
            raise ValueError('Неправильный формат')