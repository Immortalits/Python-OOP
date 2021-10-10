import uuid


class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name ='{self.product_name}', price = '{self.price}')"

    @staticmethod
    def get_id():
        code = str(uuid.uuid4()).split('-')
        return code[len(code) - 1]


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        newProd = Product(product_name, price)
        insert = True
        for product in self.products:
            if product.product_name == product_name:
                insert = False
        if insert == True:
            self.products.append(newProd)

    def remove_product(self, product_name):
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(
                f"{product.get_id()}, {product.product_name}, {product.price}")

    def sort_by_price(self, ascending=True):
        self.products.sort(key=lambda product: product.price,
                           reverse=not ascending)
        return self.products


# print(str(uuid.uuid4()).split('-'))

warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
for product in warehouse.sort_by_price():
    print(product)