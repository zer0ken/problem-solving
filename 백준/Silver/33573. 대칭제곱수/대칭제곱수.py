import sys
import math

T, *arr = list(map(int, sys.stdin.read().rstrip().split()))
for v in arr:
    if int(math.sqrt(v)) ** 2 != v:
        sys.stdout.write('NO\n')
        continue
    
    v = int(str(v)[::-1])
    if int(math.sqrt(v)) ** 2 != v:
        sys.stdout.write('NO\n')
        continue
    
    sys.stdout.write('YES\n')