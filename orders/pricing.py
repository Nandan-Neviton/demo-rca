def compute_total(items, discount=0):
    subtotal = sum(i['price'] * i['qty'] for i in items)
    return round(subtotal * (1 - discount / 100), 2)
