a_, b_ = map(int, input().split())

a, b = (a_, b_) if a_ > b_ else (b_, a_)
r = 1

while r != 0:
    r = a % b
    a = b
    b = r

print(a)
print(a_ * b_ // a)