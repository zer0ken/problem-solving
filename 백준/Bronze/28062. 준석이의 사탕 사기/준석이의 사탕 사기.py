input()
a_n = sorted(list(map(int, input().split())))
sum_ = sum(a_n)

if sum_ % 2 == 1:
    for v in a_n:
        if v % 2 == 1:
            sum_ -= v
            break

print(sum_)