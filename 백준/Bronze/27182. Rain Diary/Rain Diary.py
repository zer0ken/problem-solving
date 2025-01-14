n, m = input().split()
n = int(n)
m = int(m)
last_sunday = m + 7

now = m + 14

if m + 14 == n:
    print(last_sunday)
else:
    d = m + 14 - n
    if last_sunday > d:
        print(last_sunday - d)
    else:
        print(last_sunday)
