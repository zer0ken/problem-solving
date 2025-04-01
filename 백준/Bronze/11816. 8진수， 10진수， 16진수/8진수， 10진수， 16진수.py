X = input()

if X.startswith('0x'):
    print(int(X, base=16))
elif X.startswith('0'):
    print(int(X, base=8))
else:
    print(int(X))