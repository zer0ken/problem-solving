def solution(clothes):
    from collections import Counter
    
    kinds = Counter(map(lambda x: x[1], clothes))
    cases = 1
    for count in kinds.values():
        cases *= count + 1
    return cases - 1