def main():
    import sys
    from collections import deque
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    N, M = map(int, readline().split())
    board = [list(map(int, readline().split())) for _ in range(N)]
    cheese = sum(r.count(1) for r in board)
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def get_cc(r, c):
        target = board[r][c]
        cc = [(r, c)]
        visited = [[0] * M for _ in range(N)]
        visited[r][c] = 1
        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == target and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    cc.append((nr, nc))
                    queue.append((nr, nc))
        return cc 
    
    
    time = 0
    while cheese:
        time += 1
        exposed = set()
        for r, c in get_cc(0, 0):
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 0:
                    if (nr, nc) not in exposed:
                        exposed.add((nr, nc))
                    else:
                        exposed.remove((nr, nc))
                        board[nr][nc] = 0
                        cheese -= 1

    write(str(time))


if __name__ == '__main__':
    main()