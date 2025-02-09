def solution(arr):
    l = 1
    while len(arr) > l:
        l *= 2
    arr.extend([0] * (l - len(arr)))
    return arr