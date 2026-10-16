def compute_total(items, discount):
    subtotal = sum(i['price'] * i['qty'] for i in items)
    # discount is a percentage
    return round(subtotal * (1 - discount / 100), 2)
