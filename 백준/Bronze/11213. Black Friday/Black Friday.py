import sys
from collections import Counter
N, *arr = map(int, sys.stdin.read().split())
counter = Counter(arr)
for eyes in range(6, 0, -1):
    if arr.count(eyes) == 1:
        print(arr.index(eyes) + 1)
        exit(0)
else:
    print('none')