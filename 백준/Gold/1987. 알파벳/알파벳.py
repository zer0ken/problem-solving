def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    R, C = map(int, readline().split())
    
    board = [readline().rstrip() for _ in range(R)]
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [0] * 26
    
    def dfs(r, c):
        nonlocal board, deltas, visited, R, C
        
        cur = ord(board[r][c]) - ord('A')
        if visited[cur] or all(visited):
            return 0
        
        visited[cur] = 1

        ret = 0
        for dr, dc in deltas:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                ret = max(ret, dfs(nr, nc))

        visited[cur] = 0
        return 1 + ret

    write(str(dfs(0, 0)))


if __name__ == '__main__':
    main()