def solution(n):
    arr = [n]
    while (last := arr[-1]) != 1:
        if last % 2 == 0:
            arr.append(last // 2)
        else:
            arr.append(3 * last + 1)
    return arr