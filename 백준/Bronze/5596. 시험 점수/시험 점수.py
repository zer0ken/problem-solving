import sys

readline = sys.stdin.readline
mingook = sum(map(int, readline().split()))
mansae = sum(map(int, readline().split()))
sys.stdout.write(f'{mingook if mingook > mansae else mansae}')