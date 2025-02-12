import sys
for num in map(int, sys.stdin.read().rstrip().split('\n')[:-1]):
    print('TENTE NOVAMENTE' if num % 42 else 'PREMIADO')