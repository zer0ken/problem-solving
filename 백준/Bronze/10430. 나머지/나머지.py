import sys
a, b, c = map(int, sys.stdin.readline().split())
sys.stdout.write(
    f'{(a + b) % c}\n'
    f'{((a % c) + (b % c)) % c}\n'
    f'{(a * b) % c}\n'
    f'{((a % c) * (b % c)) % c}\n'
)