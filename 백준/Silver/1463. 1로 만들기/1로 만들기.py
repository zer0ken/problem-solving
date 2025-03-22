def main():
    import sys
    
    N = int(sys.stdin.read())
    
    if N == 1:
        sys.stdout.write('0')
        exit(0)
    
    dp = set([N])
    for i in range(1, N):
        next_dp = set()
        for v in dp:
            new_v = set()
            if v % 3 == 0:
                new_v.add(v // 3)
            if v % 2 == 0:
                new_v.add(v // 2)
            new_v.add(v - 1)
            next_dp.update(new_v)
            
            if 1 in new_v:
                break
        
        dp = next_dp
        if 1 in dp:
            break
        
    
    sys.stdout.write(str(i))


if __name__ == '__main__':
    main()