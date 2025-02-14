def main():
    import sys
    from functools import cache
    
    sys.setrecursionlimit(1000000)
    
    N = int(input())
    
    @cache
    def dfs(cur):
        if cur == N:
            return 1
        if cur > N:
            return 0
        
        return (dfs(cur + 1) + dfs(cur + 3)) % 1_000_000_007
    
    for i in range(N, -1, -5):
        dfs(i)
    print(dfs(0) % 1_000_000_007)


if __name__ == '__main__':
    main()