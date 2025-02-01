import sys

arr = [1, 1, 2, 2, 2, 8]
for i, count in enumerate(map(int, sys.stdin.readline().split())):
    arr[i] -= count
sys.stdout.write(' '.join(map(str, arr)))