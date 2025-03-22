def main():
    import sys
    
    lines = iter(sys.stdin.read().rstrip().splitlines())
    
    N, M, Q = map(int, next(lines).split())
    
    board = [0] * (N + 1)
    
    for _ in range(M):
        W, D = map(int, next(lines).split())
        board[W] = D
    
    acc_sum = [0]
    for v in board:
        acc_sum.append(acc_sum[-1] + v)
        
    l, r = 0, N + 1
    results = []
    for line in lines:
        P = int(line)
        if l <= P < r:
            left_sum = acc_sum[P] - acc_sum[l]
            right_sum = acc_sum[r] - acc_sum[P+1]
            
            if left_sum == right_sum:
                is_left_better = P <= N - P + 1
            else:
                is_left_better = left_sum < right_sum
            
            if is_left_better:
                results.append(left_sum)
                l = P + 1
            else:
                results.append(right_sum)
                r = P
        else:
            results.append(0)
    
    sys.stdout.write('\n'.join(map(str, results)))
    

if __name__ == '__main__':
    main()