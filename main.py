from scr.dataclass import Product


# Считываем данные из  csv-файла и создаем экземпляры класса, выводим длину массива
path = 'items.csv'
Product.instantiate_from_csv(path)
print(len(Product.all))
print(Product.all)

#Добавляем к классу Товара магические методы __repr__ и __str__
item1 = Product("Смартфон", 10000, 20)
print(item1)