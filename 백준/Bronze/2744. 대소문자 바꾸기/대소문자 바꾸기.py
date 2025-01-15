word = input()

word2 = []
ord_a = ord('a')
ord_z = ord('z')
ord_A = ord('A')

for c in word:
    ord_c = ord(c)
    if ord_a <= ord_c <= ord_z:
        word2.append(chr(ord_c - ord_a + ord_A))
    else:
        word2.append(chr(ord_c - ord_A + ord_a))
print(''.join(word2))