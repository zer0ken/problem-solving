k, d = map(int, input().split())
day_spent = 0
wrote = 0

while day_spent + k <= d:
    wrote += 1
    day_spent += k
    k *= 2

print(wrote)