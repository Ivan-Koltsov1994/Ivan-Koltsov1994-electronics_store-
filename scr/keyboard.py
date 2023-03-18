from scr.product import Product


class Mixinlog:
    """Класс-миксин реализующий дополнительный функционал по хранению и изменению раскладки клавиатуры"""

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> str:
        """Метод изменяет раскладку клавиатуры"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self.__language


class KeyBoard(Product, Mixinlog):
    """Класс наследуемый от класса Product, Mixinlog описывает свойства товара - клавиатура"""
    pass
