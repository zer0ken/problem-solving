def solution(p, c):
    from collections import Counter
    return list(Counter(p) - Counter(c))[0]