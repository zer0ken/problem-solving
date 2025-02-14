def main():
    import sys
    from functools import cache
    
    sys.setrecursionlimit(1000000)
    
    N = int(input())
    stack = []

    @cache
    def dfs(idx, last):
        if idx == N:
            return 1
        cases = 0
        for color in range(3):
            if last != -1 and last == color:
                continue
            stack.append(color)
            cases += dfs(idx + 1, color)
            stack.pop()
        return cases
    
    for i in range(N - 1, -1, -5):
        for c in range(3):
            dfs(i, c)
            
    print(dfs(0, -1) % 100_000_007)


if __name__ == '__main__':
    main()