import sys

readline = sys.stdin.readline
write = sys.stdout.write

for _ in range(int(input())):
    h, _, n = map(int, readline().split())
    write(str(((n-1)%h + 1)*100 + (n-1)//h + 1) + '\n')
