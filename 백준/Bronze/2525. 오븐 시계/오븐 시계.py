h, m = input().split()
h = int(h)
m = int(m)
m_delta = int(input())

m += m_delta
if m > 59:
    h += m // 60
    m %= 60
if h > 23:
    h %= 24
    
print(h, m)