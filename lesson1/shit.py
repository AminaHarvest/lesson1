def format_price (price):
    price = int(price)
    price = (f'Цена: {price} руб.' )
    return price

price_shit = format_price(56.24)
print(price_shit)