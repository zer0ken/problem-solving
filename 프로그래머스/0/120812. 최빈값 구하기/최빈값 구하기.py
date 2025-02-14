def solution(arr):
    from collections import Counter
    
    counter = Counter(arr)
    if len(counter.keys()) == 1:
        return arr[0]
    
    commons = counter.most_common(2)
    return commons[0][0] if commons[0][1] != commons[1][1] else -1