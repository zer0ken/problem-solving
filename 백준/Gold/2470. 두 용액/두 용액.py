import sys
import random
input = sys.stdin.readline

def boj_2470():
    n, values = int(input()), list(sorted(map(int, input().split()), key=abs))
    a, b = values.pop(0), values[0]
    m = abs(a + b)
    for a_, b_ in zip(values, values[1:]):
        m_ = abs(a_ + b_)
        if m_ < m:
            m, a, b = m_, a_, b_
    print(f'{min(a, b)} {max(a, b)}')


boj_2470()