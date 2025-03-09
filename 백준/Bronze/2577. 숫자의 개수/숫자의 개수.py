a = int(input())
b = int(input())
c = int(input())
product = int(a) * int(b) * int(c)

counter = [0] * 10
for digit in str(product):
    counter[int(digit)] += 1

for count in counter:
    print(count)