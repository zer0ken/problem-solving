def main():
    import sys
    from collections import deque

    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())
    mountain = [list(map(int, readline().split())) for _ in range(N + 1)]
    visited = [[0] * M for _ in range(N)]
    
    peaks = set()
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = 1
                is_peak = 1
                same_height_group = set()
                queue = deque([(i, j)])
                while queue:
                    row, col = queue.popleft()
                    height = mountain[row][col]
                    same_height_group.add((row, col))
                    for drow in (-1, 0, 1):
                        for dcol in (-1, 0, 1):
                            nrow, ncol = row + drow, col + dcol
                            if drow == dcol == 0 or nrow < 0 or nrow >= N or ncol < 0 or ncol >= M \
                                    or mountain[nrow][ncol] < height:
                                continue
                            if mountain[nrow][ncol] > height:
                                is_peak = 0
                            elif not visited[nrow][ncol]:
                                visited[nrow][ncol] = 1
                                same_height_group.add((nrow, ncol))
                                queue.append((nrow, ncol))
                if is_peak:
                    peaks.add(frozenset(same_height_group))
    write(str(len(peaks)))


if __name__ == '__main__':
    main()