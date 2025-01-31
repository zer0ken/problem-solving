import sys

a, b = map(lambda s: int(s[::-1]), sys.stdin.readline().split())
sys.stdout.write(str(max(a, b)))