x, y = map(int, input().split())
a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
prefix = c + q
postfix = r
print(a, b, c, d, q, r)
print(prefix, postfix)