n, b = input().split()
b = int(b)

ord_a = ord('A')
ord_0 = ord('0')
ord_9 = ord('9')

v = 0
for digit in n:
    ord_digit = ord(digit)
    if ord_0 <= ord_digit <= ord_9:
        digit_decimal = ord_digit - ord_0
    else:
        digit_decimal = ord_digit - ord_a + 10
    v = v * b + digit_decimal 
print(v)