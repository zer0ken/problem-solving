def solution(arr):
    stack = []
    last = arr[0]
    for v in arr[1:]:
        diff = v - last
        if diff == 1:
            stack.append('w')
        elif diff == -1:
            stack.append('s')
        elif diff == 10:
            stack.append('d')
        else:
            stack.append('a')
        last = v
    return ''.join(stack)