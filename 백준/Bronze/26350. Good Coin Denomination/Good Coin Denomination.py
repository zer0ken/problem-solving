import sys

n = int(input())
for _ in range(n):
    d = sorted(map(int, sys.stdin.readline().split()[1:]))
    is_good = True

    sys.stdout.write('Denominations: ' + str(d[0]))
    for i in range(1, len(d)):
        sys.stdout.write(' ' + str(d[i]))
        if is_good and d[i] < d[i-1] * 2:
            is_good = False
    sys.stdout.write(('\nGood' if is_good else '\nBad') + ' coin denominations!\n\n')
        