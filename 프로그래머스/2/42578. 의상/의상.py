def solution(clothes):
    from collections import Counter
    
    answer = 1
    counter = Counter(map(lambda x: x[1], clothes))
    for kind in counter:
        answer *= counter[kind] + 1
    return answer - 1