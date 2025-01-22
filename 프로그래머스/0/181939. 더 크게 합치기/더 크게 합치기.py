def solution(a, b):
    a = str(a)
    b = str(b)
    return max(int(a + b), int(b + a))