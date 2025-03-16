lower_holes = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
upper_holes = [1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
logo = 1

holes = 0
ord_a = ord('a')
ord_z = ord('z')
ord_A = ord('A')
ord_Z = ord('Z')
for c in input():
    if c == '@':
        holes += 1
    ord_c = ord(c)
    if ord_A <= ord_c <= ord_Z:
        holes += upper_holes[ord_c - ord_A]
    elif ord_a <= ord_c <= ord_z:
        holes += lower_holes[ord_c - ord_a]

print(holes)