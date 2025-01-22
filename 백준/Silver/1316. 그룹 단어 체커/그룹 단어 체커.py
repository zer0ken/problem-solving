import sys

readline = sys.stdin.readline
n = int(readline().rstrip())

count = 0
for _ in range(n):
    word = readline().rstrip()
    group = True
    used = []
    last = word[0]
    for cha in word:
        if cha in used and cha != last:
            group = False
            break
        used.append(cha)
        last = cha
    if group:
        count += 1
sys.stdout.write(str(count))            