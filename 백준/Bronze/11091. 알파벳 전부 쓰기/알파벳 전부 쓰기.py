for _ in range(int(input())):
    s = set(input().lower())
    missings = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in s]
    if not missings:
        print('pangram')
    else:
        print('missing', ''.join(missings))