import sys

n, values = int(input()), list(sorted(map(int, sys.stdin.readline().split()), key=abs))
a, b = values.pop(0), values[0]
m = abs(a + b)
for a_, b_ in zip(values, values[1:]):
    m_ = abs(a_ + b_)
    if m_ < m:
        m, a, b = m_, a_, b_
    if m <= 1:
        break
sys.stdout.write(f'{min(a, b)} {max(a, b)}')
