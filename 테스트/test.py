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
            new_values = set()
            if v % 3 == 0:
                new_values.add(v // 3)
            if v % 2 == 0:
                new_values.add(v // 2)
            new_values.add(v - 1)
            
            if 1 in new_values:
                break
            next_dp.update(new_values)
        else:
            dp = next_dp
            continue
        break
    
    sys.stdout.write(str(i))


if __name__ == '__main__':
    main()