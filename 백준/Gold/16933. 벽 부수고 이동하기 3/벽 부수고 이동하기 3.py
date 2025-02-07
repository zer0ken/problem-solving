def main():
    import sys
    from collections import deque

    N, M, K = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
    visited = [[[0] * M for _ in range(N)] for _ in range(K + 1)]
    visited[0][0][0] = 1

    deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
    queue = deque([(0, 0, 0, 1)])
    while queue:
        row, col, broke, dist  = queue.popleft()
        if row == N - 1 and col == M - 1:
            sys.stdout.write(str(dist))
            break
        
        for delta_row, delta_col in deltas:
            nrow = row + delta_row
            ncol = col + delta_col
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= M:
                continue
            
            nbroke = broke + board[nrow][ncol]
            if nbroke > K:
                continue
            
            if visited[nbroke][nrow][ncol]:
                continue
            
            if not board[nrow][ncol] or dist % 2:
                visited[nbroke][nrow][ncol] = 1
                queue.append((nrow, ncol, nbroke, dist + 1))
            else:
                queue.append((row, col, broke, dist + 1))
    else:
        sys.stdout.write('-1')


if __name__ == '__main__':
    main()