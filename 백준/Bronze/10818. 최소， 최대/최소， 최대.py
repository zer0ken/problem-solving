import sys

read = sys.stdin.read
write = sys.stdout.write

arr = list(map(int, read().split()[1:]))
write(f'{min(arr)} {max(arr)}')