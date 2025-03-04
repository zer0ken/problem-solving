a, b = input(), input()

if a == 'null':
    print('NullPointerException\nNullPointerException')
    exit(0)
if b == 'null':
    print('false\nfalse')
    exit(0)

print(str(a == b).lower())
print(str(a.lower() == b.lower()).lower())