def main():
    import sys

    dp = {}
    
    def w(a, b, c):
        nonlocal dp
        if (result := dp.get((a, b, c))) is not None:
            return result

        if a <= 0 or b <= 0 or c <= 0:
            result = 1
        elif a > 20 or b > 20 or c > 20:
            result = w(20, 20, 20)
        elif a < b < c:
            result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        dp[(a, b, c)] = result
        return result
    
    a, b, c = 0, 0, 0
    for line in sys.stdin.read().rstrip().splitlines()[:-1]:
        a, b, c = map(int, line.split())
        sys.stdout.write(f'w({a}, {b}, {c}) = {w(a, b, c)}\n')
    

if __name__ == '__main__':
    main()