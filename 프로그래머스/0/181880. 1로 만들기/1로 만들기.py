def solution(arr):
    count = 0
    for num in arr:
        while num > 1:
            if num % 2 == 1:
                num -= 1
            num = num // 2
            count += 1
    return count