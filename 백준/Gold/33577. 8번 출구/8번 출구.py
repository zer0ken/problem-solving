def main():
    import sys
    import math
    
    N, *abnormalities = map(int, sys.stdin.read().split())
    acc_sum = [0]
    for v in abnormalities:
        acc_sum.append(acc_sum[-1] + v)
    
    immunity_gains = [abnormalities[i] - acc_sum[i] for i in range(N)]    
    best_gains = [immunity_gains[0]]
    for i in range(1, N):
        best_gains.append(immunity_gains[i] if immunity_gains[i] > best_gains[-1] else best_gains[-1])
    
    immunity = 0
    loops = 0
    for i in range(N):
        if immunity < acc_sum[i + 1]:
            new_loops = math.ceil((acc_sum[i + 1] - immunity) / best_gains[i])
            immunity += best_gains[i] * new_loops
            loops += new_loops
    
    sys.stdout.write(str(loops))


if __name__ == '__main__':
    main()