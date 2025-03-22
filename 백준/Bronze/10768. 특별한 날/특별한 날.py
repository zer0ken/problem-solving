m, d = int(input()), int(input())

t = 100*m + d

if t == 218:
    print('Special')
elif t < 218:
    print('Before')
else:
    print('After')