def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(N)]
    cheese = sum(r.count(1) for r in board)
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    time = 0
    while cheese:
        time += 1
        
        visited = [[0] * M for _ in range(N)]
        visited[0][0] = 1
        queue = deque([(0, 0)])
        exposed = set()
        while queue:
            r, c = queue.popleft()
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    if board[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
                    elif (nr, nc) not in exposed:
                        exposed.add((nr, nc))
                    else:
                        visited[nr][nc] = 1
                        exposed.remove((nr, nc))
                        board[nr][nc] = 0
                        cheese -= 1

    write(str(time))


if __name__ == '__main__':
    main()