a, b, c, d = map(int, (input() for _ in range(4)))

total = a + b + c + d
r1 = total // 60
r2 = total % 60

print(r1)
print(r2)