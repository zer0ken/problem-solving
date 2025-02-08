def solution(arr):
    ret = []
    for n in arr:
        ret.extend([n] * n)
    return ret