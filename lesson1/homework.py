def format_price (price):
    price = int(price)
    price = "Цена: {price} руб."
    return format_price
    
price_shit = format_price(56.24)
print(price_shit)

def discounted(price, discount):
    price = abs(price)
    discount = abs(discount)
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)