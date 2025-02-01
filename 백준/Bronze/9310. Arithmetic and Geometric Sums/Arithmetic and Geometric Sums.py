import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    a, b, c = map(int, sys.stdin.readline().split())
    
    
    if b - a == c - b:
        d = b - a
        s = N * (2*a + (N - 1)*d) // 2
    else:
        r = b // a
        s = a * (r ** N - 1) // (r - 1)
    sys.stdout.write(f'{s}\n')