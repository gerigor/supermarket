from supermarket import Product

class Order:
    def __init__(self) -> None:
        # [
        #     (WeightProduct(name='Apples', price=Price(2.0)), 1.5, ),
        #     (ItemProduct(name='Bananas', price=Price(2.0)), 2, ),
        # ]
        self.items = []

    def add_product(self, product: Product, quantity: float):
        is_fraction = int(quantity) != quantity
        is_only_int_quantity = not product.can_be_fraction_quantity()
        if is_only_int_quantity and is_fraction:
            raise ValueError("Quantity can't be fractionable.")

        self.items.append({
            "product": product, 
            "quantity": quantity,
        })

    def count_products(self) -> int:
        return len(self.items)

    def calculate_total_amount(self) -> float:
        """
            How much money to pay for the order:
            Sum(Product price * quantity)
        """
        return sum([
            item.get("product").price.value * item.get("quantity") 
            for item in self.items
        ])
