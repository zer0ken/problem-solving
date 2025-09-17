def solution(participant, completion):
    from collections import Counter
    return list(Counter(participant) - Counter(completion))[0]
