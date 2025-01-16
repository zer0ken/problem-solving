n = input()
int_n = int(n)
len_n = len(n)

if len_n == 1:
    p = int_n + 1
    if p == 10:
        print(11)
    else:
        print(p)
else:
    mid = len_n // 2 + len_n % 2
    l, r = n[:mid], n[mid:]
    p = l + l[::-1][len_n % 2:]
    if int(p) > int_n:
        print(p)
    else:
        n = str(int(l) + 1) + r
        int_n = int(n)
        len_n = len(n)
        mid = len_n // 2 + len_n % 2
        l, r = n[:mid], n[mid:]
        p = l + l[::-1][len_n % 2:]
        print(p)