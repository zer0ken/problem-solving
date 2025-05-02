T = int(input())
N = int(input())
if T <= sum(map(int, input().split())):
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')