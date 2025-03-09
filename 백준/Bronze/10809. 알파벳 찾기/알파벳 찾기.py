string = input()

indices = [-1] * 26
for i, c in enumerate(string):
    c = ord(c) - ord('a')
    if indices[c] != -1:
        continue
    indices[c] = i

print(*indices)