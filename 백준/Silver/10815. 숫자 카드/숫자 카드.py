import sys
from bisect import bisect_left

input = sys.stdin.readline

_, cards, _ = input(), sorted(map(int, input().split())), input()
len_cards = len(cards)

for card in map(int, input().split()):
    idx = bisect_left(cards, card)
    if idx < len_cards and cards[idx] == card:
        sys.stdout.write('1 ')
    else:
        sys.stdout.write('0 ')