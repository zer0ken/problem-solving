n, m, k = map(int, input().split())
if k > min(n, m):
    print('Impossible')
    exit(0)
print('Possible')
for i in range(n):
    for j in range(m):
        if i == j and k > 0:
            print('*', end='')
            k -= 1
        else:
            print('.', end='')
    print()