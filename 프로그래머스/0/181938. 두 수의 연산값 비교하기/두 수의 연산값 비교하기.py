def solution(a, b):
    sa = str(a)
    sb = str(b)
    ab = int(sa + sb)
    return max(ab, 2 * a * b)