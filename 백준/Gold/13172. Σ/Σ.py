def main():
    import sys
    
    M, *lines = sys.stdin.read().rstrip().split('\n')
    X = 1_000_000_007
    
    def pow(n, exp):
        if exp == 0:
            return 1
        if exp < 4:
            return (n ** exp) % X
        
        sqrt = int(exp ** 0.5)
        sqrt_pow = pow(n, sqrt)
        
        left = exp - sqrt ** 2
        left_pow = pow(n, left)
        
        return ((pow(sqrt_pow, sqrt)%X) * (left_pow%X)) % X
    
    
    total = 0
    for line in lines:
        N, S = map(int, line.split())
        total = (total + S*pow(N, X - 2)) % X
    
    sys.stdout.write(str(total))
        

if __name__ == '__main__':
    main()