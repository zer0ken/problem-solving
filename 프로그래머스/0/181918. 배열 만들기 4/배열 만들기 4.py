def solution(arr):
    stk = []
    for i in range(0, len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk