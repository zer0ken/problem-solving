budget = int(input())
for _ in range(int(input())):
    x, y = input().split()
    budget -= int(x) * int(y)
    if budget < 0:
        break
print('Yes' if budget == 0 else 'No')