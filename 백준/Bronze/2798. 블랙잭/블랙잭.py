def main():
    import sys
    
    N, M, *arr = map(int, sys.stdin.read().split())
    arr.sort()
    
    best_sum = -float('inf')
    for i in range(N - 2):
        if 3 * arr[i] > M:
            break
        for j in range(i + 1, N - 1):
            if arr[i] + 2 * arr[j] > M:
                break
            for k in range(j + 1, N):
                sum_of_three = arr[i] + arr[j] + arr[k]
                if sum_of_three > M:
                    break
                if best_sum < sum_of_three:
                    best_sum = sum_of_three

    sys.stdout.write(str(best_sum))


if __name__ == '__main__':
    main()