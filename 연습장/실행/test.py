def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def main():
    import sys
    input = sys.stdin.readline

    for _ in range(int(input())):
        M, N, x, y = map(int, input().split())
        doom = M * N // gcd(M, N)
        target_diff = y - x

        m = 1
        n = 1
        k = 1
        while k <= doom:
            diff = n - m
            
            if diff == target_diff:
                k += min(x, y) - 1
                sys.stdout.write(f'{k}\n')
                break
            
            m_left = M - m + 1
            n_left = N - n + 1
            if m_left == n_left:
                k += m_left
                m = 1
                n = 1
            elif m_left < n_left:
                k += m_left
                m = 1
                n += m_left
            else:
                k += n_left
                m += n_left
                n = 1
        else:
            sys.stdout.write('-1\n')


if __name__ == '__main__':
    main()