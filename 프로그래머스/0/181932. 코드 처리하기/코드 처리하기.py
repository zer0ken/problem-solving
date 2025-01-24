def solution(code):
    ret = []
    mode = '0'
    for i, c in enumerate(code):
        if c == '1':
            mode = '0' if mode == '1' else '1' 
            continue
        if mode == '0':
            if i % 2 == 0:
                ret.append(c)
        else:
            if i % 2 == 1:
                ret.append(c)
    return ''.join(ret) if ret else 'EMPTY'