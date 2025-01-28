def solution(numbers, k, s, l):
    results = []
    for number in numbers:
        num = int(number[s:s+l])
        if num > k:
            results.append(num)
    return results