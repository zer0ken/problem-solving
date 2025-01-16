r = 31
m = 1234567891

h = 0

input()

for i, c in enumerate(input()):
    c = ord(c) - ord('a') + 1
    r_pow_i = 1
    for _ in range(i):
        r_pow_i *= r
        if r_pow_i > m:
            r_pow_i %= m
    h += c * r_pow_i

print(h % m)
    