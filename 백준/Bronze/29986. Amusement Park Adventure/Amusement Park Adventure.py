_, h = input().split()
h = int(h)
limits = input().split()

count = 0
for limit in limits:
    if int(limit) <= h:
        count += 1

print(count)