from supermarket import (
    WeightProduct, 
    ItemProduct,
    Price
)


def test_weighted_product():
    product = WeightProduct(name='apple', price=Price(2.0))
    assert type(product) == WeightProduct


def test_item_product():
    product = ItemProduct(name='snikers', price=Price(2.0))
    assert type(product) == ItemProduct
