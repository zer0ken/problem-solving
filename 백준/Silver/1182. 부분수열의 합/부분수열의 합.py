import sys

readline = sys.stdin.readline
n, s = map(int, readline().split())

arr = list(map(int, readline().split()))
len_arr = len(arr)

def dfs(i, acc, empty):
    count = 0
    if i == len_arr:
        return 1 if acc == s and not empty else 0    
    return dfs(i + 1, acc, empty) + dfs(i + 1, acc + arr[i], False)

sys.stdout.write(str(dfs(0, 0, True)))