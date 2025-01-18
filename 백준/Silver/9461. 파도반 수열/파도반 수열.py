import sys

arr = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 7, 10: 9}

def padovan(n):
    if n in arr:
        return arr[n]
    v = padovan(n - 1) + padovan(n - 5)
    arr[n] = v
    return v

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(padovan(n)) + '\n')
    