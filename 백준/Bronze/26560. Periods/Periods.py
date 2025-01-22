import sys

readline = sys.stdin.readline
t = int(readline().rstrip())
for _ in range(t):
    sentence = readline().rstrip()
    if sentence[-1] != '.':
        sentence += '.'
    sys.stdout.write(sentence + '\n')