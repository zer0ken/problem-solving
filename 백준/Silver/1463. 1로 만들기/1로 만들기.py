def main():
    import sys
    
    N = int(sys.stdin.read())
    
    if N == 1:
        sys.stdout.write('0')
        exit(0)
    
    dp = {1: 0, 2: 1, 3: 1}
    
    def solve(x):
        if x in dp:
            return dp[x]
        result = 1 + min(solve(x//3) + x%3, solve(x//2) + x%2)
        dp[x] = result
        return result
    
    sys.stdout.write(str(solve(N)))


if __name__ == '__main__':
    main()