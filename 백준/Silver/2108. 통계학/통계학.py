import sys
import decimal
from collections import Counter

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
sum_ = sum(arr)
mean = int(round(decimal.Decimal(str(sum_)) / N, 0))
sarr = sorted(arr)
median = sarr[N // 2]
common = arr[0]

if N > 1:
    counter = Counter(sarr[::-1])
    commons = counter.most_common()
    max_count = commons[0][1]
    
    same_commons = []
    for value, count in commons:
        if max_count > count:
            break
        same_commons.append(value)
    same_commons = sorted(same_commons)
    common = same_commons[1 if len(same_commons) > 1 else 0]

range_ = sarr[-1] - sarr[0]

sys.stdout.write(f'{mean}\n{median}\n{common}\n{range_}')