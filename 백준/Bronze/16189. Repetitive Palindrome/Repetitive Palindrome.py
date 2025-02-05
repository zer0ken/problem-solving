import sys

raw = sys.stdin.readline().rstrip()
sys.stdout.write('YES' if raw == raw[::-1] else 'NO')