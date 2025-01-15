ids = { v: v for v in range(1, 31) }

for _ in range(28):
    del ids[int(input())]

for v in ids.keys():
    print(v)