def solution(numbers, n):
    acc = 0
    for num in numbers:
        acc += num
        if acc > n:
            return acc