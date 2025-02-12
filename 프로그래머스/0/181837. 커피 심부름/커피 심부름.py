def solution(orders):
    price = 0
    for o in orders:
        if 'latte' in o:
            price += 5000
        else:
            price += 4500
    return price