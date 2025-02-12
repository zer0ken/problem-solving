def solution(d1, d2):
    to_int = lambda d: d[0] * 10000 + d[1] * 100 + d[2]
    return int(to_int(d1) < to_int(d2))