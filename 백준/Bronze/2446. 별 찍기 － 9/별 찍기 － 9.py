import sys

for i in list(range(N := int(input()))) + list(range(N - 2, -1, -1)):
    sys.stdout.write(' '*i + '*'*(2*N - 2*i - 1) + '\n')