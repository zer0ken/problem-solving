n = int(input())

top = '@' * n * 3 + ' '*n + '@' * n + '\n'
print(top * n, end='')

middle = ('@' * n + ' ' * n) * 2 + '@' * n + '\n'
print(middle * n * 3, end='')

bottom = '@' * n + ' '*n + '@' * n * 3 + '\n'
print(bottom * n, end='')
