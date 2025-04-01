for _ in range(int(input())):
    try:
        x = int(input())
        if x < 0:
            raise ValueError()
    except:
        print('invalid input')
    else:
        print(x)