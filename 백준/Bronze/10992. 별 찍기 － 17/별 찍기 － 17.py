import sys

for i in range(N := int(input())):
    sys.stdout.write(' '*(N - i - 1))
    if i == 0:
        sys.stdout.write('*\n')
    elif i == N - 1:
        sys.stdout.write('*'*(2*N - 1) + '\n')
    else:
        sys.stdout.write('*' + ' '*(2*i - 1) + '*\n')