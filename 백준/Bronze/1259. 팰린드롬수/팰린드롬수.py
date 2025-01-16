import sys

lines = sys.stdin.read().split()[:-1]

for line in lines:
    is_palindrome = True
    for i in range(len(line) // 2):
        if line[i] != line[-1 - i]:
            is_palindrome = False
            break
    print('yes' if is_palindrome else 'no')
    