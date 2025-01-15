br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

b_j_distance = max(abs(jr - br), abs(jc - bc))
d_j_distance = abs(jr - dr) + abs(jc - dc)

if b_j_distance < d_j_distance:
    print('bessie')
elif b_j_distance > d_j_distance:
    print('daisy')
else:
    print('tie')