from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, ' f' {self.weight}, ' f' {self.category}'
class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return pprint()

    def add(self, *products):
        file = open(self.__file_name, 'a')
        if Product.name in self.__file_name:
            file.write(Product.name)
        else: print(f'Продукт {Product.name} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())




