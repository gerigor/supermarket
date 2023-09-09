from supermarket import Price


def test_price_create():
    price = Price(value=1.0)
    assert type(price) == Price
    assert price.value == 1.0
