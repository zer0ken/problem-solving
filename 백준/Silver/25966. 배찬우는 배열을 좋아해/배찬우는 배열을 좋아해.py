def main():
    import sys
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M, q = map(int, readline().split())
    matrix = [list(map(int, readline().split())) for _ in range(N)]
    for _ in range(q):
        op, i, j, *k = map(int, input().split())
        if op == 0:
            matrix[i][j] = k[0]
        else:
            matrix[i], matrix[j] = matrix[j], matrix[i]
    for row in matrix:
        write(f'{" ".join(map(str, row))}\n')


if __name__ == '__main__':
    main()