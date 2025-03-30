X, Y = map(int, input().split())
Z = Y*100 // X
if Z >= 99:
    print('-1')
else:
    extra_game = (100*Y - (Z + 1)*X) / (Z - 99)
    print(int(extra_game) if int(extra_game) == extra_game else int(extra_game) + 1)