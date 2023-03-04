from scr.dataclass import Product


# Считываем данные из  csv-файла и создаем экземпляры класса, выводим длину массива
Product.instantiate_from_csv()
print(len(Product.all))
print(Product.all)

