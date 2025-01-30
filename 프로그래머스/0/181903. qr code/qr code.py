def solution(q, r, code):
    s = []
    for i in range(len(code)):
        if i % q == r:
            s.append(code[i])
    return ''.join(s)