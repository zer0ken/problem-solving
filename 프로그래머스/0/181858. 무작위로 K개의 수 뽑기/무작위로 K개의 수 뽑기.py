def solution(arr, k):
    ret = []
    for v in arr:
        if len(ret) == k:
            break
        if v not in ret:
            ret.append(v)
    return ret + [-1] * (k - len(ret))