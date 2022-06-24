class Product:
    def __init__(self, product_name: str, product_color: str, product_price: int):
        self.product_name = product_name
        self.product_color = product_color
        self.product_price = product_price

    def __str__(self):

        return f'{self.product_name}, {self.product_color}, {self.product_price}'
class NumberError:
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

pr_1 = Product('Apple', 'green', -1)

try:
    if pr_1.product_price <= 0:
        raise NumberError(pr_1.product_price, 'Number is below 0')
except NumberError as err:
    print(err)

try:
    if not isinstance(pr_1.product_price, int):
        raise TypeError('Please input only numbers')
except:
    print(pr_1)



