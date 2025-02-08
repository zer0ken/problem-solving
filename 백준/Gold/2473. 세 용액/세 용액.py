import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.read().split())))

min_set = []
min_value = float('inf')

for i in range(N - 2):
    l = i + 1
    r = N - 1
    
    while l < r:
        value = arr[i] + arr[l] + arr[r]
        
        if min_value > abs(value):
            min_value = abs(value)
            min_set = [arr[i], arr[l], arr[r]]
        if value < 0:
            l += 1
        elif value > 0:
            r -= 1
        else:
            print(*min_set)
            exit(0)

print(*min_set)