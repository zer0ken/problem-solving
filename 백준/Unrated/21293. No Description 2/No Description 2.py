import sys

arr = list(map(int, sys.stdin.read().split()))
sys.stdout.write(f'{arr[-1] - arr[-2]}\n{arr[-1] * arr[-2]}\n{arr[-1] + arr[-2] + 1}')