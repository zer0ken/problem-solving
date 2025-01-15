count = int(input())
arr = map(int, input().split())

for v in arr:
    if v == 1:
        count -= 1
        continue
    if v == 2:
        continue
    for n in range(2, int(v ** 0.5) + 1):
        if v % n == 0:
            count -= 1
            break
print(count)