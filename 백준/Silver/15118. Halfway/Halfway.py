import sys

n = int(sys.stdin.readline())

def acc(x):
    if x % 2 == 0:
        return (x + 1) * (x // 2)
    return x * (x // 2) + x

total = acc(n - 1)
half = (total + 1) // 2

l, r = 1, n - 1
while l <= r:
    mid = (l + r) // 2
    comp = total - acc(n - 1 - mid)
    if comp == half:
        l = mid
        break
    elif comp < half:
        l = mid + 1
    else:
        r = mid - 1

sys.stdout.write(str(l))