def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    
    a, b = min(denom, numer), max(denom, numer)
    while a > 0:
        a, b = b % a, a
    
    return [numer // b, denom // b]