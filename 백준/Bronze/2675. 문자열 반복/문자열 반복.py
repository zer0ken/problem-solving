import sys
for _ in range(int(input())):
    r, s = sys.stdin.readline().split()
    r = int(r)
    sys.stdout.write(''.join(c * r for c in s) + '\n')
