for _ in range(int(input())):
    s = input()
    _c = s[0]
    print(_c, end='')
    for c in s[1:]:
        if c != _c:
            _c = c
            print(_c, end='')
    print()