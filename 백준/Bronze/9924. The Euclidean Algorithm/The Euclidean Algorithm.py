import sys

def gcd(a, b):
    step = 0
    while a != b:
        step += 1
        a, b = max(a, b) - min(a, b), min(a, b)
    return step

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(f'{gcd(a, b)}\n')