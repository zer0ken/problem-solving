def main():
    import sys
    
    N, *lines = sys.stdin.read().rstrip().splitlines()
    N = int(N)
    counsels = [list(map(int, line.split())) for line in lines]

    income = 0
    max_income = 0
    
    def dfs(i):
        nonlocal income, max_income
        
        if i > N:
            return
        if i == N:
            max_income = max(max_income, income)
            return
        
        dfs(i + 1)
        
        income += counsels[i][1]
        dfs(i + counsels[i][0])
        income -= counsels[i][1]

    dfs(0)
    print(max_income)


if __name__ == '__main__':
    main()