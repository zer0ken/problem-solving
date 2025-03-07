import sys

for i in range(N := int(input()) - 1, -1, -1):
    sys.stdout.write(' ' * (N - i) + '*' * (2 * i + 1) + '\n')