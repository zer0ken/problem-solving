n, m = map(int, input().split())
cards = list(sorted(filter(lambda x: x < m - 2, map(int, input().split())), reverse=True))

m_ = 0

for i0 in range(n):
    v0 = cards[i0]
    for i1 in range(n):
        if i0 == i1:
            continue
        
        sum_of_two = v0 + cards[i1]
        
        if sum_of_two >= m:
            continue
            
        for i2 in range(n):
            if i2 == i0 or i2 == i1:
                continue
            
            sum_of_three = sum_of_two + cards[i2]
            
            if m >= sum_of_three > m_:
                m_ = sum_of_three

print(m_)