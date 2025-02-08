def solution(arr, flag):
    ret = []
    for v, f in zip(arr, flag):
        if f:
            ret.extend([v] * (2 * v))
        else:
            ret = ret[:-v]
    return ret