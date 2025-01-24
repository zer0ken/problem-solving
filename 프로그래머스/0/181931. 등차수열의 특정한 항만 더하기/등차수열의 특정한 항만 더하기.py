def solution(a, d, included):
    ret = 0
    for i, flag in enumerate(included):
        if flag:
            ret += a
        a += d
    return ret