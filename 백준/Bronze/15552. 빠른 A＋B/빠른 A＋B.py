import sys
for _ in range(int(input())):
    a, b = sys.stdin.readline().rstrip().split()
    sys.stdout.write(str(int(a) + int(b)) + '\n')