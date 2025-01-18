n, r, c = map(int, input().split())

count = 0
r_offset, c_offset = 0, 0
while n > 0:
    half = 2 ** (n-1)
    rel_r = r - r_offset
    rel_c = c - c_offset
    if rel_r < half:
        if rel_c >= half:
            count += half ** 2
            c_offset += half
    elif rel_c < half:
        count += half ** 2 * 2
        r_offset += half
    else:
        count += half ** 2 * 3
        r_offset += half
        c_offset += half
    n -= 1

print(count)