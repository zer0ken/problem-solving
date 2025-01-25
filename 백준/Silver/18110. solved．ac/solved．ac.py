import sys
import decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
D = decimal.Decimal
readline = sys.stdin.readline

n = D(readline().rstrip())
if n == 0:
    sys.stdout.write('0')
else:
    arr = sorted(D(readline().rstrip()) for _ in range(int(n)))
    cut = int(round(D(str(n)) * D('0.15'), 0))
    if cut > 0:
        arr = arr[cut:-cut]
        n -= 2 *  cut
    sys.stdout.write(str(round(sum(arr) / n, 0)))