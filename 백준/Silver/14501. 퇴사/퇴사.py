def main():
    import sys
    
    N, *lines = sys.stdin.read().rstrip().splitlines()
    N = int(N)
    counsels = [[] for _ in range(N + 1)]
    for i, line in enumerate(lines):
        T, P = map(int, line.split())
        if i + T <= N:
            counsels[i+T].append([i, P])
    
    dp = [None] * (N + 1)
    
    def evaluate(end_day):
        nonlocal dp
        
        if end_day < 0:
            return 0
        
        if dp[end_day] is not None:
            return dp[end_day]
        
        total_paid = evaluate(end_day - 1)
        for start_day, paid in counsels[end_day]:
            total_paid = max(total_paid, paid + evaluate(start_day))
        
        dp[end_day] = total_paid
        return dp[end_day]
    
    print(evaluate(N))


if __name__ == '__main__':
    main()