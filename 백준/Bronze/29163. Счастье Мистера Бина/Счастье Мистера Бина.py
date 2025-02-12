n = int(input())
odd = len(list(filter(lambda x: x % 2, map(int, input().split()))))
print('Happy' if n - odd > odd else 'Sad')