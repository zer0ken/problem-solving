import sys

x, y, w, h = map(int, sys.stdin.readline().split())
sys.stdout.write(str(min(x, w - x, y, h - y)))