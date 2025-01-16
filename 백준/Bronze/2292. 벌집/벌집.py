n = int(input())

acc = 1
for i in range(1, 100000000):
    if n <= acc:
        print(i)
        break
    acc += 6 * i