def solution(string, m, c):
    s = []
    for i in range(c - 1, len(string), m):
        s.append(string[i])
    return ''.join(s)