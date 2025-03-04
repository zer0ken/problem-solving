def main():
    import sys
    
    readline = sys.stdin.readline
    write = sys.stdout.write
    INF = float('inf')
    
    N, M = map(int, readline().split())
    houses = []
    chickens = []
    for r in range(N):
        row = readline().split()
        for c in range(N):
            if row[c] == '1':
                houses.append((r, c))
            elif row[c] == '2':
                chickens.append((r, c))
    
    choosen = []
    
    def dfs(cur):
        if cur == len(chickens):
            if len(choosen) != M:
                return INF
            d = sum(min(abs(r1 - r2) + abs(c1 - c2) for r2, c2 in choosen) for r1, c1 in houses)
            return d
        
        if len(choosen) + len(chickens) - cur < M:
            return INF
        
        with_cur = INF
        if len(choosen) < M:
            choosen.append(chickens[cur])
            with_cur = dfs(cur + 1)
            choosen.pop()
        without_cur = dfs(cur + 1)
        return min(without_cur, with_cur)

    write(str(dfs(0)))


if __name__ == '__main__':
    main()