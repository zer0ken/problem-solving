def solution(num_list):
    odds = 0
    evens = 0
    
    for n in num_list:
        if n % 2 == 1:
            odds = odds * 10 + n
        else:
            evens = evens * 10 + n
    return odds + evens