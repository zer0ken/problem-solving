import sys
arr = list(map(int, sys.stdin.read().split()[1:]))
print(min(arr), max(arr))