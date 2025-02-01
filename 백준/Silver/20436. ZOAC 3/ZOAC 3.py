import sys
from collections import deque

l, r = sys.stdin.readline().split()
string = sys.stdin.readline().rstrip()

left_pos = {
    'q': (0, 0),
    'w': (0, 1),
    'e': (0, 2),
    'r': (0, 3),
    't': (0, 4),
    'a': (1, 0),
    's': (1, 1),
    'd': (1, 2),
    'f': (1, 3),
    'g': (1, 4),
    'z': (2, 0),
    'x': (2, 1),
    'c': (2, 2),
    'v': (2, 3)
}

right_pos = {
    'y': (0, 5),
    'u': (0, 6),
    'i': (0, 7),
    'o': (0, 8),
    'p': (0, 9),
    'h': (1, 5),
    'j': (1, 6),
    'k': (1, 7),
    'l': (1, 8),
    'b': (2, 4),
    'n': (2, 5),
    'm': (2, 6)
}

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

acc = 0
for c in string:
    if c in right_pos:
        acc += dist(right_pos[r], right_pos[c]) + 1
        r = c
    else:
        acc += dist(left_pos[l], left_pos[c]) + 1
        l = c

sys.stdout.write(str(acc))