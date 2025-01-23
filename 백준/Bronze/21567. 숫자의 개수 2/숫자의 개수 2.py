import sys
from collections import Counter

readline = sys.stdin.readline
abc = int(readline().rstrip())
abc *= int(readline().rstrip())
abc *= int(readline().rstrip())
counter = Counter(str(abc))

for i in range(10):
    sys.stdout.write(f'{counter.get(str(i), 0)}\n')