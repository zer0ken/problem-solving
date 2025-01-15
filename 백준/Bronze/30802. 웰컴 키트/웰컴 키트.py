n = int(input())
sizes = input().split()
t, p = map(int, input().split())

count = 0
for size in sizes:
    if size == '0':
        continue
    size = int(size)
    count += size // t
    if size % t != 0:
        count += 1
print(count)
print(n // p, n % p)