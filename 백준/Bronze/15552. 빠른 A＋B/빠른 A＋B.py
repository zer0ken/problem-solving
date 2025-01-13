import sys
for _ in range(int(input())):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    b = int(b)
    sys.stdout.write(str(a + b) + '\n')