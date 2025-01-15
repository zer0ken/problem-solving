import sys
_, n, _ = input(), set(input().split()), input()
for m in input().split():
    sys.stdout.write('1\n' if m in n else '0\n')
