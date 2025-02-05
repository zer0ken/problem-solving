def solution(arr):
    count = 0
    while True:
        narr = list(arr)
        for i, num in enumerate(narr):
            if num >= 50 and num % 2 == 0:
                narr[i] = narr[i] // 2
            elif num < 50 and num % 2 == 1:
                narr[i] = narr[i] * 2 + 1
        if narr == arr:
            break
        arr = narr
        count += 1
    return count