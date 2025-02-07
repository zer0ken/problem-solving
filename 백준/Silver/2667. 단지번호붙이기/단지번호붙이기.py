def main():
    import sys
    from collections import deque
    import heapq
    
    input = sys.stdin.readline
    N = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(N)]
    visited= [[0] * N for _ in range(N)]
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    groups = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] or not board[i][j]:
                continue
            visited[i][j] = 1
            count = 0
            queue = deque([(i, j)])
            while queue:
                row, col = queue.popleft()
                count += 1
                for drow, dcol in deltas:
                    nrow = row + drow
                    ncol = col + dcol
                    if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N:
                        continue
                    if visited[nrow][ncol] or not board[nrow][ncol]:
                        continue
                    visited[nrow][ncol] = 1
                    queue.append((nrow, ncol))
            heapq.heappush(groups, count)
    
    sys.stdout.write(f'{len(groups)}\n')
    while groups:
        sys.stdout.write(f'{heapq.heappop(groups)}\n')


if __name__ == '__main__':
    main()