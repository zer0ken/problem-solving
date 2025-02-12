t, e, f = map(int, input().split())
Max = t*3 + e*20 + f*120
t, e, f = map(int, input().split())
Mel = t*3 + e*20 + f*120

if Max == Mel:
    print('Draw')
elif Max > Mel:
    print('Max')
else:
    print('Mel')