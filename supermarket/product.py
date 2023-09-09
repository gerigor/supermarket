from supermarket.price import Price

class Product:
    """
        Abstract class
        This method must NOT ever-ever be initiated directly
    """
    def __init__(self, name: str, price: Price):
        self.name = name
        self.price = price
    
    def can_be_fraction_quantity(self):
        raise NotImplementedError

class ItemProduct(Product):
    def __init__(self, name: str, price: Price):
        super().__init__(name, price)

    def can_be_fraction_quantity(self):
        return False


class WeightProduct(Product):
    def __init__(self, name: str, price: Price):
        super().__init__(name, price)

    def can_be_fraction_quantity(self):
        return True
