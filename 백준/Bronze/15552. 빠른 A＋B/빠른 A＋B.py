import sys
for _ in range(int(input())):
    a, b = sys.stdin.readline().split()
    sys.stdout.write(str(int(a) + int(b)) + '\n')