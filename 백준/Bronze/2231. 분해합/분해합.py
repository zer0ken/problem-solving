n = int(input())
m = 0
for x in range(max(1, n - 54), n):
    if x + sum(map(int, str(x))) == n:
        m = x 
        break
print(m)
