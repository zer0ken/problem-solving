import sys
readline = sys.stdin.readline

n = int(readline().rstrip())

guys = []
ranks = []

for i in range(n):
    here = tuple(map(int, readline().split()))

    guys.append(here)
    ranks.append(1)

    for j in range(i):
        there = guys[j]
        if there[0] > here[0] and there[1] > here[1]:
            ranks[i] += 1
        if here[0] > there[0] and here[1] > there[1]:
            ranks[j] += 1

sys.stdout.write(' '.join(map(str, ranks)))