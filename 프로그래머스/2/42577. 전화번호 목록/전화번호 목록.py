def solution(phones):
    phones.sort()
    
    for i in range(len(phones) - 1):
        if phones[i + 1].startswith(phones[i]):
            return False
    
    return True