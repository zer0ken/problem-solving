import sys

readline = sys.stdin.readline

text = list(readline().rstrip())
bomb = list(readline().rstrip())
trigger = bomb[-1]
len_bomb = len(bomb)

stack = []

for cha in text:
    stack.append(cha)
    if cha != trigger or len(stack) < len_bomb:
        continue
    bomb_detected = True
    for i in range(-1, -len_bomb - 1, -1):
        if stack[i] != bomb[i]:
            bomb_detected = False
    if bomb_detected:
        for _ in range(len_bomb):
            stack.pop()

sys.stdout.write(''.join(stack) if stack else 'FRULA')