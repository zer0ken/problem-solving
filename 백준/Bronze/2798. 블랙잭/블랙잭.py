n, m = map(int, input().split())
cards = tuple(sorted(filter(lambda x: x < m - 2, map(int, input().split()))))

m_ = 0

for i0, v0 in list(enumerate(cards))[::-1][:-2]:
    for i1, v1 in enumerate(cards):
        if i0 == i1:
            continue
        
        sum_of_two = v0 + v1
        
        if sum_of_two >= m:
            continue
            
        for i2, v2 in enumerate(cards):
            if i2 == i0 or i2 == i1:
                continue
            
            sum_of_three = sum_of_two + v2
            
            if m >= sum_of_three > m_:
                m_ = sum_of_three

print(m_)