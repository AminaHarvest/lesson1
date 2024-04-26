def format_price (price):
    price = int(price)
    price_with_string = (f'Цена: {price} руб. ')
    return (price_with_string)
    
price_shit = format_price(17247.24)
print(price_shit)