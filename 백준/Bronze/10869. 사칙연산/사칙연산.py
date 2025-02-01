import sys

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(
    f'{a + b}\n'
    f'{a - b}\n'
    f'{a * b}\n'
    f'{a // b}\n'
    f'{a % b}\n'
)