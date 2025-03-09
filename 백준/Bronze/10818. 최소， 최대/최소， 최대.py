import sys
arr = list(map(int, sys.stdin.read().split()[1:]))
sys.stdout.write(f'{min(arr)} {max(arr)}')