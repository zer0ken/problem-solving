import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

max_card = max(cards)
win = [None] * (max_card + 1)
lose = [None] * (max_card + 1)

for card in cards:
    win[card] = 0
    lose[card] = 0

for n in range(1, max_card):
    if win[n] is None:
        continue
    for kn in range(2 * n, max_card + 1, n):
        if lose[kn] is None:
            continue
        win[n] += 1
        lose[kn] += 1

for card in cards:
    sys.stdout.write(f'{win[card] - lose[card]} ')