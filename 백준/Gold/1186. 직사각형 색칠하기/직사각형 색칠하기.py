def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    INF = 10000
    
    N, K = map(int, readline().split())
    
    rectangles = []
    X = set()
    Y = set()
    x_offset = INF
    y_offset = INF
    for i in range(1, N + 1):
        x1, y1, x2, y2 = map(int, readline().split())
        rectangles.append((x1, y1, x2, y2))
        x_offset = x_offset if x_offset < x1 else x1
        y_offset = y_offset if y_offset < y1 else y1
        X.add(x1)
        X.add(x2)
        Y.add(y1)
        Y.add(y2)

    X = sorted(X)
    Y = sorted(Y)
    X_inv = {x: i for i, x in enumerate(X)}
    Y_inv = {y: i for i, y in enumerate(Y)}
    
    board = [[0] * (len(Y) - 1) for _ in range(len(X) - 1)]
    used = [[False] * (len(Y) - 1) for _ in range(len(X) - 1)]
    
    for i in range(len(X) - 1):
        dx = X[i + 1] - X[i]
        for j in range(len(Y) - 1):
            dy = Y[j + 1] - Y[j]
            board[i][j] = dx * dy
    area = [0] * (N)
    for k in range(N - 1, -1, -1):
        x1, y1, x2, y2 = rectangles[k]
        area[k] = 0
        for i in range(X_inv[x1], X_inv[x2]):
            for j in range(Y_inv[y1], Y_inv[y2]):
                if not used[i][j]:
                    used[i][j] = True
                    area[k] += board[i][j]
    write(' '.join(map(lambda x: str(x[0] + 1), sorted(sorted(enumerate(area), key=lambda x:-x[1])[:K], key=lambda x: x[0]))))


if __name__ == '__main__':
    main()