def count_basket(basket):
    total_amount, total_quantity = 0, 0
    tax_basket, total_basket = 0, 0
    if basket:
        for c in basket.values():
            total_amount += c['quantity'] * c['price']
            total_quantity += c['quantity']
            tax_basket = total_amount * 0.1
            total_basket = tax_basket + total_amount

    return {
        "total_quantity": total_quantity,
        "total_amount": total_amount,
        "tax_basket":tax_basket,
        "total_basket": total_basket
    }


def count_products(product):
    total_amount, total_quantity = 0, 0

    if product:
        for p in product.values():
            total_amount += p['quantity'] * p['price']
            total_quantity += p['quantity']

    return {
        "total_quantity": total_quantity,
        "total_amount": total_amount

    }
