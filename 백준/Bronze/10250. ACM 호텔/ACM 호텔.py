import sys

readline = sys.stdin.readline
write = sys.stdout.write

for _ in range(int(input())):
    h, _, n = map(int, readline().split())
    write(f'{(n-1)%h + 1}{(n-1)//h + 1 :02d}\n')