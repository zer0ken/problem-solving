import sys

sys.stdout.write(str(max(map(lambda s: int(s[::-1]), sys.stdin.readline().split()))))