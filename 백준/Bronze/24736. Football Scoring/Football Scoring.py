import sys

readline = sys.stdin.readline
visiting_box = map(int, readline().split())
home_box = map(int, readline().split())

def score(t, f, s, p, c):
    return t*6 + f*3 + 2*s + p + c*2

sys.stdout.write(f'{score(*visiting_box)} {score(*home_box)}')