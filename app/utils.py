def count_basket(basket):
    total_amount, total_quantity = 0, 0

    if basket:
        for c in basket.values():
            total_amount += c['quantity'] * c['price']
            total_quantity += c['quantity']

    return {
        "total_quantity": total_quantity,
        "total_amount": total_amount

    }
