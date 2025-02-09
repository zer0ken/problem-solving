def main():
    import sys
    from functools import cache

    readline = sys.stdin.readline

    N, M = map(int, readline().split())
    board = [list(map(int, readline().rstrip())) for _ in range(N)]
    
    @cache
    def is_square(num):
        return num in (0, 1) or int(num ** 0.5) ** 2 == num
    
    def to_int(arr):
        num = arr[0]
        for i in range(1, len(arr)):
            num = num * 10 + arr[i]
        return num
    
    
    max_square = -1
    for row in range(N):
        for col in range(M):
            for drow in range(-N + 1, N):
                for dcol in range(-M + 1, M):
                    digits = []
                    nrow = row
                    ncol = col
                    while 0 <= nrow < N and 0 <= ncol < M:
                        digits.append(board[nrow][ncol])
                        cur = to_int(digits)
                        if cur > max_square and is_square(cur):
                            max_square = cur
                        if drow == dcol == 0:
                            break
                        nrow += drow
                        ncol += dcol
    sys.stdout.write(str(max_square))


if __name__ == '__main__':
    main()