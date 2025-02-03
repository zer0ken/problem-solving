def solution(arr):
    if len(arr) >= 11:
        return sum(arr)
    mul = 1
    for n in arr:
        mul *= n
    return mul