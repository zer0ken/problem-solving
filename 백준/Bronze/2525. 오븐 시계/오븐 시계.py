h, m = input().split()
h = int(h)
m = int(m)

m_delta = int(input())

m += m_delta
h = h + m // 60

m %= 60
h %= 24

print(h, m)