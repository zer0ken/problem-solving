def solution(a, b, c):
    s = set([a, b, c])
    l = len(s)
    if l == 3:
        return a + b + c
    if l == 2:
        return (a + b + c) * (a*a + b*b + c*c)
    return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)