import sys

s = sys.stdin.readline().rstrip()
sys.stdout.write('1' if s == s[::-1] else '0')