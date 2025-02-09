import sys
N = int(sys.stdin.readline())
factorial = 1
while N > 1:
    factorial *= N
    factorial %= 1_000_000_007
    N -= 1
sys.stdout.write(str(factorial))