toka = input()
if toka[0] == toka[-1] == '"' and len(toka) > 2:
    print(toka[1:-1])
else:
    print('CE')