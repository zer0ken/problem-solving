from collections import deque

N = int(input())

if N <= 9:
    print(N + 1)
    exit(0)
    
count = 0
is_palindromes = [0] * (N + 1)
queue = deque(['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

while queue:
    p = queue.popleft()
    print('p!')
    for digit in range(1, 10):
        pp = f'{digit}{p}{digit}'
        if int(pp) > N:
            break
        print()
        queue.append(pp)
        is_palindromes[int(pp)] = 1
        if is_palindromes[int(pp) // 10]:
            count += 1
