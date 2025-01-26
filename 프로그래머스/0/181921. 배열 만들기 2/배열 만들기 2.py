import math

def solution(l, r):
    results = []
    for number in range(5 * math.ceil(l / 5), r + 1, 5):
        n_str = str(number)
        valid = True
        for cha in n_str:
            if cha not in '50':
                valid = False
                break
        if valid:
            results.append(number)
    return results if results else [-1]