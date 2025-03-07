import sys

for i in range(N := int(input())):
    sys.stdout.write(' '*(N - i - 1))
    for j in range(2*i + 1):
        sys.stdout.write(' ' if j % 2 else '*')
    sys.stdout.write('\n')